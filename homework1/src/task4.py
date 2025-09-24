#calculates the discounted price
def calculate_discount(price, discount):
    #if the values are not integers or floats
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("Price and discount must be numeric.")
    #if the discount percent is not a viable number
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100.")
    #returns discounted price
    return price * (1 - discount/100)