import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input, headers=headers)
    json_response = json.loads(response.text)
    emotionPrediction = json_response['emotionPredictions'][0]
    emotionMention = emotionPrediction['emotionMentions'][0]
    emotion = emotionMention['emotion']
    dominant_emotion = 'anger'
    for key in emotion:
        value = emotion[key]
        if (value > emotion[dominant_emotion]):
            dominant_emotion = key
    emotion['dominant_emotion'] = dominant_emotion
    return emotion