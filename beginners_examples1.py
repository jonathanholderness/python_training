print("Hello, World!")

#Set some variables
acme_product_name = "Acme Product" #String
acme_product_description = "A high-quality product for your needs" #String
explosion_delay = 3
explosion_delay_actual = 0.2 #Float

print(type(explosion_delay_actual)) #output: <class 'float'>

#Strings
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

