try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line, end="")
except FileNotFoundError:
    print("Error: sample.txt does not exist!")