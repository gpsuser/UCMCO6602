# Merkel Trees and Hash functions

## Introduction
A **Merkle tree** is a binary tree structure that is used to store hashes of data blocks in a way that allows for efficient and secure verification of the contents of individual blocks. It is a fundamental component of blockchain technology, enabling efficient verification of large data sets.

In this explanation, we'll cover the basic concepts of Merkle trees and how they are used in blockchain technology. We'll also discuss hash functions, which are essential for generating the hash values used in Merkle trees.

## Hash Functions

Lets assume we have a naive hash function that performs the following steps:

1. Convert the input data into binary form.
2. Perform a bitwise XOR operation with a constant mask.
3. Calculate the modulus of the result with a prime number.
4. Apply a mixing function (e.g., left circular shift).
5. Pad the result to a fixed bit length.

This function is a simplified version of a real-world hash function, but it demonstrates the basic principles involved in hashing data.

## Example: Hashing the Number 25

Let’s now work through a simple example of hashing the number `25` as the input to our naive hash function, aiming for a final 256-bit hash.

---

### Step 1: Input in Binary
We start by converting the number `25` into its binary form. In an unsigned 32-bit representation:

```
25 (decimal) = 0000 0000 0000 0000 0000 0000 0001 1001 (binary, 32 bits)
```

This is already padded to 32 bits, so no additional padding is needed.

---

### Step 2: Bitwise Operation
For the bitwise XOR operation, we use the same constant mask:

```
Mask = 1010 1010 1010 1010 1010 1010 1010 1010 (32 bits)
```

Perform the XOR (^) operation between the input and the mask:

```
Input:      0000 0000 0000 0000 0000 0000 0001 1001
Mask:       1010 1010 1010 1010 1010 1010 1010 1010
---------------------------------------------------
Result:     1010 1010 1010 1010 1010 1010 1011 1011
```

This results in an intermediate 32-bit binary value after the XOR.

---

### Step 3: Modular Arithmetic
Next, we convert the result from the XOR step into decimal form for the modulus calculation:

```
1010 1010 1010 1010 1010 1010 1011 1011 (binary) = 2863311531 (decimal)
```

Now, calculate the modulus of this value with the prime number `251`:

```
2863311531 % 251 = 55
```

Convert the result (`55`) back to binary, padding it to 32 bits:

```
55 (decimal) = 0000 0000 0000 0000 0000 0000 0011 0111 (binary, 32 bits)
```

---

### Step 4: Mixing Function
To mix the data further, we apply a **left circular shift** (rotate left) by 5 bits:

```
Original:      0000 0000 0000 0000 0000 0000 0011 0111
Rotate Left 5: 0000 0000 0000 0000 0000 0110 1110 1000
```

This gives us the new 32-bit binary value after the mixing step.

---

### Step 5: Padding to 256 Bits
Finally, we need to pad the 32-bit result to 256 bits. As before, we repeat the 32-bit value 8 times to achieve this:

```
0000 0000 0000 0000 0000 0110 1110 1000
0000 0000 0000 0000 0000 0110 1110 1000
0000 0000 0000 0000 0000 0110 1110 1000
0000 0000 0000 0000 0000 0110 1110 1000
0000 0000 0000 0000 0000 0110 1110 1000
0000 0000 0000 0000 0000 0110 1110 1000
0000 0000 0000 0000 0000 0110 1110 1000
0000 0000 0000 0000 0000 0110 1110 1000
```

Combine these into one 256-bit binary value.

---

### Final 256-Bit Hash
In hexadecimal format (for readability), the final hash looks like:

```
00006E8 00006E8 00006E8 00006E8 
00006E8 00006E8 00006E8 00006E8
```

---

This detailed process shows how the binary components interact through each stage of the naive hash function. If you'd like to tweak this function or explore further, let me know!

Next we consider obtaining the hash of a hash - given that this is a common operation in Merkle trees.

## Hashing the Hash

In a Merkle tree, each leaf node contains the hash of a data block. To build the tree, we hash pairs of nodes together until we reach the root node, which represents the entire data set.

When hashing the hash values, we follow the same process as before, but with a few key differences:

1. The input data is now the hash value itself.
2. The hash function remains the same, but the input is the hash value from the previous step.

Let’s walk through an example of hashing the hash we generated earlier (of the number `25`).

## Example: Hashing the Hash

To generate a hash of the hash we just produced (let’s call it the "input hash"), we’ll essentially treat the 256-bit value as our new input and apply a naive hashing algorithm again. Below, I'll outline a step-by-step approach for hashing this input hash in detail.

---

### Step 1: Input Hash Representation
The input hash we generated earlier was:

```
00006E8 00006E8 00006E8 00006E8 
00006E8 00006E8 00006E8 00006E8
```

This is already in a 256-bit form. We’ll represent it in binary:

```
00000000000000000000011011101000 (32 bits, repeated 8 times)
```

So, the entire binary input hash is:

```
00000000000000000000011011101000
00000000000000000000011011101000
00000000000000000000011011101000
00000000000000000000011011101000
00000000000000000000011011101000
00000000000000000000011011101000
00000000000000000000011011101000
00000000000000000000011011101000
```

This forms our new input.

---

### Step 2: Bitwise Operation
Let’s perform a **bitwise operation** on this input hash. We’ll apply **XOR** with another fixed mask. Let’s use the mask:

```
Mask = 11111111111111111111111111111111 (32 bits)
```

We’ll XOR this mask with each 32-bit segment of the input hash. For example:

```
Input Segment: 00000000000000000000011011101000
Mask:          11111111111111111111111111111111
------------------------------------------------
Result:        11111111111111111111100100010111
```

Repeating this XOR operation for all 8 segments gives us:

```
11111111111111111111100100010111
11111111111111111111100100010111
11111111111111111111100100010111
11111111111111111111100100010111
11111111111111111111100100010111
11111111111111111111100100010111
11111111111111111111100100010111
11111111111111111111100100010111
```

---

### Step 3: Modular Arithmetic
Next, we’ll perform modular arithmetic on the entire hash. First, we convert each 32-bit segment of the XOR result to decimal. For one segment:

```
11111111111111111111100100010111 (binary) = 4294966935 (decimal)
```

Let’s calculate the modulus of this value with a prime number, say `257`:

```
4294966935 % 257 = 114
```

We repeat this calculation for all 8 segments, which will result in the same value (`114`) for each since the input is repeated. Convert `114` back to binary:

```
114 (decimal) = 00000000000000000000000001110010 (binary)
```

So, after modular arithmetic, our new hash is:

```
00000000000000000000000001110010
00000000000000000000000001110010
00000000000000000000000001110010
00000000000000000000000001110010
00000000000000000000000001110010
00000000000000000000000001110010
00000000000000000000000001110010
00000000000000000000000001110010
```

---

### Step 4: Mixing Function
Now, we perform a **mixing operation** to further scramble the data. We’ll use a left circular shift (rotate left) by 7 bits on each 32-bit segment:

```
Original:      00000000000000000000000001110010
Rotate Left 7: 00000000000000000000111001000000
```

This operation is repeated for all 8 segments, resulting in:

```
00000000000000000000111001000000
00000000000000000000111001000000
00000000000000000000111001000000
00000000000000000000111001000000
00000000000000000000111001000000
00000000000000000000111001000000
00000000000000000000111001000000
00000000000000000000111001000000
```

---

### Step 5: Padding to 256 Bits
Since our result is already 256 bits, no additional padding is required.

---

### Final Hash
The final hash of the input hash is:

```
00003800 00003800 00003800 00003800 
00003800 00003800 00003800 00003800
```

This is the output of the naive hashing algorithm applied to the hash of `25`.

---

## Conclusion

This detailed process demonstrates how we can hash a hash using a naive approach. The same principles apply to more complex hash functions used in real-world applications. 

We now have an initial understanding as to how this pattern may be applied to Merkle trees in blockchain technology.

