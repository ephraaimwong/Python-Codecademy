import gensim
from nltk.corpus import stopwords
from romeo_juliet import romeo_and_juliet

# load stop words
stop_words = stopwords.words('english')

# preprocess text
romeo_and_juliet_processed = [[word for word in romeo_and_juliet.lower().split() if word not in stop_words]]

# view inner list of romeo_and_juliet_processed
print(romeo_and_juliet_processed[0][:20])

# train word embeddings model
model = gensim.models.Word2Vec(romeo_and_juliet_processed, size = 100, window = 5, min_count = 1, workers = 2, sg = 1)

# view the entire vocabulary used to train the word embedding model HOWEVER if this step is skipped, the model will pick up on the unique ways in which words of the text are used across a corpus
vocabulary = [i for i in model.wv.vocab.items()]
print(vocabulary)

# similar to romeo
similar_to_romeo = model.most_similar("romeo", topn = 20)
print(similar_to_romeo)
# one is not like the others
not_star_crossed_lover = model.doesnt_match(["romeo", "juliet", "mercutio"])
print(not_star_crossed_lover)