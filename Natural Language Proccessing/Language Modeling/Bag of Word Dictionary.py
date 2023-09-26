from preprocessing import preprocess_text

#start of preprocessing code
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
  normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]
  return normalized
#end of preprocessing code

def text_to_bow(some_text):
    bow_dictionary = {}
    tokens = preprocess_text(some_text)
    for i in tokens:
        if i in bow_dictionary: #if lemmatized word is already in bow_dictionary, + 1 to count
            bow_dictionary[i] += 1
        elif i not in bow_dictionary: #if word not in dict, create key-value pair
            bow_dictionary[i] = 1
    return bow_dictionary

print(text_to_bow("I love fantastic flying fish. These flying fish are just ok, so maybe I will find another few fantastic fish..."))