# The customer's name     by NTEGE HARUNA
name = input("Hello! What is your name? ")
tickets = int(input(f"Hi {name}, how many tickets would you like to book? "))

print("The cost of an ticket is $12")
ticket_price = 12

#  the total cost
total_cost = tickets * ticket_price

# Print a booking confirmation
print(f"\nBooking Confirmation for {name}!")
print(f"Number of tickets: {tickets}")
print(f"Total cost: ${total_cost}")
print("\nThank you for booking with us! We hope you enjoy the movie 💥👁‍🗨")
