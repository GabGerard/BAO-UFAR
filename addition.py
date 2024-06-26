# addition.py
def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    num1 = 5
    num2 = 7
    result = add_numbers(num1, num2)

    with open("results.txt", "w") as file:
        file.write(f"The result of adding {num1} and {num2} is {result}\n")
