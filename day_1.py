input = [int(x) for x in open("input_1.txt").readlines()]

num1=0
num2=0

for i in input:
    for j in input:
        if i+j==2020:
            num1=i
            num2=j
            break

print("Num1: ",num1)
print("Num2: ",num2)
print("Sum: ", num1 + num2)

print(num1*num2)