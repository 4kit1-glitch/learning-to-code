#   Using the in operator

import re

name = 'harry'
user_message = f"hello {name}, how was your day"

result = re.search(name, user_message)

#it contains .string method to return the string that was searched
print(result.string)    #these ones dont take the () cause they are ot callable 

#it contains .group method to return what matched
print(result.group())

#return the index where the pattern starts and end
print(result.span())

#return none if the pattern doesnt match
result = re.search('war', user_message)
print(result)