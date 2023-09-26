def reverse(text):
    text_reverse = ""
    for i in text:
        #will loop a, b+a, c+b+a, ... CANNOT text_reverse += i since that is text_reverse = text_reverse + i
        text_reverse = i + text_reverse
    return text_reverse

print(reverse("abcd"))