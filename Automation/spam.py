import requests

# https://api-console.zoho.com/ -> self client -> give scopes,time duration and description -> get the code -> past it in the zoho_api_self_client_api variable
token_dict = {"refresh_token": None}
zoho_api_self_client_api = "1000.418f7db1aa1ece6849a4e73563d265dd.b3227ba7b8b83601d7af8d319f50288c"
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


def spam_messages(access_token,user,message):
    url = f'https://cliq.zoho.com/api/v2/buddies/{user}/message'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'sync-message': 'true'
    }
    payload = {
        'text': message
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code


at=access_token_generator()
response = 204
while(response == 204):
    response = spam_messages(at,"benny.harvin@zohocorp.com","poda panni")
    print(response)



# import requests

# # https://api-console.zoho.com/ -> self client -> give scopes,time duration and description -> get the code -> past it in the zoho_api_self_client_api variable
# token_dict = {"refresh_token": None}
# zoho_api_self_client_api = ""
# client_id = ""
# client_secret = ""

# url = "https://accounts.zoho.com/oauth/v2/token?"\
#     f"code={zoho_api_self_client_api}&"\
#     f"client_id={client_id}&"\
#     f"client_secret={client_secret}&"\
#     "grant_type=authorization_code"
# response = requests.request("POST", url).json()

# if token_dict["refresh_token"] is None:
#     token_dict["refresh_token"] = response["refresh_token"]
# refresh_token = token_dict["refresh_token"]


# # Get the Refersh token from above step and use the below code to keep getting access token for 60min.
# def access_token_generator():
#     url = "https://accounts.zoho.com/oauth/v2/token?"\
#         f"refresh_token={refresh_token}&"\
#         f"client_id={client_id}&"\
#         f"client_secret={client_secret}&"\
#         "grant_type=refresh_token"

#     access_response = requests.request("POST", url).json()
#     access_token = access_response["access_token"]
#     return access_token


# def spam_messages(access_token,user,message):
#     url = f'https://cliq.zoho.com/api/v2/buddies/{user}/message'
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Content-Type': 'application/json'
#     }
#     payload = {
#         'text': message
#     }
#     response = requests.post(url, headers=headers, json=payload)
#     return response.status_code


# at=access_token_generator()
# response = 204
# while(response == 204):
#     response = spam_messages(at,"email goes here","message goes here")
#     print(response)