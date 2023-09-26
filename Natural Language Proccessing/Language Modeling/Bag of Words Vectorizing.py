from preprocessing import preprocess_text
#refer to bag of word dictionary for preprocessing code

def create_features_dictionary(documents):
    features_dictionary = {}
    merged = " ".join(documents)
    tokens = preprocess_text(merged)
    index = 0
    for i in tokens:
        if i not in features_dictionary:
            features_dictionary[i] = index
            index += 1
    return features_dictionary, tokens

training_documents = ["Five fantastic fish flew off to find faraway functions.", "Maybe find another five fantastic fish?", "Find my fish with a function please!"]

create_features_dictionary(training_documents)
#features_dictionary = {'function': 8, 'please': 14, 'find': 6, 'five': 0, 'with': 12, 'fantastic': 1, 'my': 11, 'another': 10, 'a': 13, 'maybe': 9, 'to': 5, 'off': 4, 'faraway': 7, 'fish': 2, 'fly': 3}

def text_to_bow_vector(some_text, features_dictionary):
#some_text will be vectorized according to the features_dictionary index values
    bow_vector = [0] * len(features_dictionary)
    #creates a zeroized list of features for some_text to be parsed 
    tokens = preprocess_text(some_text)
    for i in tokens:
        if i in features_dictionary:
            feature_index = features_dictionary[i]
            #feature_index gets index of said feature so that bow_vector can access and add count to the appropriate index.
            bow_vector[feature_index] += 1
    return bow_vector, tokens

text = "Another five fish find another faraway fish."
print(text_to_bow_vector(text, features_dictionary)[0])