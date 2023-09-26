from collections import Counter
from preprocessing import preprocess #preprocess and tokenize text

user_message = preprocess("Hello! What is the fit of the 'Elosie' dress? My shoulders are broad, so I often size up for a comfortable fit. Do dress sizes run large or small? Especially in the shoulders?")
response_a = preprocess("All of our dresses sare cut from a polyester blend for a strechy fit")
response_b = preprocess("The 'Elosie' dress runs large. I suggest you take your regular size or smaller for the best fit.")

#printing the user_message variable below
print(user_message)

#using Counter() on proccessed text will create a BOW dict
bow_user_message = Counter(user_message)
bow_response_a = Counter(response_a)
bow_response_b = Counter(response_b)

def compare_overlap(user_message, possible_response):
  similar_words = 0
  #iterate over tokens in user_message for shared words
  for token in user_message:
    if token in possible_response:
      similar_words += 1
  return similar_words

print("Number of shared words between user_message and response_a: " + str(compare_overlap(bow_user_message, bow_response_a))) #prints 1 overlap word

print("Number of shared words between user_message and response_b: " + str(compare_overlap(bow_user_message, bow_response_b))) #prints 5 overlap words



