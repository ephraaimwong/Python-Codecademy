import codecademylib3_seaborn
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from preprocessing import preprocess_text
from term_frequency import term_frequencies, feature_names, df_term_frequencies
# start of preprocessing
import nltk, re
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
stop_words = stopwords.words('english')
normalizer = WordNetLemmatizer()
def get_part_of_speech(word):
  probable_part_of_speech = wordnet.synsets(word)
  pos_counts = Counter()
  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech
def preprocess_text(text):
  cleaned = re.sub(r'\W+', ' ', text).lower()
  tokenized = word_tokenize(cleaned)
  normalized = " ".join([normalizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized])
  return normalized
# end of preprocessing
#start of term frequency
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import preprocess_text
from poems import poems
# preprocess text
processed_poems = [preprocess_text(poem) for poem in poems]
# initialize and fit CountVectorizer
vectorizer = CountVectorizer()
term_frequencies = vectorizer.fit_transform(processed_poems)
# get vocabulary of terms
feature_names = vectorizer.get_feature_names()
# get corpus index
corpus_index = [f"Poem {i+1}" for i in range(len(poems))]
# create pandas DataFrame with term frequencies
df_term_frequencies = pd.DataFrame(term_frequencies.T.todense(), index=feature_names, columns=corpus_index)
# end of term frequency

poem = '''
Success is counted sweetest
By those who ne'er succeed.
To comprehend a nectar
Requires sorest need.

Not one of all the purple host
Who took the flag to-day
Can tell the definition,
So clear, of victory,

As he, defeated, dying,
On whose forbidden ear
The distant strains of triumph
Break, agonized and clear!'''

# define clear_count:
clear_count = 0
for i in re.findall("clear", poem):
  clear_count += 1

# preprocess text
processed_poem = preprocess_text(poem)

# initialize and fit CountVectorizer
vectorizer = CountVectorizer()
term_frequencies = vectorizer.fit_transform([processed_poem])

# get vocabulary of terms
feature_names = vectorizer.get_feature_names()

# create pandas DataFrame with term frequencies
try:
  df_term_frequencies = pd.DataFrame(term_frequencies.T.todense(), index=feature_names, columns=['Term Frequency'])
  print(df_term_frequencies)
except:
  pass

#Tfidf penalizes terms with high frequency across corpus to reduce noise in text and find "keywords"/intent of user input

# initialize and fit TfidfTransformer
transformer = TfidfTransformer(norm=None)
transformer.fit(term_frequencies)
# the TfidfTransformer is fit (trained) on a term-document matrix of term frequencies
idf_values = transformer.idf_ 
#the .idf_ attribute of the TfidfTransformer stores the inverse document frequencies of the terms as a NumPy array

# create pandas DataFrame with inverse document frequencies
try:
  df_idf = pd.DataFrame(idf_values, index = feature_names, columns=['Inverse Document Frequency'])
  print(df_idf)
except:
  pass