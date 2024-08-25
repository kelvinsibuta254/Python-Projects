def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "You can't divide by zero"
    except TypeError:
        return "Both arguments must be numbers"
    else:
        return f"The result is {result}"
    finally:
        print("Division attempt complete.")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "two"))