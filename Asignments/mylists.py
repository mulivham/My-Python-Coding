spam = ['apples', 'banana', 'tofu', 'cats']

def joints(mylist):
	s = ','
	print( s.join(mylist[:-1] + ['and ' + mylist[-1]]))

joints(spam)

"""

spam = ['apples', 'banana', 'tofu', 'cats']

def comma_(myList):

    s = ','  
    print( s.join(myList[: -1] + ['and ' + myList[-1]]))

comma_(spam)

"""


"""
list_of_words = ["apples","bananas", "tofu", "cats"]

def converter(lst):

   
    # return ", ".join(cat[:-1]) + " and " + cat[-1]    
    lst[-1] = 'and ' + str(lst[-1])
    res = ', '.join([(elem) for elem in lst])
    return res

print(converter(list_of_words))

"""