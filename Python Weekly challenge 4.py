# Step 1: Create input.txt file with some sample text
with open("input.txt", "w") as input_file:
    input_file.write("Hello world! This is a sample text file.\n")
    input_file.write("We are processing files using Python.\n")
    input_file.write("File handling is an essential skill for programmers.\n")
    input_file.write("This script demonstrates reading and writing files.\n")
    input_file.write("Let's count the words and convert text to uppercase!")

# Step 2: Read and process the input file
try:
    # Open and read the input file
    with open("input.txt", "r") as input_file:
        content = input_file.read()
    
    # Process the content
    word_count = len(content.split())
    uppercase_content = content.upper()
    
    # Write processed content to output file
    with open("output.txt", "w") as output_file:
        output_file.write(uppercase_content + "\n\n")
        output_file.write(f"Word Count: {word_count}")
    
    # Print success message
    print("Success! The file has been processed.")
    print(f"The input file contains {word_count} words.")
    print("The processed content has been written to output.txt.")
    
except FileNotFoundError:
    print("Error: The input file could not be found.")
except Exception as e:
    print(f"An error occurred: {e}")