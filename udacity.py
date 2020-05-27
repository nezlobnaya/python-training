a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

#print(max([len(a), len(b), len(c)]))
#print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
#print(" & ".join(sorted(names)))
#print(names[-1])
#print(names[len(names)-1])

#arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#print(arr[4:])


#print(list(range(0,-5)))
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)
