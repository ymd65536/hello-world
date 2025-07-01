def greet(name: str, language: str = "en") -> str:
    """Function to greet a person with their name in the specified language.
    
    Args:
        name: The name of the person to greet
        language: The language for the greeting ('en' for English, 'ja' for Japanese)
    
    Returns:
        A greeting string in the specified language
    """
    if language == "ja":
        return f"こんにちは、{name}さん！"
    else:
        return f"Hello, {name}!"


if __name__ == "__main__":
    # Example usage of the greet function
    name = "Alice"
    print(greet(name))  # Default English greeting
    print(greet(name, "ja"))  # Japanese greeting
    # Output: Hello, Alice!
    # Output: こんにちは、Aliceさん！