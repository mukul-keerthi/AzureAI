###########################################################
### Recognize brands using Azure AI.                
### Author: Mukul                                      
### Date: 17th Sept 2022
### Version: 1.0
###########################################################

# Import dependencies 
from urllib import response
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision import operationStatusCodes
from azure.cognitiveservices.vision.computervision import VisualfeatureTypes
from mrest.authentication import CognitiveServicesCredentials

import os

#Authenticate
subscription_key = os.environ["AZURE_CV_KEY"]
endpoint = os.environ["AZURE_CV_ENDPOINT"] 

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

#Input image
logo = "https://en.wikipedia.org/wiki/Volkswagen#/media/File:Volkswagen_ID.3_at_IAA_2019_IMG_0779.jpg"

#Set the response parameters
brand_response = computervision_client.analyze_image(logo, visual_features=["Brands"],max_candidates=1) 
print(f"Brands are {[brand.name for brand in brand_response.brands]}")