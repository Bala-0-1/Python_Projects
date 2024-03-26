n = int(input("Enter the number of people:"))
lst1 = [ x for x in range(1,n+1)]
m = n
count = 0
while True:
	if m//2 != 0:
		m = m//2
		count+=1
	else:
		break
for i in range(1,count+1):
	lst1 = [x for x in lst1 if lst1.index(x)%2==0]
	x = lst1[len(lst1)-1]
	lst1.append(x)
print(lst1)
