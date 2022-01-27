import boto3
import botocore

def __get_s3_client():
    """
    title:: 
        run
    description:: 
        takes dataset URL and jobID as input, download the dataset and read the input
    inputs:: 
    jobID 
       Job ID from datashop application
    dataFileURL
        Downloadable URL of the dataset
        
    returns:: 
    payloadforservice
        payload for model/service
    
    """
    return boto3.client('s3', region_name="ap-southeast-2")
    
    
def upload_file(bucket_name, key_name, file_path):
    """
    title:: 
        upload_file
    description:: 
        Generate downloadable link for the file.
    inputs:: 
        bucket_name
             The name of the bucket to upload to.
        key_name 
             The name of the key to upload to.
        file_path
             The path to the file to upload.
    returns:: 
        Downloadable link for the file.   
    """
    fileName = file_path.split("/")[-1]
    print(f"Uploading {file_path} to {bucket_name}/{key_name}")
    response = __get_s3_client().upload_file(file_path, bucket_name, f"{key_name}/{fileName}", ExtraArgs={'ACL': 'public-read'})
    return f"https://{bucket_name}.s3.ap-southeast-2.amazonaws.com/{key_name}/{fileName}" 