a = input('Enter the word: ')
f=[0]*26

for i in a:
    f[ord(i)-97] +=1

x = f.index(max(f))
print(chr(x + 97))
