import  json


# def greet_user():
#     filename = "username.json"
#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("can't load your info, plz tell me your name:\n")
#         with open(filename,'w') as f:
#             json.dump(username,f)
#             print("....we will remember you....")
#     else:
#         print("Welcome back," + username)

def get_stored_username():
    ''' demo '''
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    '''say hi to our user'''
    username = get_stored_username()

    if username:
        print("Hi,",username)
    else:
        username= input("what is your name?")
        filename = "username.json"
        with open(filename,'w') as f:
            json.dump(username,f)
            print("we will remember you when you come back,",username.title())

greet_user()
