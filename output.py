# Step 1: Write initial user input to file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.")

# Step 2: Append additional text
additional_text = input("\nEnter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:
    content = file.read()

    print(content)