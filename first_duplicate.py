def find_duplicate(array):
	unique_array = []
	for element in array:
		if element in unique_array:
			print(element)
			break
		else:
			unique_array.append(element)

array = [1, 2, 3, 2, 1]

# l = eval(input("Enter length of array: "))
# array = []
# for i in range(l):
# 	val = input("Enter array element: ")
# 	array.append(val)


find_duplicate(array)