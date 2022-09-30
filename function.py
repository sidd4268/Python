# Python3 code to demonstrate working of
# Specific Characters Frequency in String List
# Using join() + Counter()
from collections import Counter

# initializing lists
test_list = ["Mississippi"]

# printing original list
print("The original list : " + str(test_list))

# char list
chr_list = ['M', 'i', 's', 'p']

# dict comprehension to retrieve on certain Frequencies
res = {key: val for key, val in dict(Counter("".join(test_list))).items() if key in chr_list}

# printing result
print("Specific Characters Frequencies : " + str(res))