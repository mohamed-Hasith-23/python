Item_Name = input("Enter the name of the product you want to buy :")
Price = float(input("enter the price of your product :"))
Quantity = int(input("How many you want? "))

Total = Price * Quantity

print(f"you have bought {Quantity} x {Item_Name}")
print(f"total price is {round(Total, 3)}")