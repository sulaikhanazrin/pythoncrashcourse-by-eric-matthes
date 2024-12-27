usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}. Do you want look at the today report? ')
        else:
            print(f'Thank you {username.title()} for you logged')
            
else:
    print('We need any user!')            