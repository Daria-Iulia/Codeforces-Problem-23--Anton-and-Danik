n=int(input())
s=str(input())
counta=0
countd=0
for i in s:
    if i=='A':
        counta+=1
    elif i== 'D':
        countd+=1


if counta>countd:
    print("Anton")
elif countd>counta:
    print("Danik")
else:
    print("Friendship")

