# Step 1: Read from the original file
with open("original.txt", "r") as original_file:
    content = original_file.read()

# Step 2: Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Step 3: Write the modified content to a new file
with open("modified.txt", "w") as modified_file:
    modified_file.write(modified_content)

print(" File has been read, modified, and written to 'modified.txt'")



# File Read & Write  with Error Handling 

try:
    filename = input("Enter the name of the file to read: ")

    with open(filename, "r") as file:
        content = file.read()

    # Modify the content (e.g., reverse it just for fun)
    modified_content = content.upper()  # You can replace this with any transformation

    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f" Success! Modified content written to '{new_filename}'.")

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except PermissionError:
    print(" Error: You don’t have permission to read this file.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
