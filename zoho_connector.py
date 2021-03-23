import zcrmsdk as yodocrm
from config import *
import json
import logging
from pprint import pprint
from auto_email import SendMail
import random
import os
import collections
import pickle5 as pickle


logging.basicConfig(filename='LOGS_PATH', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

CONFIG = {
            "client_id": ZOHO_CLIENT_ID,
            "client_secret": ZOHO_CLIENT_SECRET,
            "redirect_uri": ZOHO_REDIRECT_URI,
            "token_persistence_path": STORAGE_PATH,   
            "currentUserEmail": ZOHO_CURRENT_USER_EMAIL,
            "accounts_url":ZOHO_ACCOUNTS_URL,
            "apiBaseUrl":ZOHO_API_BASE_URL,

        }

class SDKInitializer(object):    

    def __init__(self):     
    
        yodocrm.ZCRMRestClient.get_instance().initialize(CONFIG)
        oauth_client = yodocrm.ZohoOAuth.get_client_instance()                
        refresh_token = REFRESH_TOKEN
        user_identifier = ZOHO_CURRENT_USER_EMAIL
        oauth_tokens = oauth_client.generate_access_token_from_refresh_token(refresh_token,user_identifier)
    
    def get_related_records(self):
        """
        By default the account is not hooked to the deals module,so we need to reference the related field to get those fields.
        """
        try:  
            to_update_records = []    
            records = self.get__accounts_records()            
            for rec in records:                          
                             
                record = yodocrm.ZCRMRecord.get_instance('Accounts',rec["id"]) 
                try:
                    # get related fields
                    resp = record.get_relatedlist_records('Deals')   
                except :
                    continue

                record_ins_arr = resp.data   
                for record_ins in record_ins_arr:                     
                    def get_field_data():
                        product_dict = {}
                        product_data = record_ins.field_data                     
                        for k,v in product_data.items():
                            product_dict[k]=v 
                        return product_dict  
                    payload_records = {
                        "id":rec["id"],
                        "entity_id":record_ins.entity_id,
                        "created_by":record_ins.created_by.name,
                        "modified_by":record_ins.modified_by.id,
                        "owner_name":record_ins.owner.name,
                        "created_time":record_ins.modified_time,
                        "field_data":rec["fields_data"],     
                        "related_data":get_field_data()  
                    }                   

                    if payload_records.get("related_data").get("Stage") == 'Closed (Won)' and payload_records.get("field_data").get("CS_Owner")==None:
                        to_update_records.append(payload_records)
                        
            return to_update_records

        except yodocrm.ZCRMException as ex:
            print(ex.status_code)
            print(ex.error_message)
            print(ex.error_code)
            print(ex.error_details)
            print(ex.error_content)
    
 
    def get__accounts_records(self):
        """
        Get all the acount records.

        """
        try:
            module_ins = yodocrm.ZCRMModule.get_instance('Accounts')  
            all_records_data = []                  
            resp = module_ins.get_records()
            record_ins_arr = resp.data
            for record_ins in record_ins_arr: 
                def get_field_data():
                    product_dict = {}
                    product_data = record_ins.field_data                     
                    for k,v in product_data.items():
                        product_dict[k]=v 
                    return product_dict  

                payload = {
                    "id":record_ins.entity_id,
                    "fields_data": get_field_data(),
                }

                all_records_data.append(payload)               

            return all_records_data[20:]     

        except yodocrm.ZCRMException as ex:
            print(ex.status_code)
            print(ex.error_message)
            print(ex.error_code)
            print(ex.error_details)
            print(ex.error_content)     
    
    def random_user(self):      

        user_file = "cs_owners.txt"

        # Load the users file into a deque
        with open(user_file, 'r') as f:
            users = collections.deque(f.read().splitlines())    

        # Rotate the users
        users.rotate(-1)

        # Save the rotated users
        with open(user_file, 'w') as f:
            for s in users:
                f.write("%s\n" % s)
        
        # Print the top user
        return(users[0])

    def update_records(self):
        """
        Update the account records ,with the CS Owner

        """
        try:           
            deals_won = self.get_related_records()
            if len(deals_won)> 0:                
                for deal in deals_won:
                    record = yodocrm.ZCRMRecord.get_instance('Accounts',deal["id"])

                    users_info = [{"name":"Nir","email":"nirbendavid@yodo1.com"},{"name":"Polina","email":"polinaozhylevska@yodo1.com"},
                                    {"name":"Jamal","email":"jamalali@yodo1.com"},{"name":"Zain","email":"muhammadzain@yodo1.com"}]
                                         

                    random_name= self.random_user()

                    for user in users_info:
                        if user["name"] == random_name:
                            user_info = {
                                "name" :user["name"],
                                "email":user["email"],
                                "records_data":deal
                            }
                            print(record.entity_id)
                            record.set_field_value('CS_Owner', user_info["name"])      
                            res = record.update() 
                            if res.status_code == 200:
                                print("email send")
                                SendMail.SendDynamic(**user_info)   
            else:
                return f'No new game'                 
            
        except yodocrm.ZCRMException as ex:
            print(ex.status_code)
            print(ex.error_message)
            print(ex.error_code)
            print(ex.error_details)
            print(ex.error_content)

