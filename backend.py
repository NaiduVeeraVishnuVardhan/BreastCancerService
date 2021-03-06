import requests
import json
def upload_document(file_name, file_path):
  url = "http://13.55.64.166:8000/api/upload/uploadDocument"
  payload={}
  files=[
    ('documentFile',(file_name,open(file_path+file_name,'rb'),'text/csv'))
  ]
  headers = {}
  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  print(response.text)
  response_dict = json.loads(response.text)
  inputdata = response_dict["data"]["documentFileUrl"]
  print(inputdata)
  return inputdata["original"]

def upload_image(file_name, file_path):
  url = "http://13.55.64.166:8000/api/upload/uploadImage"
  payload={}
  files=[
    ('imageFile',(file_name,open(file_path+file_name,'rb','image/png')))
  ]
  headers = {}
  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  print(response.text)
  response_dict = json.loads(response.text)
  inputdata = response_dict["data"]["imageFileURL"]
  print(inputdata)
  return inputdata["original"]
  

  