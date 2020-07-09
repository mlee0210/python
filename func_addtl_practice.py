"""
Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as 4/3 πr^3
"""
import math

def vol(rad):
	return 4/3*math.pi*rad**3

#print(vol(2))

"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""

def ran_check(num,low,high):
	if low<=num<=high:
		print(f"{num} is in the range between {low} and {high}")
	else:
		print(f"{num} is not in the range between {low} and {high}")
	return None

#print(ran_check(5,2,7))

def ran_bool(num,low,high):
	return low<=num<=high

#print(ran_bool(5,2,7))

"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
"""

def up_low(lst):
	lower_count = 0
	upper_count = 0

	for word in lst:
		if word.isupper():

			upper_count+=1
		elif word.islower():
			lower_count+=1

	print(f'No. of Upper case characters: {upper_count}')
	print(f'No. of lower case characters: {lower_count}')

	return None

#print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""
def unique_list(lst):
	new_list=[]
	for x in lst:
		if len(new_list) == 0:
			new_list.append(x)
		else:
			for y in new_list:
				if x==y:
					break
			else:
				new_list.append(x)
	return new_list


#print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


"""
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
"""

def multiply(numbers):
	sum = 1
	for x in numbers:
		sum *= x
	return sum

#print(multiply([1,2,3,-4]))


"""
Write a Python function that checks whether a word or phrase is palindrome or not.
"""

def palindrome(s):
	s = s.replace(' ', '')

	return s == s[::-1]

#print(palindrome('nurses run'))


"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
"""

import string

def ispanagram(str1, alphabet=string.ascii_lowercase):
	sorted_str1 = sorted(str1.lower().replace(' ', ''))
	unique_str1 = ''.join(unique_list(sorted_str1))
	
	return unique_str1 == alphabet

print(ispanagram("The quick brown fox jumps over the lazy dog"))














