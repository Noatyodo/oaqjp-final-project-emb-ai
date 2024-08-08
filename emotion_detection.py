import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  
    '''Function to run emotion detection using the appropriate Emotion Detection function 
    that takes a string input (text_to_analyse) '''
    url    = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj  = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    

    formatted_return = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': '<name of the dominant emotion>'
    }

    return response.text  # Return the response text from the API