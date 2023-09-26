import codecademylib3_seaborn
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from term_frequency import bow_matrix, feature_names, df_bag_of_words, corpus_index
#start of term_frequency code which vectorizes text
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from preprocessing import preprocess_text
from poems import poems
# preprocess text
processed_poems = [preprocess_text(poem) for poem in poems]
# initialize and fit CountVectorizer
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(processed_poems)
# get vocabulary of terms
feature_names = vectorizer.get_feature_names()
# get corpus index
corpus_index = [f"Poem {i+1}" for i in range(len(poems))]
# create pandas DataFrame with term frequencies
df_bag_of_words = pd.DataFrame(bow_matrix.T.todense(), index=feature_names, columns=corpus_index)
#end of term_frequency code

# display term-document matrix of term frequencies (bag-of-words)
print(df_bag_of_words)

# initialize and fit TfidfTransformer, transform bag-of-words matrix into tfidf scores
transformer = TfidfTransformer(norm = None)
tfidf_scores = transformer.fit_transform(bow_matrix)


# create pandas DataFrame with tf-idf scores
try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index = feature_names, columns=corpus_index)
  print(df_tf_idf)
except:
  pass