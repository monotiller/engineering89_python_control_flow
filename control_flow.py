# Syntax
# if variable condition age:

weather = "sunny"

if weather == "sunny": # if this condition is true the next line would execute
    print("Enjoy the weather") # this line needs to be indented inside the code block

if weather == "rainy": # if this condition is true the next line would execute
    print("Take an umbrella") # this line needs to be indented inside the code block

if weather != "rainy": # if this condition is not true the next line would execute
    print("There is no rain, enjoy the sun!") # this line needs to be indented inside the code block

# Let's use our ticket age criteria
age = 17

if age < 18: # Checking the condition according to the age given
    print("You are not eligible to watch this film")
else: # Give the user a different message if they are 18 or over!
    print("Enjoy the film!")

# For loops and whole loops
# Loops help us iterate through our data, such as Lists, Dict, Sets etc.
shopping_list = ["eggs", "apples", "milk", "bread", "butter"]
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])
print(shopping_list[4])

for items in shopping_list:
    print(items)

# Second iterations with if conditions
shopping_list = ["eggs", "apples", "milk", "bread", "butter"]
for items in shopping_list:
    if items == "bread": # if this condition is True
        break # Stop the loop
    print(items)

# Third itterations with Dict
student_data = {
    "student_name": "James", # string
    "course": "DevOps", # string
    "course_topics": 4, # int
    "topic_names": ["Business Week", "Python", "Virtualisation with Vagrant", "AWS cloud"] # list
}

print(student_data)
# Lets itterate through our dict
for data in student_data.values():
    if data == "James": # if condition is True the loop exits
        print(data)

# In any case for loop would iterate through the data until the last item of condition is True

# While loops are essentially used to monitor the data

num = 0

while num < 10:
    print(f"it's working -> {num}") # The `f` enables formatting
    num += 1 # adding 1 into num value each time it iterates through

# Second iteration iteration
num = 0

while num < 10:
    print(f"it's working -> {num}") # The `f` enables formatting
    if num == 5: # as soon as this condition is True it would exit
        break
    num += 1 # adding 1 into num value each time it iterates through

# Let's see how can we interact with our user in the third iteration?
# Prompt the user to input age and restrict to enter in digits only
# Check if the data is in digits display it back to the user if not in digits prompt the user with message to enter in digits
age = input("How old are you? ")
while age.isdigit() == False:
    age = input("Please use a number for your age: ")
print(f"Your age is -> {age}")

# Final Iteration
user_prompt = True

while user_prompt:
    age = input(" Please enter you age ? ")
    if age.isdigit() and int(age) < 177: #
        user_prompt = False
    else:
        print("Please provide your answer in digit, below 117")
print(f"your age is {age}")