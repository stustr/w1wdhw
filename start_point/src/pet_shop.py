# WRITE YOUR FUNCTIONS HERE
# 1
def get_pet_shop_name(petshop):
    return petshop["name"]


# 2
def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]


# 3 & 4
def add_or_remove_cash(petshop, amount):
    current = get_total_cash(petshop)
    current += amount
    petshop["admin"]["total_cash"] = current


# 5
def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]


# 6
def increase_pets_sold(petshop, amount):
    current = get_pets_sold(petshop)
    current += amount
    petshop["admin"]["pets_sold"] = current


# 7
def get_stock_count(petshop):
    return len(petshop["pets"])


# 8
def get_pets_by_breed(petshop, breed):
    matching = []
    for pet in petshop["pets"]:
        if pet["breed"] == breed:
            matching.append(pet)

    return matching


# 9
def find_pet_by_name(petshop, name):
    for p in petshop['pets']:
        if p['name'] == name:
            return p

# 10
def remove_pet_by_name(petshop, name):
    for p in petshop['pets']:
        if p['name'] == name:
            petshop['pets'].remove(p)
            
# 11
def add_pet_to_stock(petshop, pet):
    petshop['pets'].append(pet)
    
# 12
def get_customer_cash(customer):
    return customer['cash']

# 13
def remove_customer_cash(customer, amount):
   current = get_customer_cash(customer)
   current -= amount
   customer['cash'] = current
   
# 14
def get_customer_pet_count(customer):
    return len(customer['pets'])

# 15
def add_pet_to_customer(customer, pet):
    customer['pets'].append(pet)
    
# 16 17 18
def customer_can_afford_pet(customer, pet):
    affordable = False
    if get_customer_cash(customer) >= pet['price']:
        affordable = True
    return affordable

# 19
