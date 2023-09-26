from nltk import pos_tag
user_message = ["i", "ordered", "two", "t-shirts", "this", "past", "weekend", "when","will", "my", "package", "be", "shipped"]

#pos_tag() will create tuples of each word with their form aka VB or NN
tagged_user_message = pos_tag(user_message)


def extract_nouns(tagged_message):
  message_nouns = list()
  
  for tup in tagged_message:
      #check if word is tagged as noun since entities are nouns
      if "NN" in tup[1]:
        #we only want to append the word, not the tag
        message_nouns.append(tup[0])
  return message_nouns

#define `user_message_nouns` here
user_message_nouns = extract_nouns(tagged_user_message)
print(user_message_nouns)