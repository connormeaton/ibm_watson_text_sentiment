from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions, EntitiesOptions, EmotionOptions
import json
import pandas as pd



df = pd.read_csv(r'C:\Users\conno\code\spaff_automation_git\notebooks\d1203.csv')

authenticator = IAMAuthenticator('OfL-cA76YVVr5V8-RrH9EZtOlFcGkNSPNldbRZMfR7XP')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)
natural_language_understanding.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

response_list = []
utt_list = df.word.tolist()
emotion_list = []

for i in utt_list:
    emotion_dict = {}
    emotion_dict['word'] = i
    try:
        response = natural_language_understanding.analyze(
            text=i,
            features=Features(sentiment=SentimentOptions(), emotion=EmotionOptions())).get_result()

    # print(json.dumps(response.result, indent=2))
        data = json.dumps(response, indent=2)
        data = json.loads(data)
        # temp_dict = ast.literal_eval(data[0])
        sentiment_score = data['sentiment']['document']['score']
        sentiment_label = data['sentiment']['document']['label']
        sadness = data['emotion']['document']['emotion']['sadness']
        joy = data['emotion']['document']['emotion']['joy']
        fear = data['emotion']['document']['emotion']['fear']
        disgust = data['emotion']['document']['emotion']['disgust']
        anger = data['emotion']['document']['emotion']['anger']
        emotion_dict['sentiment_score'] = sentiment_score
        emotion_dict['sentiment_label'] = sentiment_label
        emotion_dict['sadness'] = sadness
        emotion_dict['joy'] = joy
        emotion_dict['fear'] = fear
        emotion_dict['disgust'] = disgust
        emotion_dict['anger'] = anger

        emotion_list.append(emotion_dict)
        print(emotion_list)
    except:
        sentiment_score = 'NaN'
        sentiment_label = 'NaN'
        sadness = 'NaN'
        joy = 'NaN'
        fear = 'NaN'
        disgust = 'NaN'
        anger = 'NaN'
        
        emotion_dict['sentiment_score'] = sentiment_score
        emotion_dict['sentiment_label'] = sentiment_label
        emotion_dict['sadness'] = sadness
        emotion_dict['joy'] = joy
        emotion_dict['fear'] = fear
        emotion_dict['disgust'] = disgust
        emotion_dict['anger'] = anger

        emotion_list.append(emotion_dict)
        print(emotion_list)

        pass


df = pd.DataFrame(emotion_list)
df.to_csv('1203_nlu_demo.csv')

print(df)
