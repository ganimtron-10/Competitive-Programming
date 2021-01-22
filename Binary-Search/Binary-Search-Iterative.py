import math

arr = list(range(50))

def bsi(l,key):
	s = 0
	e = len(l)
	while s <= e:
		mid = math.floor((s+e)/2)
		# print(mid,s,e,key)
		if s == e and len(l)-1 < s:
			return -1
		elif key == l[mid]:
			return mid
		elif key < l[mid]:
			e = mid - 1
		elif key > l[mid]:
			s = mid + 1

print(bsi(arr,50))