from utility import division, multiply  # Not the best to not overwrite some existing module
from shopping.more_shopping import shopping_cart  # The best way
if __name__ == "__main__":
    print("Run this code")
    print(division(2, 3))
    print(shopping_cart.buy("Apple"))
    print(multiply(2, 3))


