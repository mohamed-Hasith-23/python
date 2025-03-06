# Name should be less than 12 Characters
# Name doesn't have space
# Name shouldn't  have Numbeers

Name = input("Enter your name: ")

if len(Name) < 12 and Name.count(" ") == 0 and Name.isalpha() == True:
    print(Name)
else:
    print("Enter the correct name")

