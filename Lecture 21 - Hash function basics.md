# Lecture 21 - Examples

Hash functions are an essential part of cryptography. They take an input (or 'message') and return a fixed-size string of bytes. This output, usually a hash value, is typically a sequence of letters and numbers. The key properties of a hash function are:

1. **Deterministic**: The same input always produces the same output.
2. **Fast Computation**: Hash functions can be computed quickly.
3. **Preimage Resistance**: It should be infeasible to generate the original input from its hash value.
4. **Small Changes in Input Produce a Large Change in Output**: Even a tiny change in the input drastically changes the output.
5. **Collision Resistance**: It should be difficult to find two different inputs that produce the same output.

Let's go through a simple worked example using the SHA-256 hash function.

## Step-by-Step Example:

1. **Choose an Input**:
   Let's start with a simple string: "hello".

2. **Process the Input through the Hash Function**:
   Using SHA-256, the string "hello" is processed by the hash function.

3. **Generate the Hash Value**:
   The output hash value for "hello" using SHA-256 is:
   ```
   2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
   ```

4. **Observe the Output**:
   Notice that the output hash is a 64-character hexadecimal number, regardless of the length of the input.

5. **Change the Input Slightly**:
   Let's change our input slightly to "Hello" (with an uppercase 'H').
   
6. **Reprocess the Input through the Hash Function**:
   Using SHA-256, the string "Hello" is processed again.

7. **Generate the New Hash Value**:
   The new output hash value for "Hello" (with an uppercase 'H') using SHA-256 is:
   ```
   185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
   ```

8. **Compare the Hash Values**:
   Notice how drastically different the hash values are for "hello" and "Hello":
   - "hello": `2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824`
   - "Hello": `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

### Key Takeaways:

- **Hash functions** create a unique, fixed-size output from any input.
- **Even small changes** to the input create completely different hash values, enhancing security.
- **Irreversibility** means you can't retrieve the original input from the hash.


## Logic Behind the 64-Character Hex Number

1. **Hexadecimal Representation**:
   - Each character in a hexadecimal (hex) number represents 4 bits (binary digits).
   - Hexadecimal numbers use the digits 0-9 and the letters A-F, where:
     - `0` in hex is `0000` in binary
     - `1` in hex is `0001` in binary
     - `2` in hex is `0010` in binary
     - `3` in hex is `0011` in binary
     - `4` in hex is `0100` in binary
     - `5` in hex is `0101` in binary
     - `6` in hex is `0110` in binary
     - `7` in hex is `0111` in binary
     - `8` in hex is `1000` in binary
     - `9` in hex is `1001` in binary
     - `A` in hex is `1010` in binary
     - `B` in hex is `1011` in binary
     - `C` in hex is `1100` in binary
     - `D` in hex is `1101` in binary
     - `E` in hex is `1110` in binary
     - `F` in hex is `1111` in binary

2. **Converting Hex to Binary**:
   - A 64-character hex number can be converted to binary by converting each hex character to its 4-bit binary equivalent.
   - Since each hex character represents 4 bits, the entire 64-character hex number represents \(64 \times 4\) bits.

### Calculation:

\[ 64 \text{ characters} \times 4 \text{ bits/character} = 256 \text{ bits} \]

### Example:

Let's take the hash value we used earlier:

```
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

Converting each character to binary:

- `2` in hex is `0010` in binary
- `c` in hex is `1100` in binary
- `f` in hex is `1111` in binary
- `2` in hex is `0010` in binary
- ...

Continuing this for all 64 characters, you'll get a 256-bit binary representation.

### Key Points:

- **Hexadecimal** simplifies the representation of large binary numbers.
- **Each hex character** is a shorthand for 4 binary digits.
- A **64-character hex** value represents a **256-bit** binary number.

## Simple Hash Function Example

Let's look at a very simple hash function called the **sum-of-characters hash**. This example is far from cryptographically secure, but it will give you an idea of how a basic hash function works. Here’s a step-by-step explanation:

### Sum-of-Characters Hash Algorithm:

1. **Input**:
   - The string "hi".

2. **Initialize a Variable**:
   - Set a variable `sum` to 0. This variable will hold the sum of the character values.

3. **Convert Each Character to Its ASCII Value**:
   - ASCII value of 'h': 104
   - ASCII value of 'i': 105

4. **Sum the ASCII Values**:
   - `sum = 104 + 105`

5. **Hash Value**:
   - In this basic example, the hash value is just the sum of the ASCII values.

### Step-by-Step Calculation:

1. **Input**: "hi"

2. **ASCII Conversion**:
   - 'h' -> 104
   - 'i' -> 105

3. **Sum**:
   - `sum = 104 + 105 = 209`

4. **Hash Value**:
   - The hash value for "hi" is 209.

### Example in Python:

Here’s a simple implementation of the sum-of-characters hash function in Python:

```python
def simple_hash(input_string):
    sum = 0
    for char in input_string:
        sum += ord(char)
    return sum

input_string = "hi"
hash_value = simple_hash(input_string)
print("Hash value:", hash_value)
```

### Explanation:

- **ord(char)**: This function returns the ASCII value of the character `char`.
- **sum += ord(char)**: This line adds the ASCII value of `char` to `sum` for each character in the input string.
- The result, `209`, is the simple hash value for "hi".

Again, this is a very basic hash function and is not suitable for cryptographic purposes. It's just a simple example to illustrate how hashing works. In real-world applications, more complex and secure hash functions like SHA-256 are used.

---
To ensure that the hash value becomes exactly 256 bits, you can pad the output to meet the required bit length. This technique is commonly used in cryptographic hash functions.

### Padding a Simple Hash Function to 256 Bits:

1. **Generate the Initial Hash**:
   - Let's say the initial hash value from our sum-of-characters hash function is `209`.

2. **Convert to Binary**:
   - First, we convert the hash value to a binary string:

     ```python
     hash_value = 209
     binary_hash = bin(hash_value)[2:]  # Remove the '0b' prefix
     ```

3. **Pad the Binary String**:
   - To ensure the binary string is exactly 256 bits, we can pad it with leading zeros if it's shorter than 256 bits:

     ```python
     padded_binary_hash = binary_hash.zfill(256)
     ```

### Example in Python:

Here's how you can pad the hash value to 256 bits:

```python
def simple_hash(input_string):
    sum = 0
    for char in input_string:
        sum += ord(char)
    return sum

def pad_to_256_bits(hash_value):
    binary_hash = bin(hash_value)[2:]  # Convert to binary and remove '0b' prefix
    padded_binary_hash = binary_hash.zfill(256)  # Pad with leading zeros to 256 bits
    return padded_binary_hash

input_string = "hi"
hash_value = simple_hash(input_string)
padded_hash = pad_to_256_bits(hash_value)
print("Padded Hash (256 bits):", padded_hash)
print("Length of Padded Hash:", len(padded_hash), "bits")
```

### Explanation

- `bin(hash_value)[2:]`: Converts the integer hash value to a binary string and removes the '0b' prefix.
- `binary_hash.zfill(256)`: Pads the binary string with leading zeros to ensure it's exactly 256 bits long.

### Result

Running the above code will give you a 256-bit binary string:

```
Padded Hash (256 bits): 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011010001
Length of Padded Hash: 256 bits
```

This way, you can ensure that your hash output is always 256 bits, regardless of the initial hash value's length. Padding is a common technique to meet fixed bit-length requirements in cryptographic applications.

