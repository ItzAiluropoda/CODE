
import datetime  # Import datetime library to handle date and time

# Define the menu with items and their prices
Menu = {
    'Burger': 100,
    'Fries': 40,
    'Coke': 30,
    'Sandwich': 80
}
order = {}  # Initialize an empty order dictionary

# Function to display the menu
def show_menu(menu):
    for key, value in menu.items():
        print(f'{key}: {value}')  # Print each item and its price

# Function to add an item to the order
def add_to_order(item):
    if item in Menu:  # Check if the item is in the menu
        if item in order:
            order[item] += 1  # Increment the quantity if the item is already in the order
        else:
            order[item] = 1  # Add the item to the order with quantity 1
    else:
        print('Enter valid item')  # Print error message if the item is not in the menu

# Function to display the current order and total cost
def show_order(order):
    if order != {}:  # Check if the order is not empty
        print('Current Order: ')
        for key, value in order.items():
            print(f'{key}: {value}')  # Print each item and its quantity
        print('Total: ', order_total(order))  # Print the total cost
    else:
        pass

# Function to calculate the total cost of the order
def order_total(order):
    total = 0
    for key, val in order.items():
        total += Menu[key] * order[key]  # Calculate total cost by summing up the cost of each item
    return total
def main():
    userinput = ''
    print('Welcome to Fastest foods! What would you like to have?')
    show_menu(Menu)  # Display the menu
    
    while userinput.lower() != 'done':  # Loop until the user types 'done'
        userinput = input('What would you like to have? (Type "done" when finished): ').title()
        if userinput.lower() != 'done':
            add_to_order(userinput)  # Add the item to the order
            show_order(order)  # Display the current order
    
    print(f'Thank you for your order! Your total is {order_total(order)}')
# Run the main function if this script is executed
if __name__ == '__main__':
    main()