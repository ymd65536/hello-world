def greet(name: str) -> str:
    """Function to greet a person with their name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Example usage of the greet function
    name = "Alice"
    print(greet(name))
    # Output: Hello, Alice!