from sys import argv

user_name = argv 
Age = 0    
prompt = '-->'

print(f"Name?")
user_name = input(prompt)

print(f"Age?")
Age = input(prompt)
    
print(f"Thank you for stopping by {user_name}.")
print(f"Age {Age}.")