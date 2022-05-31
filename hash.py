# Python 3 code to demonstrate
# working of hash()

# initializing objects
# Python program showing
# a use of input()

int_val = input("Enter your value: ")
str_val = 'blockchain'
flt_val = 24.56

# Printing the hash values.
# Notice Integer value doesn't change
# You'l have answer later in article.
print("The integer hash value is : " + str(hash(int_val)))
print("The string hash value is : " + str(hash(str_val)))
print("The float hash value is : " + str(hash(flt_val)))
