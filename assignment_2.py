# Order summary calculation program
def calculate_total(items, tax_rate): 
    """
    Function definition to calculate total 
    with items and tax_rate as parameters
    """
    subtotal = sum(items) # sum of all items to calculate subtotal using sum function
    tax = subtotal * tax_rate # Tax is calculated by multiplying subtotal with tax_rate
    total = subtotal + tax # Total is calculated by adding subtotal and tax
    return subtotal, tax, total

prices = [29.99, 45.50, 12.99]
rate = 0.08
sub, tax, total = calculate_total(prices, rate)
print(f"Order Summary: ${total:.2f}") # .2f is used to get 2 decimals