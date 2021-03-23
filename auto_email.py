import os
from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

FROM_EMAIL = config("SENDER_EMAIL")


class SendMail(object):
    """This class is for auto_sending email when a CSM is assigned an account """   
    
    @classmethod
    def notify_email(cls,email,name,records_data):
        
        from_email= Email(FROM_EMAIL)
        to_email = To(email)
        subject= f'You have been assigned to account : {records_data.get("related_data").get("Account_Name").get("name")}'
        content= Content(
            "text/html", 
            f"""
            <img src="https://i.ibb.co/X4xqHkW/logo.png" alt="Yodo1 Fish">
            <p>
            <h2>Dear <span style="color:black;font-weight:bold">{name}</span>,</h2>
            </p>          
            <p>
            Following the change of stage to <span style="color:black;font-weight:bold">Closed (Won)</span> in the {records_data.get("related_data").get("Account_Name").get("name")} you have been automatically assigned to it.
            </p>                     
            <br>
            The Yodo1 Developer Support Team
            """
            )        
        try:
            mail = Mail(from_email, to_email, subject, content)
            mail_json = mail.get()
            sg = SendGridAPIClient(config("SENDGRID_TOKEN"))
            response = sg.client.mail.send.post(request_body=mail_json)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)



    @classmethod
                            
    def SendDynamic(cls,email,name,records_data=None ):
        """ Send a dynamic email to a list of email addresses
            :returns API response code:raises Exception e: raises an exception """
        # create Mail object and populate
        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=email)
        # pass custom values for our HTML placeholders
        message.dynamic_template_data = {
            'name':name,
            "account_name":f'{records_data.get("related_data").get("Account_Name").get("name")}'
           
        }
        message.template_id = "d-d5fb291dbb394117bb81f799aba665c8"
        # create our sendgrid client object, pass it our key, then send and return our response objects
        try:
            sg = SendGridAPIClient(config("SENDGRID_TOKEN"))
            response = sg.send(message)
            code, body, headers = response.status_code, response.body, response.headers
            print(f"Response code: {code}")
            print(f"Response headers: {headers}")
            print(f"Response body: {body}")
            print("Dynamic Messages Sent!")
        except Exception as e:
            print("Error: {0}".format(e))
        return str(response.status_code)




#Template ID: d-d5fb291dbb394117bb81f799aba665c8 


