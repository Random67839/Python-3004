# Demo 1
fruits = ["apple", "orange", "banana", "cherry"]
i = len(fruits) -1
while i >= 0:
    fruits.append(fruits[i])
    fruits.pop(i)
    print(fruits)
    i -= 1



# Demo 2
word = input("Syötä haluamasi sana!\n")
i = 1
while i < len(word):
    print(word[i])
    i += 2