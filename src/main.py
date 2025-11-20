def find_sum(numbers):
    """Return the sum of the provided numbers."""
    return sum(numbers)

def greet(name):
    """Return a friendly greeting."""
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"

if __name__ == "__main__":
    nums = [1, 2, 3]
    print("Sum is:", find_sum(nums))
    print(greet("Aswin"))
