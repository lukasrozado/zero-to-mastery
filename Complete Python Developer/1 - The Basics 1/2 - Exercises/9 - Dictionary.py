#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    "username" : None,
    "age" : None,
    "weapons" : None,
    "is_active" : None,
    "clan" : None,
}
#2 iterate and print all the keys in the above user.

print(user_profile.keys())

#3 Add a new weapon to your user

user_profile.update({"weapons" : "Excalibur"})
print(user_profile)

#4 Add a new key to include 'is_banned'. Set it to false

user_profile["is_banned"] = False
print(user_profile)

#5 Ban the user by setting the previous key to True

user_profile.update({"is_banned" : True})
print(user_profile)

#6 create a new user2 my copying the previous user and update the age value and username value. 
user_profile2 = user_profile.copy()
user_profile2.update({"age" : 20})
user_profile2.update({"username" : "Lukas"})
print(user_profile2)