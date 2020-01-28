from Password import Credential,UsersData

import random
import string
import time
import pyperclip
def main():
        print("Hello welcome to your user list.what is your name?")
user_name=input()
print (f"Hello{user_name}.What would you like to do?")
print("/n")
while True:
        print ("use these short codes:cu-create new user name,du-display user name,fu-find user.ex-exit the user list")
        short_code=input().lower()
        if short_code=='cu':
         print("New User")
         print("_"*10)
         print("identity...")
         identity=input()

        print("username")
        user_name=input()

        print("password")
        password=input()
save_users(create_users(identity,user_name,password))

        print('/n')
        print(f"New User{identity}{user_name} created")
        print('/n')

                     # elif short_code=='du':
        print("Here is a list of all users")
        print('/n')

for password in display ():

       print(f"{credential.identity} {credential.user_name}{credentila.password})
       print('/n')
               else:
       print('/n')

       print("You dont have a user name")
       print('/n')

                elif: short code =='fu':
      print ("Enter the user name")
search_user=input()
if check_existing_user(serch_user)


     print(f"{search_user.user_name}")
     print('_'*8)
     print(f"password.....{search_users.password}")
     print(f"identity....{search_user.identity}")
else;
    print("The user does not exist")
elif "ex" == short_code:
    print("Bye .......")
break
 else:
print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()











#
# def create_user(identity,user_name, password):
#     '''
#     function that creates new credentials
#     '''
#     new_user = Credential(identity,user_name,password)
#     return new_user
#
# def save_user(credential):
#     '''
#     function that saves credentials
#     '''
#     credential.save_user()




# def check_existing_cred(user_name):
#     '''
#     function to test if credentials exist
#     '''
#     return Credential.creds_exist(uname)







































































def main():
    print("Hello Welcome to your contact list. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : cc - create a new account, dc - display password, fc -find a account, ex -exit the account list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_password(create_account(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_account():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")