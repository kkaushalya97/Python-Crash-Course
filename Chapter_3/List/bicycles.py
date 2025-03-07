# List is a collection of items in a particular order.

bicycles =['trek','cannodale','redline','specialized']
print(bicycles)

# Access element in a list
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3].title())

# access last item in a list
print(bicycles[-1].title())

# print a message using individual elemnet in a list
message = f"My first bycycle was a {bicycles[0].title()}"
print(message)
