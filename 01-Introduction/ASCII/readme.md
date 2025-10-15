# Challenge: ASCII

- **Category**: Introduction / Encoding
- **Points**: 5

## 📖 Problem Description

ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.

Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.

`[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]`

*Hint: In Python, the `chr()` function can be used to convert an ASCII ordinal number to a character (the `ord()` function does the opposite).*

## 🤔 Thought Process

The problem asks us to convert a list of numbers into text. The challenge name "ASCII" and the description clearly indicate that these numbers are ASCII decimal values.

The logic is as follows:
1.  Take the list of numbers provided by the challenge.
2.  Go through each number in the list one by one.
3.  For each number, find the corresponding character based on the ASCII standard.
4.  The hint helpfully points to the built-in `chr()` function in Python, which is designed for exactly this purpose.
5.  After converting all the numbers, we just need to join the resulting characters together to form the flag.

## 🐍 Solution

We can write a very simple Python script to solve this. The most "Pythonic" way is to use a list comprehension and the `"".join()` method to build the final string in a single line.

### Python Script

```python
# The list of ASCII ordinal values from the challenge
ascii_values = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Use a list comprehension to apply chr() to each value,
# then join the resulting characters into a single string.
flag = "".join([chr(value) for value in ascii_values])

# Print the final flag
print(flag)  
 ```

#### 🎯 Flag from the Challenge

    Running the script above produces the flag:  
    ```crypto{ASCII_pr1nt4bl3}```


---

##### 🧠 Key Takeaways

 1. **ASCII Encoding**
- This challenge demonstrates how ASCII encoding works, where each character on a keyboard has a corresponding integer value.

 2. **Python's `chr()` and `ord()`**
- `chr(integer)`: Converts an integer to its ASCII character.
- `ord(character)`: Converts a character to its ASCII integer value.

 3. **Data Representation**
- It highlights that data can be represented in many formats, with string representation and a list of ASCII values being two examples.
