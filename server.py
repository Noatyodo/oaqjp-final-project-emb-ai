from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Return a formatted string with the sentiment label and score
    return """For the given statement, the system response is 'anger': %(anger)s, 
    'disgust': %(disgust)s, 'fear': %(fear)s, 'joy': %(joy)s and 'sadness': %(sadness)s. 
    The dominant emotion is %(dominant emotion)s. """%response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)