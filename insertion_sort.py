import random, datetime, time
list_size = 100
mess = []
for index in range(list_size):
	mess.append(random.randint(1,10000))
print "Original list: " + str(mess)
if_count = 0
start_time = time.clock()						
for new_item_index in range(1,len(mess)):
	insertion_index = new_item_index -1
	if_count += 1
	if mess[new_item_index] < mess[insertion_index]:
		insertion_index -= 1
		insert_found = False
		while insert_found == False:
			if_count += 1
			if mess[new_item_index]<mess[insertion_index]:
				insertion_index -= 1
				if_count += 1
				if insertion_index == -1:
					insert_found = True
			else:
				insert_found = True
		mess.insert(insertion_index+1, mess.pop(new_item_index))
end_time=  time.clock()
print "Sorted list: " +  str(mess)
print str(datetime.timedelta(start_time, end_time))
print str(if_count) + " if statements."