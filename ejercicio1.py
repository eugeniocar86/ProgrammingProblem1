def assing(arr):
	arr_out = []

	for a in arr:
		arr_out.append(a)

	return arr_out

def combine(n, arr, arr2):
	salida = []

	aux = arr

	for i in range(0, len(arr2)):
		#print(arr[i])
		d = []
		d= assing(arr)
		d.append(arr2[i])

		if sum(d) == n:
			salida.append(d)
		else:
			if sum(d) < n:
				return salida + combine(n, d, arr2)


	return salida

arr  = [3, 2, 1]
copy = assing(arr)

n = 5

arr_out = []

arr_aux = []

arr_salida_final = []
 
i = 0

for a in arr:
	for b in arr:
		arr_out.append([a,b])

for arr in arr_out:
	if sum(arr) == n:
		arr_salida_final.append(arr)
	else:
		arr_salida_final = arr_salida_final + combine(n, arr, copy)

print("OUTPUT")
print(arr_salida_final)





		

	










