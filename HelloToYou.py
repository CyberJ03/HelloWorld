# # This program prints Hello World

# name = "Joe"

# if name == "Joseph":
#     print("Hello,", name)
# else:
#     print ("Oh, well, what is your name then?")

def checkName(name):
    answer = input("Is your name " + name + "? ")

    if answer.lower() == "yes": 
        # lower() turns the answer into lowercase
        print("Hello,", name)
    else:
        new_name = input("we're sorry about that. What is your name again? ")
        print("Welcome,", new_name)

checkName("Joseph")