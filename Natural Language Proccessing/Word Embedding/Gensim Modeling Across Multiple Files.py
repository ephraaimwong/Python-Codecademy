import os
import gensim
import spacy
from president_helper import read_file, process_speeches, merge_speeches, get_president_sentences, get_presidents_sentences, most_frequent_words
# start of president_helper code
import os
from nltk.tokenize import PunktSentenceTokenizer
from collections import Counter
def read_file(file_name):
  with open(file_name, 'r+', encoding='utf-8') as file:
    file_text = file.read()
  return file_text
def process_speeches(speeches):
  word_tokenized_speeches = list()
  for speech in speeches:
    sentence_tokenizer = PunktSentenceTokenizer()
    sentence_tokenized_speech = sentence_tokenizer.tokenize(speech)
    word_tokenized_sentences = list()
    for sentence in sentence_tokenized_speech:
      word_tokenized_sentence = [word.lower().strip('.').strip('?').strip('!') for word in sentence.replace(",","").replace("-"," ").replace(":","").split()]
      word_tokenized_sentences.append(word_tokenized_sentence)
    word_tokenized_speeches.append(word_tokenized_sentences)
  return word_tokenized_speeches
def merge_speeches(speeches):
  all_sentences = list()
  for speech in speeches:
    for sentence in speech:
      all_sentences.append(sentence)
  return all_sentences
def get_president_sentences(president):
  files = sorted([file for file in os.listdir() if president.lower() in file.lower()])
  speeches = [read_file(file) for file in files]
  processed_speeches = process_speeches(speeches)
  all_sentences = merge_speeches(processed_speeches)
  return all_sentences
def get_presidents_sentences(presidents):
  all_sentences = list()
  for president in presidents:
    files = sorted([file for file in os.listdir() if president.lower() in file.lower()])
    speeches = [read_file(file) for file in files]
    processed_speeches = process_speeches(speeches)
    all_prez_sentences = merge_speeches(processed_speeches)
    all_sentences.extend(all_prez_sentences)
  return all_sentences
def most_frequent_words(list_of_sentences):
  all_words = [word for sentence in list_of_sentences for word in sentence]
  return Counter(all_words).most_common()
# end of president_helper code

# get list of all speech files
#creates a sorted list of all speech files that end in ".txt"
files = sorted([file for file in os.listdir() if file[-4:] == ".txt"])
print(files)

# read each speech file
#create a list containing each speech in files
speeches = [read_file(i) for i in files]


# preprocess each speech
processed_speeches = process_speeches(speeches)
#print(processed_speeches)

# merge speeches
all_sentences = merge_speeches(processed_speeches)
#print(all_sentences)

# view most frequently used words
most_freq_words = most_frequent_words(all_sentences)
#print(most_freq_words)

# create gensim model of all speeches
all_prez_embeddings = gensim.models.Word2Vec(all_sentences, size=96, window=5, min_count=1, workers=2, sg=1)

# view words similar to freedom
similar_to_freedom = all_prez_embeddings.most_similar("freedom", topn=20)
similar_to_success = all_prez_embeddings.most_similar("success", topn=20)
#print(similar_to_freedom, similar_to_success)

# get President Roosevelt sentences
roosevelt_sentences = get_president_sentences("franklin-d-roosevelt")

# view most frequently used words of Roosevelt
roosevelt_most_freq_words = most_frequent_words(roosevelt_sentences)
# print(roosevelt_most_freq_words)

# create gensim model for Roosevelt
roosevelt_embeddings = gensim.models.Word2Vec(roosevelt_sentences, size=96, window=5, min_count=1, workers=2, sg=1)

# view words similar to freedom for Roosevelt
roosevelt_similar_to_freedom = roosevelt_embeddings.most_similar("freedom", topn=20)
# print(roosevelt_similar_to_freedom)

# get sentences of multiple presidents
rushmore_prez_sentences = get_presidents_sentences(["washington","jefferson","lincoln","theodore-roosevelt"])

# view most frequently used words of presidents
rushmore_most_freq_words = most_frequent_words(rushmore_prez_sentences)
# print(rushmore_most_freq_words)

# create gensim model for the presidents
rushmore_embeddings = gensim.models.Word2Vec(rushmore_prez_sentences, size=96, window=5, min_count=1, workers=2, sg=1)

# view words similar to freedom for presidents
rushmore_similar_to_freedom = rushmore_embeddings.most_similar("freedom", topn=20)
print(rushmore_similar_to_freedom)