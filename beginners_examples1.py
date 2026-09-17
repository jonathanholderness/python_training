print("Hello, World!")

#Set some variables
acme_product_name = "Acme Product" #String
acme_product_description = "A high-quality product for your needs" #String
explosion_delay = 3
explosion_delay_actual = 0.2 #Float

print(type(explosion_delay_actual)) #output: <class 'float'>

#Strings
#Concatenate strings with the + operator
acme_product_name = "Acme Product" #String
acme_product_description = "A high-quality product for your needs" #String
print(acme_product_name + " - " + acme_product_description) #output: Acme Product - A high-quality product for your needs

#f sting
message = f"{acme_product_name} - {acme_product_description}"
print(message) #output: Acme Product - A high-quality product for your needs

#Inputs
user_input = input("Please enter your name: ")
print(f"Hello, {user_input}!")

#Lists
#Create a list of products and choose the second item in the list
acme_products = ["Rocket", "Anvil", "Dynamite"]
print(acme_products[1]) #output: Anvil

#Add to the list, find the length of the list
acme_products.append("Giant Rubber Band")
print(acme_products) #output: ['Rocket', 'Anvil', 'Dynamite
print(len(acme_products)) #output: 4

#Simple if statement
explosion_delay_actual = 0.2 
if explosion_delay_actual < 1:
    print("Boom") #output: Warning: Explosion delay is less than 1 second!
else:
    print("Phew")

#Simple 'for' loop
for product in acme_products:
    print(product) #output: Rocket, Anvil, Dynamite, Giant Rubber Bandjon


#Create a new function
def calculate_tip(bill, percentage):
    """
    This function calculates the tip amount based on the bill amount and tip percentage.
    bill_amount: float
    tip_percentage: float (e.g., 0.15 for 15%)
    
    returns: float
    """
    tip_amount = bill * (percentage/100)
    return tip_amount

bill_amount = float(input("Enter the bill amount: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

tip = calculate_tip(bill_amount, tip_percentage)
total_amount = bill_amount + tip

print(f"Tip amount: £{tip:.2f}")
print(f"Total amount to pay:£{total_amount:.2f}")