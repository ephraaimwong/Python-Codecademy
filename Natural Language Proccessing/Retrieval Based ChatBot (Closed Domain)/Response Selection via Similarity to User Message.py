from user_functions import preprocess, compare_overlap, pos_tag, extract_nouns, word2vec, compute_similarity
from collections import Counter
# start of user_functions code
import re
from collections import Counter
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
import spacy
word2vec = spacy.load('en')

def preprocess(input_sentence):
    input_sentence = input_sentence.lower()
    input_sentence = re.sub(r'[^\w\s]','',input_sentence)
    tokens = word_tokenize(input_sentence)
    input_sentence = [i for i in tokens if not i in stop_words]
    return(input_sentence)

def compare_overlap(user_message, possible_response):
    similar_words = 0
    for token in user_message:
        if token in possible_response:
              similar_words += 1
    return similar_words
  
def extract_nouns(tagged_message):
    message_nouns = list()
    for token in tagged_message:
        if token[1].startswith("N"):
            message_nouns.append(token[0])
    return message_nouns

def compute_similarity(tokens, category):
    output_list = list()
    for token in tokens:
        output_list.append([token.text, category.text, token.similarity(category)])
    return output_list
# end of user_functions code

user_message = "Good morning... will it rain in Chicago later this week?"

blank_spot = "illinois city"
response_a = "The average temperature this weekend in {} with be 88 degrees. Bring your sunglasses!"
response_b = "Forget about your umbrella; there is no rain forecasted in {} this weekend."
response_c = "This weekend, a warm front from the southeast will keep skies near {} clear."
responses= [response_a, response_b, response_c]

#preprocess documents
bow_user_message = Counter(preprocess(user_message))
# for loop is used since responses is a list
processed_responses = [Counter(preprocess(response)) for response in responses] 

#determine intent with BoW(similarity in words), another option is intent with Tfidf where cosine distance is used instead
similarity_list = [compare_overlap(doc, bow_user_message) for doc in processed_responses]
# prints [0,1,0] since there is a overlapping word of "rain" between user_message and response_b
# selecting best response based on similarity
response_index = similarity_list.index(max(similarity_list))
print(response_index)
# or

#extract entities with word2vec 
tagged_user_message = pos_tag(preprocess(user_message))
message_nouns = extract_nouns(tagged_user_message)

#execute word2vec below
tokens = word2vec(" ".join(message_nouns))
category = word2vec(blank_spot)
word2vec_result = compute_similarity(tokens, category)
print(word2vec_result)
entity = word2vec_result[2][0]
print(entity)

#select final response below
final_response = responses[response_index].format(entity)
print(final_response)


