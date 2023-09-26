from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() #cast words back to root form, requires additional function (part_of_speech tagging)to reconstruct sentences

def get_part_of_speech(word):
  import nltk
  from nltk.corpus import wordnet #wordnet is word databased used for contextualizing words
  from collections import Counter #counter is a container that stores elements as dict keys
  probable_part_of_speech = wordnet.synsets(word) #wordnet.synsets(i) gets synonyms for i from wordnet database
  
  pos_counts = Counter()

  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  ) #check if wordnet.synsets(word) is noun
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  ) #''verb
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  ) #''adjectives
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  ) #''adverbs
  
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0] #takes the category of the highest pos_counts and the most common in that category
  return most_likely_part_of_speech

populated_island = 'Indonesia was founded in 1945. It contains the most populated island in the world, Java, with over 140 million people.'

tokenized_string = word_tokenize(populated_island)
lemmatized_words = [lemmatizer.lemmatize(i, get_part_of_speech(i)) for i in tokenized_string]

try:
  print(f'A lemmatizer exists: {lemmatizer}')
except:
  print('Expected a variable called `lemmatizer`')
try:
  print(f'Words Tokenized: {tokenized_string}')
except:
  print('Expected a variable called `tokenized_string`')
try:
  print(f'Lemmatized Words: {lemmatized_words}')
except:
  print('Expected a variable called `lemmatized_words`')
  