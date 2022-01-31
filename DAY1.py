x = input('Enter the values : ').split()
c=0

val = []

for i in x:
    val.append(int(i))
    
for j in val:
    c=c+j

print('sum =',c)