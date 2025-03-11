# Lecture 22 - Examples


## Example 1

Below is a simplified step-by-step example of creating a cryptographic hash of the message "hello" using a SHA (Secure Hash Algorithm), such as SHA-256.

### Step 1: Input the Message
The input message is `"hello"`. In computing, text is represented in binary. The ASCII representation of "hello" in binary is:

```
01101000 01100101 01101100 01101100 01101111
```

### Step 2: Pre-Processing
1. **Padding the Message**: SHA algorithms require the input message to have a length that's a multiple of 512 bits. So, we pad the binary representation of "hello" to fit this requirement. Padding typically involves:
   - Adding a "1" bit at the end.
   - Adding enough "0" bits to make the length 448 bits (512 bits minus 64 bits).
   - Adding a 64-bit binary value representing the original message length.

   After padding, "hello" becomes a 512-bit block.

2. **Breaking into Blocks**: Since our padded message is already 512 bits, it forms a single block. Longer messages are split into multiple 512-bit blocks.

### Step 3: Initialize Hash Values
SHA-256 uses 8 predefined 32-bit constants (denoted H0 to H7). These are derived from the first 32 bits of the fractional parts of the square roots of the first 8 prime numbers.

### Step 4: Process the Message Block
1. The algorithm processes the message in 64 rounds. Each round involves specific mathematical operations, like bitwise shifts, logical operations (AND, OR, XOR), and modular additions.
2. Predefined constants (called K values) and a "message schedule" are used in these rounds.

### Step 5: Update Hash Values
The output from each round updates the 8 hash values (H0 to H7).

### Step 6: Output the Hash
After processing all message blocks, the final hash values (H0 to H7) are concatenated to produce the final hash. For "hello" using SHA-256, the output hash is:

```
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

This is the cryptographic hash of "hello"! 


---

## Example 2

It's important to preface this by saying that MD5 is now considered cryptographically weak and should not be used for security-sensitive applications. 

However, for educational purposes, here's a simplified breakdown of the MD5 process on the word "hello":

**Understanding MD5 Basics**

* **Hash Function:** MD5 is a one-way hash function. This means it takes input (a message) and produces a fixed-size output (a hash), but you can't easily reverse the process to get the original message from the hash.
* **128-bit Hash:** MD5 always produces a 128-bit hash value, typically represented as a 32-character hexadecimal number.
* **Padding:** The input message is padded to ensure its length is a multiple of 512 bits.
* **Initialization:** The algorithm starts with four initial 32-bit values.
* **Processing in Blocks:** The padded message is processed in 512-bit blocks.
* **Rounds of Operations:** Each block goes through a series of rounds involving bitwise operations, additions, and rotations.

**Simplified Steps for "hello"**

1.  **Padding:**
    * The word "hello" is converted to its ASCII representation.
    * Padding is added to this binary representation to make its length a multiple of 512 bits. This involves adding a "1" bit, followed by "0" bits, and then the original message length.

2.  **Initialization:**
    * MD5 uses four 32-bit initialization values (these are constants).

3.  **Processing Blocks:**
    * The padded message is divided into 512-bit blocks.
    * Each block is processed through four rounds of operations. These rounds involve:
        * Bitwise logical operations (AND, OR, XOR, NOT).
        * Modular additions.
        * Left bit rotations.
        * The use of predefined constants.

4.  **Final Hash:**
    * After all blocks are processed, the results are combined to produce the 128-bit MD5 hash.
    * The resulting 128 bit hash is then displayed as a 32 character hexadecimal string.

**Result**

* The MD5 hash of "hello" is: 5d41402abc4b2a76b9719d911017c592

**Important Notes:**

* This explanation is highly simplified. The actual MD5 algorithm is much more complex.
* MD5 is vulnerable to collision attacks, meaning it's possible to find two different messages that produce the same hash. This makes it unsuitable for security purposes.
* Modern hashing algorithms such as SHA-256, and SHA-3 are much more secure.



