import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('iNc2yHHlYAQED17JOkDFSwAZgbaJ_7kvjO3iLZx-a_ub')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/6e6385db-5447-4c85-921a-ba73851865f7%27')

text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

text2 = 'I am happy'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()

# print(json.dumps(tone_analysis, indent=2))
tone_JSON = json.dumps(tone_analysis, indent=2)
print(tone_JSON)

posCounter = 0
negCounter = 0

if 'joy' in tone_JSON:
    posCounter += 1
else:
    negCounter +=1


print(posCounter)
print(negCounter)


#print(tone_JSON['document_tone']['tones']['score'])