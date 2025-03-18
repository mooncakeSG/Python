# Python
Weekly Challenge 
# Task 1: List sum program
def list_sum_program():
    # Get user input for list of integers
    user_input = input("Enter integers separated by spaces: ")
    
    # Convert input string to list of integers
    num_list = [int(num) for num in user_input.split()]
    
    # Calculate sum
    total = sum(num_list)
    
    # Display results
    print(f"Your list: {num_list}")
    print(f"Sum of all integers: {total}")

# Task 2: Tuple of favorite books
def favorite_books():
    # Create tuple of favorite books
    books = ("To Kill a Mockingbird", "1984", "The Great Gatsby", 
             "The Catcher in the Rye", "Pride and Prejudice")
    
    # Print each book on a separate line
    print("My favorite books:")
    for book in books:
        print(book)

# Task 3: Dictionary for person information
def person_info():
    # Create empty dictionary
    person = {}
    
    # Get user input
    person["name"] = input("Enter your name: ")
    person["age"] = int(input("Enter your age: "))
    person["favorite_color"] = input("Enter your favorite color: ")
    
    # Print the dictionary
    print("\nPerson Information:")
    print(person)

# Task 4: Common elements in two sets
def common_elements():
    # Get first set
    set1_input = input("Enter first set of integers separated by spaces: ")
    set1 = set([int(num) for num in set1_input.split()])
    
    # Get second set
    set2_input = input("Enter second set of integers separated by spaces: ")
    set2 = set([int(num) for num in set2_input.split()])
    
    # Find common elements
    common = set1.intersection(set2)
    
    # Display results
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Common elements: {common}")

# Task 5: Words with odd number of characters
def odd_length_words():
    # Get list of words
    words_input = input("Enter a list of words separated by spaces: ")
    words = words_input.split()
    
    # Use list comprehension to find words with odd length
    odd_words = [word for word in words if len(word) % 2 != 0]
    
    # Display results
    print(f"All words: {words}")
    print(f"Words with odd number of characters: {odd_words}")

# Main program to run all tasks
def main():
    while True:
        print("\n===== PYTHON DATA STRUCTURES PRACTICE =====")
        print("1. List Sum Program")
        print("2. Favorite Books Tuple")
        print("3. Person Information Dictionary")
        print("4. Common Elements in Sets")
        print("5. Words with Odd Characters")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            list_sum_program()
        elif choice == '2':
            favorite_books()
        elif choice == '3':
            person_info()
        elif choice == '4':
            common_elements()
        elif choice == '5':
            odd_length_words()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
