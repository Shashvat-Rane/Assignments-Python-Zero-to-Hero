def fact(num): 
	if(num == 1): 
		return 1 
	s = num * fact(num-1) 
	return s;

n = int(input())
print(fact(n))