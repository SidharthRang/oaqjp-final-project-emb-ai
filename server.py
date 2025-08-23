from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def detectEmotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    responseText = 'For the given statement, the system response is '
    for key in response:
        if key == "dominant_emotion":
            responseText += f'The dominant emotion is {response[key]}.'
            break
        if key == "sadness":
            responseText += f'\'{key}\': {response[key]}.'
        responseText += f'\'{key}\': {response[key]},'
    return responseText

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
