import requests
import json


def list_databricks_jobs(databricks_instance_name,authorization_token):
  
  headers={"Authorization": "Bearer "+authorization_token}
  
  url= "https://" + databricks_instance_name + "/api/2.0/jobs/list"
  try:
      response = requests.get(url, headers=headers)
      job_names = [job['settings']['name']  for job in response.json()['jobs']]
  except Exception as error:
      print("Error : {}".format(error))
        
  return job_names