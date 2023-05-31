# 100 people stand in a circle.
# Number 1 has a sword.
# He kills the next person (i.e. Number 2) and gives the sword to the next living person (i.e. Number 3).
# Everyone does the same until only 1 survives.
# Who survives?
# What if the circle was 150 people, or 273 people?


# user_number = int(input("enter a number:\t"))                         # ask user for a number
# mylist = list(range(1,user_number+1))                                 # use that number to make the list


# my list is every number from 1 to 273
mylist = list(range(1, 273 + 1))

# while there's more than 1 person left
while len(mylist) > 1:
    # the person is the first person in my list
    person = mylist[0]
    # delete the person and the next person along
    del mylist[0:2]
    # append person to the end of the list
    mylist.append(person)

print(mylist)
