current_usernames = ['kasuni','James','sawani','charlie','geogina']
new_usernames = ['serena','samara','kasuni','JAMES','charlie']

for new_uname in new_usernames:
    if new_uname in current_usernames:
        print(f"Please enter a new username.{new_uname} is currently in use.")
    else:
        print(f'usernamne: {new_uname} is available.')

 
print("\n")

#make a copy of current user names with all lowercase.
current_usernames_lower = [user.lower() for user in current_usernames]

for new_uname in new_usernames:
    if new_uname.lower() in current_usernames_lower:
        print(f"Please enter a new username.{new_uname} is currently in use.")
    else:
        print(f'usernamne: {new_uname} is available.')