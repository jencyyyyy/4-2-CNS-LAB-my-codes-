import random

def lehmann(n, t):
	a = random.randint(2, n-1)
	print("a = ",a)

	e =(n-1)/2
	while(t>0):
		result =((int)(a**e))% n
		print("result = ",result)
		if((result == 1) or (result ==(n-1))):
			a = random.randint(2, n-1)
			print("Inside: a = ",a)
			t-= 1
		else:
			return -1
	return 1

n = int(input("Enter integer to test primality: "))
#n = 97

t = 10 

if(n ==1 or n == 2 ):
	print(n," is Prime.")
elif(n % 2 == 0):
	print(n, "is Composite")
else:
	flag = lehmann(n, t)

	if(flag == 1):
		print(n, "may be Prime.")

	else:
		print(n, "is Composite.")
