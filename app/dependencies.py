from fastapi import HTTPException, status
from app import config
from requests import get

class AccountAPI(object):
    def get_user_email(email):
        # First, verify the email exists in the account database via Account API
        response = get(f"{config.ACCOUNT_API_ENDPOINT}?email={email}",
                        headers={"Authorization": f"Bearer {config.API_KEY}"}
                      )
        
        if response.status_code != 200:
            # If the response isn't successful, assume the email isn't valid or there's an error
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email not found or internal error")
        else:
            return True