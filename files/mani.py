import pymongo
import datetime


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["my_db"]
my_collec = mydb["book_details"]


c=0
time = 0
for j in range(1996,2020):
	start = datetime.datetime.now() + datetime.timedelta(minutes=time)
	file_name = "GUTINDEX." + str(j) + ".txt"
	f = open(file_name,"r")
	list_dic = []
	print(str(j) + " file processing started at: " + str(start))
	for i in f:
		
		if "by" in i:
			# print(i)
			book = i.split(", by")
			# print(book)
			if "\xa0" in book[-1]:
				# print(book[-1])
				temp1 = book[-1].split("\xa0")
				book[-1] = temp1[0].strip()
			temp2 = book[-1].split("   ")
			book[-1] = temp2[0].strip()
			book[0] = book[0].strip()
			
			if "by" not in book[0]:
				c=c+1
				my_dic = {"p_key":c, "title":book[0], "author":book[-1], "start_time":str(start)} 
				list_dic.append(my_dic)
				# x = my_collec.insert_one(my_dic)
				# print(my_dic)
	#print(list_dic)
	end = datetime.datetime.now() 
	for k in list_dic:
		k["end_time"] = str(end)
		x = my_collec.insert_one(k)
	print(str(j) + " file processing ends at: " + str(end))
	print("")
	print("")
	f.close()

	# 39 + datetime.timedelta(minutes=time)
	# 44 time = time + 5