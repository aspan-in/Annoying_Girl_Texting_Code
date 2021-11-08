import random
print("Texting Platform... Input Your Texts and get auto replies....")
print('')
while True:
    You=input("You:")
    rand=["nice","yeah","fine","i don't know what to say","hmm","you know what","let's talk tomorrow","I need some space","oh","huh?","I am fine","nothing","kuch nahi","idk","yeah maybe","yeah right","yup","no"]
    ch=random.randint(0,10)
    print("She:",rand[ch])
