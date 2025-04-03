string="Hello, World!"
print("\nThe given string is: ",string)

print("\nThe uppercase of the string is: ",string.upper())

print("\nThe lowercase of the string is: ",string.lower())

x=string.startswith("Hello")
print("\nString starts with 'Hello': ",x)

y=string.endswith("World!")
print("\nString ends with 'World!': ",y)

new_string=string.replace("World","Python")
print("\nThe new string is: ",new_string)

s=string.split(',')
print("\nThe splitting of the given string into words is: ",s)