import re

# DEMO examples
# replace a word in the text
def replace_word(text, old_word, new_word):
    pattern = re.compile(r'\b' + re.escape(old_word) + r'\b')
    return pattern.sub(new_word, text)

# Example usage
text = "You like apples, but I prefer oranges."
new_text = replace_word(text, "apples", "bananas")
print(new_text)  # Output: "You like bananas, but I prefer oranges."


# extract phone number which contains 10 digits and two - separators
def extract_phone_numbers(text):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    return re.findall(pattern, text)

# Example usage
text = "Contact us at 123-456-7890 or 987-654-3210."
phone_numbers = extract_phone_numbers(text)
print(phone_numbers)  # Output: ['123-456-7890', '987-654-3210']

# does it look like a valid email?
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email1 = "user@example.com"
email2 = "invalid_email.com"

print(validate_email(email1))  # Output: True
print(validate_email(email2))  # Output: False

# The BASICS
# simple matching. 
# Pay attention to r in the pattern for search which means it's a raw string
# Raw string says to Python: take it at face value even if it contains special characters
# Always use raw strings as patterns in regex
result = re.search(r'ain', "The rain in Spain")
print(result) # output: <re.Match object; span=(5, 8), match='ain'>

# use findall to get all matches
result = re.findall(r'ain', "The rain in Spain")
print(result) # output: ['ain', 'ain']

# using a dot (.) and [] in pattern, like below - any lower case vowel. 
# A dot is a special character, wildcard. It stands for any character
# to match the beginning of the string use ^
# to match the end of the string use $
print (re.search(r'h.n', "python")) # output: <re.Match object; span=(3, 6), match='hon'>
print(re.search(r'[aeiou].[aeiou]', "Smile")) # output: <re.Match object; span=(2, 5), match='ile'>
print(re.search(r'[aeiou].[aeiou]', "Smith")) # output: None
string1 = "hello beautiful world"
string2 = "hello amazing world!"
print(re.search(r'world$', string1)) # Output: <re.Match object; span=(16, 21), match='world'>
print(re.search(r'world$', string2)) # Output: None

# using other special characters
# [a-z] corresponds to any lower case letter
# [0-9] corresponds to  all digits
# \w it matches any alphanumeric character including _
# this is equivalent to the class [a-zA-Z0-9_]
# \s matches spaces, tabs, and newline character
# character ^ within [] means 'not'
# so r"[^\w\s]" matches any single character that is not a word character or
# spaces, tabs, and newline character, i.e. dots, commas, hash, dollar and so on
# use it to remove punctuation and other technical characters with re.sub
# Sample string containing various characters
sample_string = "Hello! How are you doing? 12345 #example"

# Using the pattern to remove non-word and non-whitespace characters
cleaned_string = re.sub(r'[^\w\s]', '', sample_string)

# Output the cleaned string
print(cleaned_string) # Output: Hello How are you doing 12345 example

# you can also use r"me|us" to accept bot me and us
print(re.search(r"me|us", 'Are they going to invite us?')) # Output: <re.Match object; span=(25, 27), match='us'>
print(re.search(r"me|us", 'Are they going to invite you?')) # Output: None
print(re.findall(r"rain|snow", 'I hate both rain and snow')) # Output: ['rain', 'snow']

# character repition - use * or + after a character which can be repeated any number of times
# + covers 1,2,3,...
# * covers 0,1,2,3,...
# so ^hello.*world$ matches strings startin with hello, anding with world and any number of characters in between
pattern = r'^hello.*world$'

string1 = "hello world"
string2 = "hello wonderful world"
string3 = "hello amazing world!"

# Check if each string matches the pattern
for string in [string1, string2, string3]:
    if re.match(pattern, string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match the pattern")


# ? is another multiplier , it means either 0 or 1 repetition

# Example strings US bs British spelling
strings = ["color", "colour", "favorite", "favourite"]

# Regular expression pattern to match "color" or "colour"
pattern = r'colou?r'

# Check if each string matches the pattern
for string in strings:
    if re.match(pattern, string):
        print(f"'{string}' matches the pattern")
    else:
        print(f"'{string}' does not match the pattern")

# DEMO Example: how to use regular expressions to check 
# if a given string represents a valid variable name
def is_valid_variable_name(variable_name):
    # Regular expression pattern to match a valid variable name
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    
    # Check if the variable name matches the pattern
    if re.match(pattern, variable_name):
        return True
    else:
        return False

# Example variable names
variable_names = ["my_variable", "_variable", "123variable", "variable123", "var!able"]

# Check if each variable name is valid
for name in variable_names:
    if is_valid_variable_name(name):
        print(f"'{name}' is a valid variable name.")
    else:
        print(f"'{name}' is not a valid variable name.")