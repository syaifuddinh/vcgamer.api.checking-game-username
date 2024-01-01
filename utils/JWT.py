import jwt
from datetime import datetime, timedelta

SECRET_KEY = '_@CHECKGAMEID_'

def GetExpiredDate():
    current_datetime = datetime.now()

    # Calculate the date and time for 3 days later
    three_days_later = current_datetime + timedelta(days=3)

    # Format the date as "yyyy-mm-dd hh:mm:ss"
    formatted_date = three_days_later.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_date

def GetJWTExp():
    result = datetime.utcnow() + timedelta(days=3)

    return result

def Generate(email):
    """
    Generate a JWT token for the given username.
    """
    # Set the expiration time for the token (e.g., 1 hour)
    expiredDate = GetExpiredDate()
    expiration_time = GetJWTExp()

    # Create the payload
    payload = {
        'email': email,
        'expiredDate': expiredDate,
        'exp': expiration_time
    }

    # Generate the JWT token
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token

def Decode(jwt_token):
    result = None
    try:
        decoded_payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        result = decoded_payload
    except jwt.ExpiredSignatureError:
        print("JWT has expired")
    except jwt.InvalidTokenError:
        print("Invalid JWT")

    return result