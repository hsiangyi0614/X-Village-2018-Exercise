import re
name1 =input("Enter name : ")
name2 =input("Enter name : ")
name3 =input("Enter name : ")

# Define pattern
pattern = r'(?P<firstname>\w\w\w) (?P<lastname>\w\w\w\w)'

# search pattern
match1 = re.search(pattern, name1)
match2 = re.search(pattern, name2)
match3 = re.search(pattern, name3)

# Check
print(match1.groupdict())
print(match2.groupdict())
print(match3.groupdict())
