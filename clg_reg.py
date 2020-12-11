from os import path

import csv

class college:
	
	def __init__(self,collegeid,collegename,coursetype,city,fees,pincode):
		
		self.collegeid = collegeid
		self.collegename = collegename
		self.coursetype = coursetype
		self.city = city
		self.fees = fees
		self.pincode = pincode

	def add(self):
		var = [self.collegeid,self.collegename,self.coursetype,self.city,self.fees, self.pincode]

		clgli = []
		flag = 0
		with open("colleges.csv","r") as efile:
			csv_reader = csv.reader(efile)
			for line in csv_reader:
				if line[0] == self.collegeid:
					print("College-id already Exists")
					flag = 1
					efile.close()
					break
				else:
					continue
		if flag ==0:
			for i in var:
				clgli.append(i)
			with open("colleges.csv","a+",newline='') as handle:
				writer = csv.writer(handle)
				writer.writerow(clgli)
				handle.close()

def search():
	with open("colleges.csv","r") as fhandle:
		csv_reader = csv.reader(fhandle)
		print(",".join(["college-id","college-name","course-type","city","fees","pincode"]))
		for line in csv_reader:
			if line[3] == city_name:
				print(",".join(line))

def delete():
	delflag = 0
	try:
		with open("colleges.csv","r") as del_file:
			sample = []
			csvdel = csv.reader(del_file)
			for line in csvdel:
				if line[0] != clgid or line[0] == "collegeid":
					sample.append(line)
		
		del_file.close()
	
	except FileNotFoundError:
		print('''File colleges.csv not found,
please re-run the program and add college data and then try delete''')
		delflag = 1

	if delflag == 0:
		with open("colleges.csv","w", newline='') as new_file:
			writer_del = csv.writer(new_file)
			for data in sample:
				writer_del.writerow(data)
			new_file.close()
		print("college with college-id {} is removed".format(clgid))

def fields():
	li = ["collegeid","collegename","coursetype","city","fees","pincode"]
	with open("colleges.csv","a+",newline='') as tag_lines:
		writer = csv.writer(tag_lines)
		writer.writerow(li)
		tag_lines.close()

while True:

	print('''-------------------Welcome-----------------------
-------------------Enter the following-----------
		1-To add college details
		2-To Show the College details based on city
		3-To delete college details''')

	choice = int(input("Enter your Choice:--> "))

	if choice==1:
		
		if path.exists("colleges.csv"):
			pass
		else:
			fields()
		
		while True:
			collegeid = input("Enter the college id:--> ")
			collegename = input("Enter the college name:--> ")
			coursetype = input("Enter the course type:--> ")
			city = input("Enter the city name:--> ")
			fees = input("Enter the fees:--> ")
			pincode = input("Enter the pincode:--> ")

			clgobj = college(collegeid, collegename, coursetype, city, fees, pincode)
			clgobj.add()

			con = (input("Enter 0 to add new college data:--> "))

			if con != "0":
				break

	if choice == 2:
		
		try:
			city_name = input("Enter the city name:--> ")
			search()
		except FileNotFoundError:
			print('''File colleges.csv not found,
	please re-run the program and add college data and then search''')

	if choice == 3:
		clgid = input("Enter the college id which is to be deleted from the colleges.csv file:--> ")
		delete()

	shut = input("Enter 0 to continue process or press anything else to exit program:--> ")

	if shut != "0":
		break