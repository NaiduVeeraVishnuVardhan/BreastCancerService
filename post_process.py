import aws_s3
import json
import requests
import zipfile
import os

def run(jobID, dataLocation):
   """
    title:: 
        run
    description:: 
        -	This takes insightsDataFileLocation and jobID as Input, upload the insights file to s3 and get the downloadable link for the same.
    inputs:: 
    jobID 
       Job ID from datashop application
    dataFileURL
        Downloadable URL of the dataset
        
    returns:: 
        response from the Datashop application
    """
   insightsS3Link = aws_s3.upload_file("data-shop-backend", "insights", dataLocation)
   return __updateJob(jobID, insightsS3Link)


def __updateJob(jobID, insightsS3Link):
    """
    title:: 
        __updateJob
    description:: 
        Update the data application with insightsLink.
    inputs:: 
    jobID 
       Job ID from datashop application.
    insightsS3Link
       Downloadable URL of the insights.
        
    returns:: 
    payloadforservice
        response from the datashop application.
    """
    status_map = {'status_code': '', 'json_response': ''}    
    dataShopEndpointURL = "http://52.64.118.100:8000/api/job/updateJob"
    payload = json.dumps({
                "insightFileURL": insightsS3Link,
                "jobid":jobID
            })  
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("PUT", dataShopEndpointURL, headers=headers, data=payload)
    status_map["json_response"] = json.dumps(response.text)
    status_map["status_code"] = response.status_code
    
    return status_map
    
    
# def zip_output_files(files_to_zip):
#
#     zip_file = "/tmp/post-process" + files_to_zip + ".zip"
#
#     with zipfile.ZipFile(zip_file, 'w') as zipObj:
#         for folderName, subfolders, filenames in os.walk(zip_file):
#             for filename in filenames:
#                 filePath = os.path.join(folderName, filename)
#                 zipObj.write(filePath, basename(filePath))
#     print(f"Files zipped to : {zip_file}")
