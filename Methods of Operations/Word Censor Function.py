def censor(text, word):
    #text.split() splits the sentence into words
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            # words[count] is looping through via index, replacing censored word with stars
            words[count] = stars
        count += 1
    #" ".join(words) joins the words back into sentence with a space between words
    result =' '.join(words)
    return result