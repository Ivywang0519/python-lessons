sum = 0
count = 0
for o in range(4, 10):
    sum = sum + o
    count = count + 1

print(sum / count)

if sum != 30 and count > 0:
    print(sum)
elif sum > 200:
    print(sum)
else:
    print("yxh is silly")

# condition >, <, >=, <=, !=, ==
if sum == 30:
    print(sum)

if sum <=40:
    print(sum)

while sum > 0:
    sum -= 1 # sum = sum - 1
    #print(sum, end="")
    if sum > 0:
        print(sum, end="| ")
    elif sum == 0:
        print(sum)

sum2 = 39
while sum2 > 0:
    sum2 -= 1
    print(sum2, end= "| " if sum2 > 0 else " ") # ternary operator

print()

def sum(a):
    sum3 = 0
    t = 3
    for i in a:
        sum3 += i
    return sum3 * t

def print_sum(a):
    print(sum(a))

print(sum([1, 2, 3, 4]))
print(sum([1, 2, 3, 4, 5]))
print_sum({1, 2, 3, 4, 5, 6})

def print_sum(a):
    sum4 = 0
    t = 3
    for i in a:
        sum4 += i
    print(sum4 * t)

print_sum({1, 2, 3, 4, 5, 6})

