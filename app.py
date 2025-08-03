import os
from dotenv import load_dotenv
from src.constants import AWS_SECRET_ACCESS_KEY_ENV_KEY, AWS_ACCESS_KEY_ID_ENV_KEY, REGION_NAME

s3_client = None
s3_resource = None

load_dotenv()

if s3_resource is None or s3_client is None:
    __access_key_id = os.getenv("AWS_ACCESS_KEY_ID_ENV_KEY",)  
    __secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY_ENV_KEY",)
    
    if __access_key_id is None:
        raise Exception(f"Environment variable: {AWS_ACCESS_KEY_ID_ENV_KEY} is not set.")
    if __secret_access_key is None:
        raise Exception(f"Environment variable: {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set.")
