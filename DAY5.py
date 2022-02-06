def f(n):
    return n%3==0 and n%5==0

num_list = []

a = int(input("Enter number of elements : ")) 

for i in range(0, a):
    ele = int(input())
 
    num_list.append(ele)

result = list(filter((f), num_list))

print("Numbers divisible by 3 and 5 are",result)