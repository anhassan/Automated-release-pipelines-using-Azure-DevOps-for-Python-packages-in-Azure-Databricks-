import requests
import json


def list_databricks_clusters(databricks_instance_name,authorization_token):
  
  headers={"Authorization": "Bearer "+authorization_token}
  
  url= "https://" + databricks_instance_name + "/api/2.0/clusters/list"
  try:
      response = requests.get(url, headers=headers)
      clusters_info = response.json()["clusters"]
      cluster_names = [cluster_info["cluster_name"] for cluster_info in clusters_info]
  except Exception as error:
      print("Error : {}".format(error))
      
  return cluster_names


def list_databricks_job_clusters(databricks_instance_name,authorization_token):
  
    cluster_names = list_databricks_clusters(databricks_instance_name,authorization_token)
    job_cluster_names = [cluster_name for cluster_name in cluster_names if cluster_name.startswith("job")]
    
    return job_cluster_names


def list_databricks_all_purpose_clusters(databricks_instance_name,authorization_token):
  
    cluster_names = list_databricks_clusters(databricks_instance_name,authorization_token)
    all_purpose_cluster_names = [cluster_name for cluster_name in cluster_names if not cluster_name.startswith("job")]
    
    return all_purpose_cluster_names

