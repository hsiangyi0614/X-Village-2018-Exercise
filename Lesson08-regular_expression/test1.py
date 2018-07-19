import re

# Search sub-string in text
text = "Today is good day to learn regular expression."

# Define re pattern
pattern = r'regular expression'

# Search if there is 'regular expression' in the text
match = re.search(pattern, text)

# Check result
start_index = match.span()[0]
end_index = match.span()[1]
match_string = match.group()
print("The location of '{}' is between {} and {} in text".format(match_string, start_index, end_index))
