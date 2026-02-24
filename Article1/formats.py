# program test all printing formats in python

num1 = 12
num2 = 10

message = "hello"

#f-string methods
print(f"{message} solution no {num1 + num2}")

#format() method
print("{} solution no {} ".format(message , num2+num1))

# %formatting
print("%s solution no %d" % (message , num1+num2))




