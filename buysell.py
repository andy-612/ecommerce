#first we have a list of users where each useer is a dictionary
users = [{"name":"Andy","selling":["nike8","Addidas9"]}]
#now let's make a function to add a user
def signup():
    user = {"name":"","selling":[]}
    user["name"] = input("What is your name?")
    user["selling"].append(input("What are you selling?"))
    users.append(user)

signup()
                         