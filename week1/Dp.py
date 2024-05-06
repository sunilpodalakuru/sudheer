R1=[]
R2=[]
sum=0
n=int(input("No of orders: "))
for i in range(n):
	x=int(input("Enter number: "))
	y=int(input("Enter number: "))
	R1.append(x)
	R2.append(y)
print("V1= ",R1)
print("V2= ",R2)
for i in range(len(R1)):
	sum+=R1[i]*R2[i]
print("Dot product: ", sum)
