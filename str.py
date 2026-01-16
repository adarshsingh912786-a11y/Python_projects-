word = str(input("Enter your word: "))

vowels =  ["a","e","i","o","u"]
count = 0
for i in word:
    if (i in vowels):
        count += 1

print(f"Total words of vowels used is {count}")



