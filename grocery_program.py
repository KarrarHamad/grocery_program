grocery_items = {
    "apple": 1.0,
    "banana": 0.5,
    "milk": 3.0,
    "bread": 2.0,
}
cart = {}
while True:
    item = input(
        "Enter an item to buy (or type 'done' to finish): ").strip().lower()
    if item == "done":
        break
    parts = item.split()
    item_name = parts[0]
    quantity = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1

    if item_name in grocery_items:
        if item_name in cart:
            cart[item_name] += quantity
        else:
            cart[item_name] = quantity
    else:
        print("Sorry, we don't have that item.")
# Continuosly ask the user to input what they want to buy, and stop when they type "done"
# If the item is in the dictionary, add it to a list of items to buy
# If the item is not in the dictionary, print a message saying "Sorry, we don't have that item."
# After finishing, print the total cost of the items in the list using a loop (use the prices that i like)
# if the If the total is greater than $10, print "You spent a lot!", otherwise print "You spent a little!"
# Print the final list of items and the total cost.
# Let the user type a quantity after the item (example: apple 3). Update your code so it multiplies the price by the quantity.
# Save the cart to a dictionary like: cart = {"apple": 3, "milk": 1}
# Add a discount rule: if "milk" is bought more than 2 times, reduce the price by $1.
