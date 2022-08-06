from dotenv import load_dotenv
import os
import requests

load_dotenv()

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']
print(PETFINDER_API_KEY)
def get_Oauth_token():
    resp = requests.get('https://api.petfinder.com/v2/oauth2/token',
                        params = {"grant_type":"client_credentials",
                        "client_id":PETFINDER_API_KEY,
                        "client_secret":PETFINDER_SECRET_KEY})

    json = resp.json()

    return json["access_token"]