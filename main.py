import random
past = list(range(0,45))
#44,34,26,37
past.remove(44)
past.remove(34)
past.remove(26)
past.remove(37)
list_after = random.sample(past,41)
list_after = [44,34,26,37]+list_after
list_r = list()
for index,i in enumerate(list_after):
    if index % 6 ==0:
        string = ""
        for j in list_r:
            string = string + f"{j:02d} "
        print(string)
        list_r = list()
    if index < 42:
        list_r.append(i)
    else:
        break
string = f"      {list_after[42]:02d} {list_after[43]:02d} {list_after[44]:02d}   "
print(string)        
