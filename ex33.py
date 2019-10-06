

"""numbers=[]
def tryone(i,j):
    while i>j:
        print(f"At the top i is {j}")
        numbers.append(j)

        j=j+1
        print("Numbers now:",numbers)
        print(f"At the bottom i is {j}")
tryone(6,0)
print(numbers)
for num in numbers:
     print(num)"""






numbers=[]
def trytwo(j):
    for j in range(0,6):
        print(f"At the top i is {j}")
        numbers.append(j)

        #j=j+1
        print("Numbers now:",numbers)
        print(f"At the bottom i is {j}")
trytwo(0)
print(numbers)
for num in numbers:
     print(num)
