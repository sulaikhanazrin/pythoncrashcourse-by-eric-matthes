current_users = ['Carrol', "Rick", 'Morty', 'John', 'Amy']
new_users = ['Gary', "peter", 'morty', 'rick', 'Anna']

new_user_enter = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in new_user_enter:
        print(f"{new_user.title()} change your username")
    else:
        print(f"{new_user.title()} you can use this username")    