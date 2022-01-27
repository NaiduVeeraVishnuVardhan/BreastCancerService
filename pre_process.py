import requests
import zipfile
import os
"""
    title:: pre_process
    description:: takes dataset URL and jobID as input, download the dataset and read the input.
    
"""
def run(jobID, dataFileURL):
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
    #Extracting file name from dataFileURL
    fileName = dataFileURL.split("/")[-1]
    input_file = f"/tmp/{jobID}-{fileName}"  
    
    # Dowloading dataset
    req = requests.get(dataFileURL)
    with open(input_file, 'wb') as fileHandle :
        fileHandle.write(req.content)
    print(f"File Downloaded to {input_file}")
    
    # Extracting all files if the datafile is zip.  
    if fileName.endswith(".zip"):
        input_file = extract_zip_file(input_file)
    if os.path.isdir(input_file):
        payloadforservice = "<test response goes here>"
        print("loop through the folder and read all files")
        #code to loop through extracted zip folder
        for filename in os.listdist(input_file):
            f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                print(f)
                # update payloadforservice for each iteration
    else:
        with open(input_file) as f: 
            payloadforservice = f.read()
    
    return payloadforservice




def extract_zip_file(zipped_file):
    """
    title:: 
        extract_zip_file
    description:: 
        extract the files in the zip file.
    inputs::
        zipped_file
             URL for the downloaded zipfile.
    returns::
         extracted_folder
              extracted zip files 
    """

    extracted_folder = "/tmp/pre-process" + zipped_file.replace(".zip", "")
    with zipfile.ZipFile(zipped_file, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder)
    print(f"Files extracted to {extracted_folder}")
    
    return extracted_folder