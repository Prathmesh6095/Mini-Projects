# # String concatenation (How to put strings together)
# # Suppose we want to create a string that says "subscribe to ________ "
# youtuber="Prathamesh Hatkar"#Some string variable

# # A few ways to say this 
# print("subscribe to "+youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("verb1: ")
verb2 = input("verb2: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time  because \
I love to {verb1}. Stay hydrated and {verb2}, You are {famous_person}!"  

print(madlib)

