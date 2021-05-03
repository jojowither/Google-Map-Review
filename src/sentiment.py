from cnsenti import Sentiment
from cnsenti import Emotion
from hanziconv import HanziConv
import pandas as pd
import math
from termcolor import colored


def sentiment_analyze(text):
    if isinstance (text, float) and math.isnan(text):
        text = ''

    text = HanziConv.toSimplified(text)

    senti = Sentiment()
    sentiment_result = senti.sentiment_count(text)

    emotion = Emotion()
    emotion_result = emotion.emotion_count(text)
    emotion_result['樂'] = emotion_result.pop('乐')
    emotion_result['懼'] = emotion_result.pop('惧')
    emotion_result['惡'] = emotion_result.pop('恶')
    emotion_result['驚'] = emotion_result.pop('惊')

    return sentiment_result, emotion_result



if __name__ == "__main__":
    filepath = '../data/newest_gm_reviews.csv' 
    reviews = pd.read_csv(filepath)
    texts = reviews['caption']
    sentiment_results = []
    emotion_results = []
    for text in texts:
        sentiment_result, emotion_result = sentiment_analyze(text)
        sentiment_results.append(sentiment_result)
        emotion_results.append(emotion_result)

    reviews['sentiment'] = sentiment_results
    reviews['emotion'] = emotion_results

    new_file = '../data/newest_gm_reviews_with_sent.csv' 
    reviews.to_csv(new_file, index=False)
    print(colored('Finish', 'cyan'))