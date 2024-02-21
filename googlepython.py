import os
from google.oauth2 import service_account
from google.cloud import storage
import json

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\Users\karun\Downloads\service.json'

storage_client = storage.Client()

bucket_name="python_practice_storage"

"""bucket = storage_client.bucket(bucket_name)

   
bucket = storage_client.create_bucket(bucket, location="US") 

print(f'Bucket {bucket_name} created')

"""
karu = storage_client.list_blobs(bucket_name) 

for file_list in karu:
    print(file_list.name)

   

    