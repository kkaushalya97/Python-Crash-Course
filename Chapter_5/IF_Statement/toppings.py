#checking for Inequality
requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies")
    
#if statement in the list
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print(f"\nadded {requested_topping}")

print("\nFinished making your pizza!.")

#Checking the list is  not empty.
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"\nadded {requested_topping}")
    print("\nFinished making your pizza!.")
    
else:
    print("ARe you sure you want a plain pizza?.")
    
#using multiple lists
available_toppings = ["mushrooms","olives","green pepers","pepperoni",
                      "pineapple","extra cheese"]

requested_toppings = ["mushrooms","french fries","extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"\nAdded {requested_topping}")
    else:
        print(f"Sorry we do not have {requested_topping}")
print("\n finished making your pizza!.")

    
