print("hello")
if True:
    print("tab")
else:
    print("false")

def testing(a, b):
    """add two numbers

    Args:
        a (int): first value
        b (int): second value

    Returns:
        int: sum of two
    """

    return a + b

v = testing(1, 6)
print(v)