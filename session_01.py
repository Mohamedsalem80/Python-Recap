# comments #

# variables
#   Start with _ or alphabetics
#   contain numbers
varNone = None
varBool = True
varBool = False
varInt = 12345
varFloat = 1.235
varComp = 1 + 2j

# Composite
varStr = "String"
arr = [1, [1.2, 1.3, 1.4], 1+1j, "str"]
tup = (1, "2", [{1}])
sets = {1, 2, 3}
dict1 = {
    "name": "Mohamed",
    "age": 20,
    "activies": {
        "sports": ["basketball", "football"]
    }
}
print(dict1.values())

#integer division
a = 14
b = 3
# 14 - 3 = 11
# 11 - 3 = 8
# 8  - 3 = 5
# 5  - 3 = 2
# 2

print(a // b)

# Input
input1 = input("please enter values")

# Loops
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

# Functions

def add(num1, num2):
    return num1 + num2

print(add(1, 2))

def addm(*nums):
    sumt = 0
    for item in nums:
        sumt += item
    return sumt

print(addm(1, 2, 3))