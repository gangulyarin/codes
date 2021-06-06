import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('rE8iV2c7J7Z0QCZQdrC8x6q0BvzWAw1uBzPf-qd6AWiH')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/ebf5130d-3c9a-4020-a9a8-7582ecf6d8bb')
def sendTone(text):
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()
    
    return json.dumps(tone_analysis, indent=2)