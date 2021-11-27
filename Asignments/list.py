spam = ["apple", "banana", "tofu", "cats"]

def my_function(items):

	print(','.join(items[:-1] + [ "and " + items[-1]]))

my_function(spam)
