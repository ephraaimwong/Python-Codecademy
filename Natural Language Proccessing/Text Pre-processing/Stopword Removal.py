from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english")) #will eliminate all english "filler" words which do not provide info about the statement

survey_text = 'A YouGov study found that American\'s like Italian food more than any other country\'s cuisine.'

tokenized_survey = word_tokenize(survey_text)

text_no_stops = [i for i in tokenized_survey if i not in stop_words] #if i in stop_words, it will not append to list

try:
  print(f'Stopwords type: {type(stop_words)}')
except:
  print('Expected a variable called `stop_words`')
try:
  print(f'Words Tokenized: {tokenized_survey}')
except:
  print('Expected a variable called `tokenized_survey`')
try:
  print(f'Text without Stops: {text_no_stops}')
except:
  print('Expected a variable called `text_no_stops`')
  