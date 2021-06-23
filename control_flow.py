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