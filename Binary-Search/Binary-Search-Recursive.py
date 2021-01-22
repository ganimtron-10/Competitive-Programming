import math

arr = list(range(5))
print(arr)

def bsr(l,s,e,key):
	if s == e:
		if l[s] == key:
			return s
		else:
			return -1
	else:
		mid = math.floor((s+e)/2)
		print(mid,s,e,key)
		if key == l[mid]:
			return mid
		elif key < l[mid]:
			return bsr(l,s,mid-1,key)
		elif key > l[mid]:
			return bsr(l,mid+1,e,key)

print(bsr(arr,0,len(arr)-1,9))
