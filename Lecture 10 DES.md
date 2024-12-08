# Lecture 10 - Data Encryption Standard (DES) and Feistel Ciphers

## Introduction

Today's lecture is on the Data Encryption Standard (DES) and Feistel Ciphers. These fundamental concepts in cryptography have shaped modern encryption methods and continue to influence contemporary cryptographic designs. While DES itself is no longer considered secure for modern applications, understanding its architecture and the Feistel structure provides insight and intuition behind block cipher design.

In this session, we'll explore the theoretical foundations of Feistel ciphers, examine their practical implementations, and study how these concepts were applied in DES. We'll also look at Triple DES as an evolution of the original standard.

## 1. Feistel Cipher Overview

### Historical Context

The Feistel cipher structure, developed by Horst Feistel at IBM in the early 1970s, revolutionised block cipher design. Its balanced approach to encryption and decryption made it particularly attractive for hardware implementation.

### Description

A Feistel cipher is a symmetric structure used in block cipher construction. It transforms an input block through multiple rounds of processing, with each round using a portion of the encryption key (subkey).

### Key Characteristics

- **Encryption/Decryption Symmetry**: The same structure is used for both operations
- **Round Function Flexibility**: The F-function can be any operation
- **Guaranteed Reversibility**: Decryption is always possible regardless of the F-function

### Guidelines for Use

- Implement with sufficient rounds (typically 16 or more)
- Use strong round functions
- Ensure proper key scheduling
- Maintain key secrecy

### Strengths

- Encryption and decryption are structurally identical
- Simple to implement in hardware
- Proven security properties with sufficient rounds
- Flexible round function design

### Weaknesses

- Requires multiple rounds for security
- Potentially slower than non-Feistel designs
- Vulnerable to slide attacks if round keys are similar

## 2. Feistel Cipher Structure

### Basic Architecture

The Feistel structure divides each input block into two equal halves:

```
Input Block (2n bits)
       ↓
 +------------+------------+
 |  Left (n)  | Right (n) |
 +------------+------------+
       ↓           ↓
```

### Round Structure

Each round performs the following operations:

1. Right half goes through the round function (F) with the subkey
2. Result is XORed with the left half
3. Sides are swapped (except in the final round)

```python
def feistel_round(left, right, subkey, round_function):
    """Single round of Feistel cipher"""
    new_left = right
    new_right = left ^ round_function(right, subkey)
    return new_left, new_right
```

## 3. Feistel Cipher Design Elements

### Structural Parameters

Parameter | Typical Values | Considerations
----------|---------------|---------------
Block Size | 64-128 bits | Balance between security and efficiency
Key Size | 128-256 bits | Must resist brute force attacks
Number of Rounds | 16-32 | More rounds increase security but reduce speed
Round Function | Non-linear | Must provide confusion and diffusion

### Subkey Generation Algorithm

- Must generate unique subkeys for each round
- Should maximize differences between round keys
- Must be efficiently computable

### Round Function Requirements

- Non-linearity
- Avalanche effect
- Bit independence
- Computational efficiency

## 4. Feistel Cipher Deep Dive

### Implementation Example

Let's implement a simplified 16-bit Feistel cipher:

```python
def simple_round_function(right_half, subkey):
    """Simple round function for demonstration"""
    # Rotate right by 2 and XOR with subkey
    rotated = ((right_half >> 2) | (right_half << 6)) & 0xFF
    return rotated ^ subkey

class SimpleFeistel:
    def __init__(self, num_rounds=8):
        self.num_rounds = num_rounds
    
    def generate_subkeys(self, master_key):
        """Generate subkeys from master key"""
        subkeys = []
        for i in range(self.num_rounds):
            # Simple key schedule for demonstration
            subkey = (master_key >> (i * 2)) & 0xFF
            subkeys.append(subkey)
        return subkeys
    
    def encrypt(self, plaintext, master_key):
        # Split 16-bit plaintext into two 8-bit halves
        left = (plaintext >> 8) & 0xFF
        right = plaintext & 0xFF
        
        subkeys = self.generate_subkeys(master_key)
        
        for i in range(self.num_rounds):
            left, right = right, left ^ simple_round_function(right, subkeys[i])
            
        # Final swap and combine
        return (right << 8) | left

    def decrypt(self, ciphertext, master_key):
        # Split 16-bit ciphertext
        left = (ciphertext >> 8) & 0xFF
        right = ciphertext & 0xFF
        
        subkeys = self.generate_subkeys(master_key)
        
        for i in range(self.num_rounds - 1, -1, -1):
            left, right = right, left ^ simple_round_function(right, subkeys[i])
            
        return (right << 8) | left
```

### Example Usage

```python
# Example usage
cipher = SimpleFeistel(num_rounds=8)
plaintext = 0xABCD
key = 0x1234

encrypted = cipher.encrypt(plaintext, key)
decrypted = cipher.decrypt(encrypted, key)

print(f"Plaintext:  0x{plaintext:04X}")
print(f"Encrypted:  0x{encrypted:04X}")
print(f"Decrypted:  0x{decrypted:04X}")
```

## 5. Symmetric Block Encryption Algorithms

### Block Cipher Characteristics

- Fixed input block size
- Fixed output block size
- Key-dependent transformation
- Reversible operation

### Common Block Sizes

- 64-bit (legacy systems)
- 128-bit (modern standard)
- 256-bit (future-proof systems)

## 6. Data Encryption Standard (DES)

### Historical Context

DES was developed by IBM and standardized by NIST in 1977. It remained the global standard for symmetric encryption until the late 1990s.

### Basic Specifications

- 64-bit block size
- 56-bit effective key size (64-bit input with parity bits)
- 16 rounds Feistel structure
- Complex substitution-permutation network

## 7. DES Algorithm

### Description

DES processes 64-bit blocks through:
1. Initial permutation
2. 16 rounds of Feistel network
3. Final permutation

### Guidelines for Use

Modern recommendations:

- Use only in legacy systems
- Prefer Triple DES or AES for new applications
- Never use single DES for sensitive data

### Strengths

- Well-analyzed algorithm
- Fast hardware implementation
- Simple Feistel structure

### Weaknesses

- 56-bit key size (too small)
- Vulnerable to brute force attacks
- Known theoretical weaknesses

## 8. DES Algorithm Deep Dive

### Simplified DES Implementation

```python
class SimplifiedDES:
    # Initial and Final Permutation Tables (simplified)
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    FP = [4, 1, 3, 5, 7, 2, 8, 6]
    
    def __init__(self):
        self.subkeys = []
    
    def permute(self, block, table):
        """Permute input block using specified table"""
        return int(''.join(str((block >> (8-i)) & 1) for i in table), 2)
    
    def generate_subkeys(self, key):
        """Generate 16 subkeys from main key"""
        # Simplified key schedule for demonstration
        self.subkeys = [(key >> i) & 0xF for i in range(0, 56, 4)]
    
    def f_function(self, right_half, subkey):
        """Simplified f-function"""
        # Expansion
        expanded = ((right_half & 0xF) << 1) | ((right_half & 0x8) >> 3)
        # XOR with subkey
        xored = expanded ^ subkey
        # Simplified S-box
        return (xored ^ (xored >> 2)) & 0xF
    
    def encrypt_block(self, plaintext):
        """Encrypt a single 8-bit block"""
        # Initial permutation
        block = self.permute(plaintext, self.IP)
        
        # Split block
        left = (block >> 4) & 0xF
        right = block & 0xF
        
        # 16 rounds
        for i in range(16):
            new_left = right
            new_right = left ^ self.f_function(right, self.subkeys[i])
            left, right = new_left, new_right
        
        # Final permutation
        return self.permute((right << 4) | left, self.FP)
```

## 9. Triple DES

### Description

Triple DES (3DES) applies DES three times with different keys to increase security.

```
C = E(k3, D(k2, E(k1, P)))
```

### Guidelines for Use

- Use only in legacy systems
- Implement with three different keys
- Consider migration to AES

### Strengths

- Stronger than single DES
- Backwards compatible
- Well-understood security properties

### Weaknesses

- Slow (3x DES operations)
- Block size still 64 bits
- Complex key management

## Conclusion

Today we've explored the fundamental concepts of Feistel ciphers and their implementation in DES. While DES itself is no longer considered secure for modern applications, its structure and design principles continue to influence modern cryptographic systems. Understanding these concepts is crucial for:

- Analyzing modern block ciphers
- Implementing secure systems
- Evaluating cryptographic protocols

In following sessions, we'll examine more contemporary block ciphers, particularly AES, and how they've evolved from these foundational concepts.

### Key Takeaways

1. Feistel structures provide a flexible framework for block cipher design
2. DES implemented these principles effectively but with insufficient key length
3. Triple DES offered a temporary solution to DES's key length problem
4. Modern systems should use AES or other contemporary algorithms

### Further Reading

- "Applied Cryptography" by Bruce Schneier
- NIST Special Publication 800-67: Recommendation for Triple DES Block Cipher
- "The Design of Rijndael" by Joan Daemen and Vincent Rijmen

---

