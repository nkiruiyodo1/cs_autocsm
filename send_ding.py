import requests

url = 'https://oapi.dingtalk.com/robot/send?access_token=fc775aeb65cbfb404c497e1c699d84f9abf058e6f5fae8623b4ade37ff951954'

def send_to_dingtalk(account_name, account_owner, cs_owner, country):
    data = {"msgtype": "markdown", "markdown": {"title": "Revenue changed alert",
                                                "text": "#### Account name: *{0}* \n"
                                                        "#### Account owner: *{1}* \n"
                                                        "#### CS Owner: *{2}* \n"
                                                        "#### Developers country: *{3}* "
                                                        "".format(
                                                    account_name,
                                                    account_owner,
                                                    cs_owner,
                                                    country
                                                )}}
    r = requests.post(url, json=data)
    print(r.json())

send_to_dingtalk('Test', 'Test', 'Test', 'Test')