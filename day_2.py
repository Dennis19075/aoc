import numpy as np

input = [(x) for x in open("input_2.txt").readlines()]
# input = ["11-13 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
cont=0
res = 0
limits=[]
passwd=[]
for a in input:
    value = a.replace("-", " ")
# print(input)
    limits.append([int(i) for i in value.split() if i.isdigit()])
    for j in range(len(a)):
        if a[j]==" ":
            passwd.append(a.split())
            print("ROTO: ", a.split())
            break

res=0
for i in range(len(passwd)):
    cont=0
    for j in range(len(passwd[i][2])):
        # print("Cada letra: ",passwd[i][2][j])
        # print("Tipo de cada letra: ",type(passwd[i][2][j]))
        # print("La letra: ",passwd[i][1][0])
        # print("Tipo de la letra: ",type(passwd[i][1][0]))
        if passwd[i][1][0]==passwd[i][2][j]: #compare letter and each letter in the passwd
            cont=cont+1

    # print("Cont: ", cont)
    if cont >= limits[i][0] and cont <=limits[i][1]:
        res = res+1
# print(input)
# print("Limites: ",limits)
print(res)
# print("Largo INPUT ",len(passwd))

    

# for a in input:
#     letter=passwd[]
#     passwd=a[8:len(a)]
#     cont=0
#     print(a)
#     print(min)
#     print(max)
#     print(letter)
#     print(passwd)
#     for i in passwd:
#         if i==letter:
#             cont=cont+1
#     print(cont)
#     if cont>=min and cont<=max:
#         print(True)
#     else:
#         print(False)

# print(res)