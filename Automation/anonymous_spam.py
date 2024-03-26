import requests

# https://api-console.zoho.com/ -> self client -> give scopes,time duration and description -> get the code -> past it in the zoho_api_self_client_api variable
token_dict = {"refresh_token": None}
zoho_api_self_client_api = "1000.b95e425ea28f8a3c9e6c2eced0043ac7.5dfe1549cba86ffedace70ba2e591926"
client_id = "1000.CZX7RTX1UYBONDQPGW85P8DE6B7W1J"
client_secret = "c7d62ba7ca537f43611a0d0ad58dfc1050ea2509c7"

url = "https://accounts.zoho.com/oauth/v2/token?"\
    f"code={zoho_api_self_client_api}&"\
    f"client_id={client_id}&"\
    f"client_secret={client_secret}&"\
    "grant_type=authorization_code"
    
response = requests.request("POST", url).json()

if token_dict["refresh_token"] is None:
    token_dict["refresh_token"] = response["refresh_token"]
refresh_token = token_dict["refresh_token"]


# Get the Refersh token from above step and use the below code to keep getting access token for 60min.
def access_token_generator():
    url = "https://accounts.zoho.com/oauth/v2/token?"\
        f"refresh_token={refresh_token}&"\
        f"client_id={client_id}&"\
        f"client_secret={client_secret}&"\
        "grant_type=refresh_token"

    access_response = requests.request("POST", url).json()
    access_token = access_response["access_token"]
    return access_token


def spam_messages(user_name,access_token,user,title,message):
    url = f'https://cliq.zoho.com/api/v2/buddies/{user}/message'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'sync-message': 'true'
    }
    payload = {"text":f"{message}","bot":{"name":user_name},"card":{"title":title,"theme":"modern-inline"}}
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code


at=access_token_generator()
response = spam_messages("stressed_owl",at,"chhaya.sukhdev@zohocorp.com","Hiii","How cool is this on a scale from one to ten.")
print(response)



