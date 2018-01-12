#for testing usernames, users enter "George"
#for selling, users enter "Adidas"
#users should be added to list ---
#[{'name': 'Andy', 'selling': ['nike8', 'Addidas9']}, {'name': 'George', 'selling': ['Adidas']}]

#first we have a list of users where each useer is a dictionary
users = [{"name":"Andy","selling":["nike8","Addidas9"]}]
#now let's make a function to add a user
def signup():
    user = {"name":"","selling":[]}
    user["name"] = input("What is your name?")
    user["selling"].append(input("What are you selling?"))
    users.append(user)
def view_profile(pname):
    for i in users:
        if i["name"]==pname:
            print(i["name"], "is currently selling ")
            for j in i["selling"]:
                print(j)
signup()
print(users)
profile=input("which user do you want to view")
view_profile(profile)
                         