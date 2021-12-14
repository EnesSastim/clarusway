word = input("Enter a word: ")
word = word.lower()
mydict = {}

for i in word:
    if not i in mydict.keys():
        mydict.update({i:word.count(i)})

print(mydict)
