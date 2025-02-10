def greet(name):
    # This function takes a name as input and returns a greeting string
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Prompt the user to enter their name
    name = input("Enter your name: ")
    # Print the greeting message
    print(greet(name))
