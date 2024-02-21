from google.cloud import storage
from google.auth import compute_engine
import os
import json
from google.oauth2 import service_account
import requests

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\Users\karun\Downloads\service.json'


def stop_sql_instances(project_id, instance_ids, zone):
    credentials = compute_engine.Credentials()
    client = storage.Client()

    for instance_id in instance_ids:
        # Formulate the instance URL
        instance_url = f'https://sqladmin.googleapis.com/v1/projects/{project_id}/instances/{instance_id}'
        
        print(instance_url)
        # Set the request body to stop the instance
        request_body = {
            "settings": {
                "activationPolicy": "NEVER"
            }
        }

        # Send a PATCH request to update the instance settings
        client._http.patch(instance_url, json=request_body)

        print(f"Instance {instance_id} has been stopped.")

if __name__ == "__main__":
    # Replace these with your actual values
    project_id = "python-practice-407605"
    instance_ids = ["db-instance-1", "destroy-db"]  # Add more instance IDs as needed
    zone = "us-central1-c"

    stop_sql_instances(project_id, instance_ids, zone)
