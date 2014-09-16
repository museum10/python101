'''
Created on 2014. 9. 16.

@author: dusskapark
'''
"""This is the "nester.py" module and  it provides one function called print_lol() which prints lists tha may or may not include nested lists."""


movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, 
                ["Graham Chapman", ["Michael Palin", "John Cleese",
                        "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


"""This function takes one positional argument called "a_list", which is any Python list (of-possibly-nested lists). 
	Each data item in the provided list is (recursively) printed to the screen on it's own line..."""


def print_lol(a_list):
    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
            

print_lol(movies)
