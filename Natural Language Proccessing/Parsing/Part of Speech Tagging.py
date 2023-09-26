import nltk
from nltk import pos_tag #pos_tag() identifies if tokenized word is(noun, pronoun, verb, adverb, adjective, preposition, conjunction or interjection)
from word_tokenized_oz import word_tokenized_oz
# start of pos_tag code
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
# end of pos_tag code


witches_fate = word_tokenized_oz[100]
print(witches_fate)

pos_tagged_oz = list()

for word_tokenized_sentence in word_tokenized_oz:
  pos_tagged_oz.append(pos_tag(word_tokenized_sentence))

witches_fate_pos = pos_tagged_oz[100]
print(witches_fate_pos)