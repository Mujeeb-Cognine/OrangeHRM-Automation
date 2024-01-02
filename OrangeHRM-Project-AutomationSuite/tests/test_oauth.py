from auth_client_utils.oauth_functions import register_client, generate_code_verifier, generate_code_challenge, \
    build_authorization_url, parse_authorization_response, request_access_token, extract_access_token


def test_oauth_flow():
    # Register a client
    # client_id, client_secret, redirect_uri = register_client()
    client_id, redirect_uri = register_client()

    # Generate code verifier and challenge
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)

    # Step 3: Build authorization URL
    authorization_url = build_authorization_url(client_id, code_challenge, redirect_uri, state='your_state')

    # Manually open the authorization_url in a browser, and let the user interact and provide consent

    # Step 4: Simulate the authorization response
    # This step will be manual or can be automated using a tool like Selenium
    # For simplicity, I'm simulating the response manually here
    authorization_response_url = 'https://fortest-demo.orangehrmlive.com/?code=authorization_code&state=your_state'
    authorization_code, state = parse_authorization_response(authorization_response_url)

    # Step 5: Request access token
    token_response = request_access_token(client_id, authorization_code, redirect_uri, code_verifier)

    # Step 6: Extract access token
    access_token = extract_access_token(token_response)

    # Step 7: Use access token to make API requests (not shown here)
    assert access_token is not None
