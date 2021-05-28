#1

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi_split = rainfall_mi.split(",")
num_rainy_months = 0
for x in rainfall_mi_split:
    x = float(x)
    if x > 3.0:
        num_rainy_months += 1

print(num_rainy_months)


#2

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

same_letter_count = sum(w[0] == w[-1] for w in sentence.split())
print(same_letter_count)

#3

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num = 0
for i in items:
    if 'w' in i:
        acc_num += 1

print(acc_num)

#4

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."

num_a_or_e = 0
for i in sentence.split():
    if ('a' in i) or ('e' in i):
        num_a_or_e += 1

print(num_a_or_e)

#5

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']

num_vowels = sum([1 for i in s if i in vowels])
print(num_vowels)