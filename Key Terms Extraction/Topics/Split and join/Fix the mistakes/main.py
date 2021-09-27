text = input()
words = text.split()
for word in words:
    # finish the code here
    if word.startswith("www.") and word != "www.":
        print(word)
    if word.startswith("WWW.") and word != "WWW":
        print(word)    
    if word.startswith(r"http://"):
        print(word)
    if word.startswith(r"https://"):
        print(word)
