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
eiffelTower = "https://en.wikipedia.org/wiki/Eiffel_Tower#/media/File:Tour_Eiffel_Wikimedia_Commons_(cropped).jpg"

#Set the response parameter
landmark_response = computervision_client.analyze_image(eiffelTower, details=["landmarks"]) 
#Print the brand name and other related info
print(landmark_response)

#Check if landmark detail exists
for landmark_category in landmark_response.categories:
    if landmark_category.detail is not None:
        for landmark in landmark_category.detail.landmarks:
            landmark.append(landmark.name)

print(landmark)