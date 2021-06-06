import flask
from flask import request, Flask, render_template
from toneAnalyzer import sendTone
from textToSpeech import speak
import json

app = flask.Flask(__name__, static_url_path='/static')
#app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def root():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    speak(text)
    toneResponse = json.loads(sendTone(text))
    return render_template("index.html",jsonobj=toneResponse['document_tone']['tones'])

#app.run()
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
