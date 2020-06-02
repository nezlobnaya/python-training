
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

print(bool("abc"))
print(bool(123))
print(bool(''))
print(bool([]))
x = 0
print(bool(x))

x = 200
print(isinstance(x, int)) 

def print_lyrics():
    print("Vasyy is singing")
print_lyrics()

def print_lyrics():
    print("Oh yeah, I'll tell you something")
    print("I think you'll understand")
    print("Then I'll say that something")
    print("I wanna hold your hand")
print_lyrics()

def do_twice(f, a):
    """
    Takes a function and executes it twice.
    """
    f(a)
  
   
def do_four(f, v):
    f(v)
    f(v)
 

def print_spam(string):
    print(string)
    print(string)


do_twice(print_spam, "spam")
do_four(print_spam, 'petro')

def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n :
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def check_numbers():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    n = int(input("Choose a number for n: "))
    return check_fermat(a,b,c,n)

check_numbers()
