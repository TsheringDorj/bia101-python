# ! check if user can vote

# ?Get user age from input
# ?convert userinput(str) to int() to number
# ?check if user can vote
# ?if else statement
# ?if above 18, print "You can vote"
 # ?if below 18, print "You canot vote"

# Get user age from input
user_age = input("Enter your age: ")

# Convert user input (str) to int
user_age = int(user_age)

# Check if user can vote
if user_age >= 18:
   print("You can vote")
else:
   print("You cannot vote")