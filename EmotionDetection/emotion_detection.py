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
    emotion_response = {}

    if response.status_code == 200:
        emotion_response   = formatted_response['emotionPredictions'][0]['emotion']  
        emotion_response['dominant emotion'] = max(emotion_response, key=emotion_response.get)
    elif response.status_code == 400:
        emotion_response.update(    {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion":None
        } )
    # Returning a dictionary containing emotion prediction results
    return emotion_response