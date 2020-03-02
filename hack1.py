def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1
a = []
b = []
ind=[]
m=int(input("enter no of rows: "))
n=int(input("enter no of coloumns: "))
for i in range(n):
    a = []
    for j in range(m):
        a.append(input())
    b.append(a)
data=input("Enter item to search:")
c=find(b,data)
x=c[0]
y=c[1]
print(str(x)+" row")
print(str(y)+" coloum")
