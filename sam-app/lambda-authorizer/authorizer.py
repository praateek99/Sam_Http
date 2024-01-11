def lambda_handler(event, context):
    # Extract the token from the Authorization header
    headers = event.get('headers', {})
    token = headers.get('authorization', '').lower()

    if token == 'bearer welcome123':
        return {
            "isAuthorized": True,
            "context": {
                "user": "authorizedUser",
                "anyOtherParam": "values"
            }
        }
    else:
        return {
            "isAuthorized": False,
            "context": {
                "user": "unauthorizedUser",
                "anyOtherParam": "values"
            }
        }
