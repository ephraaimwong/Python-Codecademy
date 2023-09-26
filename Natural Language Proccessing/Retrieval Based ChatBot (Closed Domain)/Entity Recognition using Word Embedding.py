import spacy
word2vec = spacy.load('en')

message_nouns = ['shirts', 'weekend', 'package']

tokens = word2vec(" ".join(message_nouns))
# or
# tokens = [word2vec(i) for i in message_nouns]
category = word2vec("clothes")


def compute_similarity(tokens, category):
  #computes similarity between token and category using the word2vec cosine distance
  output_list = list()
  for token in tokens:
    #token.similarity(category) outputs the cosine distance, higher is more similar
    output_list.append(f"{token.text} {category.text} {token.similarity(category)}")
  return output_list

print(compute_similarity(tokens, category))

blank_spot = message_nouns[0]
bot_response = f"Hey! I just checked my records, your shipment containing {blank_spot} is en route. Expect it within the next two days!"
print(bot_response)