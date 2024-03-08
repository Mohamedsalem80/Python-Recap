def add(num1, num2):
    return num1 + num2

print(add(1, 2))

def addm(*nums):
    sumt = 0
    for item in nums:
        sumt += item
    return sumt

print(addm(1, 2, 3))

print("*"*50)

for i in range(0, 21, 2):
    print(i, end="");

print()
print("*"*50)
k = 5

while k > 0:
    print(k)
    k -= 1

print("H"); print("R")