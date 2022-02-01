import pandas
import numpy 


def run(jobID, dataInput):
  """
  title:: 
      run
  description:: 
      Run the model/get the predictions according the service.
  inputs::
      jobID 
            Job ID from datashop application
      dataInput
           input Payload For the Service
  returns::
      insightsDataFileLocation
           insights data file location. 
  """
  
  #Using the model using sagemaker.
  # ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
  # runtime= boto3.client('runtime.sagemaker')
  # print (f"Attempting to predict using {ENDPOINT_NAME}")
  # response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
  #                           ContentType='text/csv',
  #                           Body= payload)
  # result = json.loads(response['Body'].read().decode())
  # print (f"Predictions Generated \n {result}")
  # result_array = result.items()
  
  result_array = eval(dataInput)
  #creating insightFile in the lambda temporary folder
  df = pandas.DataFrame(result_array)
  insightsDataFileLocation = f"/tmp/{jobID}-insights.csv"
  df.to_csv(insightsDataFileLocation)
  return insightsDataFileLocation
