# fruits = ["apple","banana","pineapple","mango","orange"]
# fruits2 = [i.upper() for i in fruits ]
# print(fruits2)

# num = [i for i in range (1,11) if i%2 ==0]
# print(num)  

#double the cubes of all even  numbers from 1 to 10
# l= [2 * x**3 for x in range (2,11,2)]
# print(l)

#create a list of the first letters of the alphabet capitalized:
# l=[letter.upper() for letter in "abcdefghijklmnopqrstu"]
# print(l)

words = [word for word in ["short", "medium", "long", "reallylong"] if len(word) > 5]
print(words)

