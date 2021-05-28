#1

my_str = "MICHIGAN"
for i in my_str:
    print(i)

#2
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
for several_things in str_list:
    print(len(several_things))

#3
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
element = 0

for i in str_list:
    print(len(str_list[element]))
    element += 1

#4
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0

for i in original_str:
    num_chars = num_chars + 1
    print(num_chars)

#5
addition_str = "2+5+10+20"
x = addition_str.split('+')

sum_val = 0
for i in x:
    sum_val = sum_val + int(i)
print(sum_val)


#6
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"

avg_temp = 0.0

for i in week_temps_f:
    avg_temp = sum(map(float,week_temps_f.split(","))) / 7
    print(avg_temp)


#7
nums = list(range(0, 68))
print(nums)


#8

original_str = "The quick brown rhino jumped over the extremely lazy fox"
new_str = original_str.split()
num_words_list = [0, ] * len(new_str)
print(num_words_list)
n = 0
for n in range(len(num_words_list)):
    num_words_list[n] = len(new_str[n])
    print(num_words_list)
sum = 0
for i in num_words_list:
        sum = sum + i
print(sum)

#9

lett = ""
str = "b"
for _ in range(7):
    lett = lett + "b"
print (lett)

#10

import turtle

star = turtle.Turtle()

for i in range(50):
    star.forward(50)
    star.right(144)

turtle.done()