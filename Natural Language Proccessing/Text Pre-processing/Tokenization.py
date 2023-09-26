from nltk.tokenize import word_tokenize, sent_tokenize

ecg_text = 'An electrocardiogram is used to record the electrical conduction through a person\'s heart. The readings can be used to diagnose cardiac arrhythmias.'

tokenized_by_word = word_tokenize(ecg_text)
tokenized_by_sentence = sent_tokenize(ecg_text)

try:
  print('Word Tokenization:')
  print(tokenized_by_word)
  #["An", "electrocardiogram", "is", "used", "to", "record"...]
except:
  print('Expected a variable called `tokenized_by_word`')
try:
  print('Sentence Tokenization:')
  print(tokenized_by_sentence)
  #["An electrocardiogram is used to record the electrical conduction through a person's heart", "The readings can be used to diagnose cardiac arrhythmias."]
except:
  print('Expected a variable called `tokenized_by_sentence`')