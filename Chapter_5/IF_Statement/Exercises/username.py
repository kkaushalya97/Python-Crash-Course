# usernames = ['admin','kasuni','james','sawani','charlie']
usernames = []

if usernames:
    for uname in usernames:
        if uname == 'admin':
            print(f"Hello {uname.title()} would you like to see status report!.")
        else:
            print(f"Hello {uname.title()} thank you for logging it again!.")
else:
    print("We need to find some users!.")