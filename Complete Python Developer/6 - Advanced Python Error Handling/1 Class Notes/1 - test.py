 # Error Handling

def sum(num1, num2):
    try:
        return num1 + num2
        raise Exception("Cut it out")
    except (TypeError, ZeroDivisionError):
        print(f"Please enter a number")
print(sum(1, "2"))
