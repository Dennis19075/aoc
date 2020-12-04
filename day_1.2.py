input = [int(x) for x in open("input_1.txt").readlines()]

num1=0
num2=0
num3=0

for i in input:
    for j in input:
        for k in input:
            if i+j+k==2020:
                num1=i
                num2=j
                num3=k
                break

print("Num1: ",num1)
print("Num2: ",num2)
print("Num3: ",num3)
print("Sum: ", num1 + num2 + num3)

print(num1*num2*num3)