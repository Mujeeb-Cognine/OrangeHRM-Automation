import secrets
import hashlib
import base64
from urllib.parse import urlparse, parse_qs

import requests


def register_client():
    # Implement logic to register a client and return client_id, client_secret, and redirect_uri
    client_id = '004c874fdb870e25693ab5bbd8b115a6'
    # client_secret = 'your_client_secret'
    redirect_uri = 'http://fortest-demo.orangehrmlive.com'
    # return client_id, client_secret, redirect_uri
    return client_id, redirect_uri


def generate_code_verifier():
    # Generate a random string as the code verifier
    return secrets.token_urlsafe(64)


def generate_code_challenge(code_verifier):
    # Generate SHA256 hash of code verifier and encode with Base64 URL encoding
    code_challenge = hashlib.sha256(code_verifier.encode()).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).rstrip(b'=').decode()
    return code_challenge


def build_authorization_url(client_id, code_challenge, redirect_uri, state):
    # Build the authorization URL
    authorization_url = (
        f'http://fortest-demo.orangehrmlive.com/web/index.php/oauth2/authorize?'
        f'response_type=code&state={state}&code_challenge_method=S256&'
        f'code_challenge={code_challenge}&client_id={client_id}&'
        f'redirect_uri={redirect_uri}'
    )
    return authorization_url


def parse_authorization_response(response_url):
    # Parse the authorization response URL and extract code and state
    # Example response_url: http://your_redirect_uri.com?code=authorization_code&state=state_provided_in_step_1
    parsed_url = urlparse(response_url)
    query_params = parse_qs(parsed_url.query)
    authorization_code = query_params.get('code')[0]
    state = query_params.get('state')[0] if 'state' in query_params else None
    return authorization_code, state


def request_access_token(client_id, authorization_code, redirect_uri, code_verifier):
    # Make a POST request to the token endpoint to obtain the access token
    token_url = 'http://fortest-demo.orangehrmlive.com/web/index.php/oauth2/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'client_id': client_id,
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri,
        'code_verifier': code_verifier,
    }
    response = requests.post(token_url, headers=headers, data=data)

    print(response.content)  # Print the response content for debugging

    try:
        response.raise_for_status()  # Raise an error for 4xx and 5xx responses
        return response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
        return None


def extract_access_token(response_json):
    # Extract and return the access token from the token response
    access_token = response_json.get('access_token')
    return access_token
