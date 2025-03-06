Credit_card = input("Enter your credit card number like xxxx-xxxx-xxxx-xxxx: ")

# # TO find last 4 digit of credit card

last_four = Credit_card[-4:]

print(last_four)

# # to reverse all numbers

reverse = Credit_card[::-1]

print(reverse)

# to get Email And Seperate with Domain and Username

Email = input("enter your emial adddress: ")

index = Email.index("@")

username = Email[:index]

domain = Email[index + 1:]

print(f"The Username of Email is {username}")

print(f"the doamin of Email is {domain}")
