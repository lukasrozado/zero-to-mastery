def say_hello (name = "Clara", emoji = ";D"):
    """
    Default value = Clara and Emoji = ;D
    This functions says hello with param {name} and {emoji}.
    """
    print(f"Hello {name} {emoji}")
say_hello()
help(say_hello)
print(say_hello.__doc__)