
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

# def check_fermat(a,b,c,n):
#     if n > 2 and a**n + b**n == c**n :
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn't work.")

# def check_numbers():
#     a = int(input("Choose a number for a: "))
#     b = int(input("Choose a number for b: "))
#     c = int(input("Choose a number for c: "))
#     n = int(input("Choose a number for n: "))
#     return check_fermat(a,b,c,n)

# check_numbers()

sample_tuple = tuple('Vladislav')
print(sample_tuple)
dir(sample_tuple)

name = "Vlad"
print(f"Hello {name}")
print("Hello {}".format(name))

p = [10, 20, 60, 5, "Banana"]
for (i, el) in enumerate(p):
    print(f"Element at {i} is {p[i]} == {el}")

numbers = [1, 3, 5, 6, 7]
cooler_squares = [num**2 for num in numbers]
print(cooler_squares)