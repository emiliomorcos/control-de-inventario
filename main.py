from Ingredient import Ingredient
from Inventory import Inventory

inventory = Inventory()
inventory.add_ingredient("Sugar", 10, "kg", 5)

x = True
print("Welcome to the inventory system")
while x:
  print("1. Add ingredient")
  print("2. Remove ingredient")
  print("3. Update ingredient ")
  print("4. Check ingredient")
  print("5. List inventory")
  print("6. Check low stock")
  print("7. View usage log")
  print("8. Generate up-to-date report")
  print("9. Exit")
  print()

  user_input = int(input("Please give a command\n"))

  # 1. Adding ingredient
  if user_input == 1: 
    add_name = input("Ingredient name:\n")
    add_quantity = int(input("Ingredient quantity:\n"))
    add_unit = input("Unit of measure:\n")
    add_lowstock = int(input(f"Number of {add_unit} for low stock alert:\n"))
    inventory.add_ingredient(add_name, add_quantity, add_unit, add_lowstock)
    print()
    print(f"{add_quantity} {add_unit} of {add_name} added succesfully!\n")

  # 2. Removing ingredient
  elif user_input == 2:
    remove_name = input("Ingredient name:\n")
    remove_quantity = int(input("Ingredient quantity to remove:\n"))
    inventory.remove_ingredient(remove_name, remove_quantity)

  # 3. Updating ingredient
  elif user_input == 3:
    update_name = input("Which ingredient would you like to update?\n")
    update_quantity = int(input("New quantity in inventory:\n"))
    update_unit = None
    update_lowstock = None
    update_info = int(input("Would you like to update unit of measurement?\n1. Yes\n2. No\n"))
    if update_info == 1:
      update_unit = input("Specify new unit:\n")
    update_info2 = int(input("Would you like to update low stock threshold of measurement?\n1. Yes\n2. No\n"))
    if update_info2 == 1:
      update_lowstock = int(input("Specify new low stock threshold:\n"))
    inventory.update_ingredient(update_name, update_quantity, update_unit, update_lowstock)
    print(f"{update_name} has been updated succesfully!\n")

  # 4. Check ingredient
  elif user_input == 4:
    check_name = input("Name of ingredient to check:\n")
    print(inventory.get_ingredient(check_name))
    print()

  # 5. Check inventory
  elif user_input == 5:
    for ingredient in inventory.list_ingredients():
      print(ingredient)
    print()

  # 6. Check low stock
  elif user_input == 6:
    inventory.check_low_stock()
    print()

  # 7. View usage log
  elif user_input == 7:
    for log_entry in inventory.view_usage_log():
      print(log_entry)

    print()

  # 8. Generate report
  elif user_input == 8:
    inventory.generate_report()

    print()

  # Exit
  elif user_input == 9:
    print("Logging off")
    x = False
    

  
    
    
    

  

# inventory.add_ingredient("Sugar", 10, "kg", 3)
# inventory.add_ingredient("Flour", 15, "kg", 5)
# inventory.add_ingredient("Tomatoes", 20, "kg", 5)
# print(inventory.list_ingredients())

# inventory.remove_ingredient("Sugar", 3)
# inventory.remove_ingredient("Flour", 10)
# inventory.remove_ingredient("Tomatoes", 14)
# print(inventory.list_ingredients())

# print(inventory.get_ingredient("sugar"))
