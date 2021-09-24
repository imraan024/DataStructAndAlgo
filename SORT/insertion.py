def insertion(list):
	for i in range(1,len(list)):
		v = list[i]
		j = i-1
		while j>=0 and v < list[j]:
			list[j+1] = list[j]
			j-=1
		list[j+1] = v

list = [8,2,5,4,9,7]
insertion(list)
print(list)	