# Enter yiur name and favourte number   by NTEGE HARUNA 
full_name = input("Enter your full name: ")
favorite_num = input("Enter your favorite number: ")

# 1st 4 characters into lower case
handle_name = full_name[:4].lower()

# Create the handle by concatenating the handle_name, favorite_number, and 'traac'
handle =  (f"{handle_name}{favorite_num}traac")

# Print the handle
print("Your handle is:", handle)