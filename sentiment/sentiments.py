from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
#nltk.download('vader_lexicon')
import pandas as pd
sid = SentimentIntensityAnalyzer()

df = pd.read_csv('sentimientos_ingles.csv')
df['sentimiento'] = df['mensaje'].apply(lambda i: sid.polarity_scores(i)['compound'])
df.to_csv("mensajes_con_sentimientos.csv")



# resultados = sid.polarity_scores()

# print(resultados)