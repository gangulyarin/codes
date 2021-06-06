from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

authenticator = IAMAuthenticator('vmObtdlv3HJVSnJTvoh8W3O1OKwo9pfzU25kv5yO_PXT')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/64cf4ad2-974f-423d-9e4a-bce51f8d0440')

def speak(text):
    if (os.path.exists('static/voice.wav')):
        os.remove('static/voice.wav')
    with open('static/voice.wav', 'wb') as audio_file:

        audio_file.write(
            text_to_speech.synthesize(
                text,
                voice='en-US_AllisonV3Voice',
                accept='audio/wav'
            ).get_result().content)