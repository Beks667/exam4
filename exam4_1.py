def getKey(string):
	copy = False
	tmp = ""
	for char in string:
		if char == '\'' and copy == True:
			return tmp
		if copy:
			tmp += char
		if char == '\'' and copy == False:
			copy = True
		
		


arr = [1, 4.7, 'hi', False, None]
arr2 = [True, 2.3, None, "brook", 5]

res_dict = {}
for el in arr:
	typeofel = getKey(str(type(el)))
	res_dict[typeofel] = el

print(res_dict)