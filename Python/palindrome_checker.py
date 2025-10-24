# Palindrome Checker
# This program checks whether a given word or phrase is a palindrome.

def is_palindrome(text):
    # Remove spaces and make lowercase
    text = text.replace(" ", "").lower()
    return text == text[::-1]

if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")
    if is_palindrome(user_input):
        print("✅ It's a palindrome!")
    else:
        print("❌ Not a palindrome.")
