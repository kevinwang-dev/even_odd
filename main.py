# Ask user for a number and print a message based on even or odd

print("Welcome to the Even or Odd app!!!")

# ask user for a number

number = int(input("\nPlease enter a number: "))

# determine number is even or odd using conditionals

if number % 2 == 0:
  print("\nThe number you entered is Even!")
else:
  print("\nThe number you entered is Odd!")