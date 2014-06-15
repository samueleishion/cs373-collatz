import random 

def main(): 
	pred = [[1,10],
			[100,200], 
			[201,210], 
			[900,1000]] 

	lims = [[1,100],
			[500,1000], 
			[2500,9000],
			[500,50000], 
			[1,999999]] 

	for p in pred: 
		print(str(p[0])+" "+str(p[1])) 

	l = 0 
	d = 1000/len(lims) 

	for i in range(1000): 
		if(i>=(d*(l+1))): 
			l+=1 
		a = random.randint(lims[l][0],lims[l][1]) 
		b = random.randint(lims[l][0],lims[l][1])
		print(str(a)+" "+str(b)) 

	print("1 999999") 

main() 