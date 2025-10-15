# The list of ASCII ordinal values from the challenge
ascii_values = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Use a list comprehension to apply chr() to each value,
# then join the resulting characters into a single string.
flag = "".join([chr(value) for value in ascii_values])

# Print the final flag
print(flag)  