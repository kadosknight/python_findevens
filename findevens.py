def readfile(file):
	with open(file,"r",encoding="utf-8") as open_file:
		lines = open_file.readlines()
		output_helper = list()
		for line in lines:
			elements = line.strip().split(",")
			for i, value in enumerate(elements):
				if value == "":
					del elements[i]
				else:
					if value.isdigit() == True:
						output_helper.append(elements[i])
	return output_helper

def check_evens(data):
	string = ''
	for element in data:
		if int(element) % 2 == 0:
			string += str(element) + ' even - '
		else:
			string += str(element) + ' odd - '

	return string

default_list = list()
default_list = readfile("file.csv")
forced_list = [1,4,10,12,15]
choice = input("From file or forced? 1) 2)")
 
if choice == "1":
	print(check_evens(default_list))
elif choice == "2":
	print(check_evens(forced_list))
else:
	print("No input selected")