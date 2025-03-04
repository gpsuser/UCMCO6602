# Lecture 16 - RSA Asymmetric Encryption

## Introduction 

In today's lecture, we will be exploring the world of RSA asymmetric encryption. 

As you may recall from our previous discussions, asymmetric encryption, also known as public key cryptography, is a cryptographic system that uses pairs of keys: public keys for encryption and private keys for decryption. 

RSA, named after its inventors Rivest, Shamir, and Adleman, is one of the first and most widely used public-key cryptosystems. It has been a cornerstone of secure communication over the internet, enabling technologies like HTTPS, SSH, and secure email.

Throughout this lecture, we will delve into the mathematical foundations of RSA, understand how it works in practice, and even implement our own RSA encryption scheme in Python. By the end of this session, you should have a solid grasp of RSA and its role in modern cryptography.

## Learning Objectives

- Understand the concept of one-way functions and their role in public key cryptography
- Compare and contrast public key, symmetric, and hybrid encryption schemes
- Understand the basics of public-key cryptanalysis, including brute force and probable message attacks
- Explain the RSA encryption and decryption process with examples
- Implement RSA encryption in Python, including key generation and fast exponentiation
- Discuss techniques to speed up RSA operations

## 1. Practical Aspects of Public Key Cryptography

Public key cryptography, as the name suggests, involves the use of public and private keys. Let's start by understanding some of the fundamental concepts that make this possible.

### 1.1 One Way Functions

A one-way function is a function that is easy to compute on every input, but hard to invert given the image of a random input. One-way functions are fundamental to public-key cryptography.

#### 1.1.1 Integer Factorization Problem

The integer factorization problem is a classic example of a one-way function. Given a composite number n, finding its prime factors is believed to be computationally difficult. This is the basis of the security of RSA.

### 1.2 Suitability of the Choice of Cipher

When designing a cryptographic system, the choice of cipher is critical. Here's a comparison of the different types:

| Cipher Type | Key Management | Computational Efficiency | Typical Use Cases |
|-------------|----------------|--------------------------|-------------------|
| Symmetric   | Single shared key | Very efficient | Bulk data encryption |  
| Public Key  | Separate public and private keys | Computationally expensive | Key exchange, digital signatures |
| Hybrid      | Combination of symmetric and public key | Balances efficiency and key management | SSL/TLS, PGP |

In practice, hybrid systems that use public key cryptography for key exchange and symmetric encryption for bulk data are most common.

## 2. Public-Key Cryptanalysis 

Just as with symmetric ciphers, public-key systems are vulnerable to cryptanalysis. Let's look at a couple of common attacks.

### 2.1 Brute Force

In a brute force attack, the attacker tries all possible private keys until they find one that works. The security of a public-key system depends on the computational infeasibility of this approach.

### 2.2 Probable Message Attacks

If the attacker has some knowledge or can guess the likely content of the encrypted message, they can use this to their advantage. For example, in RSA, if the attacker knows that the message is of the form "The password is...", they can encrypt all possible passwords with the public key and compare the results to the intercepted ciphertext.

## 3. RSA

Now let's dive into the specifics of the RSA cryptosystem.

### 3.1 The Encryption Challenge

The problem that RSA solves can be stated as follows:

```
Given: Encryption key (n, e)
Plaintext message: M (0 <= M < n)

Find: Ciphertext C such that:
C ≡ M^e (mod n)
```

### 3.2 RSA Encryption 

The encryption process in RSA is straightforward:

```
C = M^e mod n
```

Here, `(n, e)` is the public key. `M` is the plaintext message, and `C` is the resulting ciphertext.

#### 3.2.1 Example

Let's work through a small example:

```
Public Key: (n = 33, e = 7)
Message: M = 20

Ciphertext: C ≡ 20^7 (mod 33)
              ≡ 14
```

### 3.3 RSA Decryption

Decryption in RSA involves the use of the private key `(n, d)`:

```
M = C^d mod n
```

Here, `C` is the ciphertext, `d` is the private exponent, and `M` is the recovered plaintext.

#### 3.3.1 Example

Continuing our previous example:

```
Private Key: (n = 33, d = 3)
Ciphertext: C = 14

Message: M ≡ 14^3 (mod 33)
           ≡ 20
```

### 3.4 Practical Steps for Implementing RSA

In practice, implementing RSA involves the following steps:

1. Generate the public and private keys
   - Choose two large prime numbers `p` and `q`
   - Calculate `n = p * q`
   - Calculate `φ(n) = (p-1) * (q-1)`
   - Choose `e` such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`
   - Calculate `d ≡ e^(-1) (mod φ(n))`
   - Public key is `(n, e)`, private key is `(n, d)`
2. Encryption
   - Convert the message `M` into an integer `m`, where `0 <= m < n`
   - Calculate ciphertext `c ≡ m^e (mod n)`
3. Decryption
   - Use private key `(n, d)` to compute `m ≡ c^d (mod n)`
   - Convert `m` back into the plaintext message `M`

### 3.5 RSA Key Generation

The security of RSA depends on the proper generation of keys.

#### 3.5.1 Example

Here's an example of RSA key generation in Python:

```python
from Crypto.PublicKey import RSA

key = RSA.generate(2048)
public_key = key.publickey()

print(f"Public key:  (n={hex(public_key.n)}, e={hex(public_key.e)})")
print(f"Private key: (n={hex(public_key.n)}, d={hex(key.d)})")
```

This will output something like:

```
Public key:  (n=0x9d66c28df6c8d8a327d2efd66974927623fc25d8ed29c34f3acfca0efe132b235ed82feb5ce255fa307ac2aff87a17e54af893c3a0b107b3f524d36af611c89503edc766e623440c151d200b3d63a0a5e04dc1777e4506d0d87a1faab8d1fa15cac4933b42f81ff33f2ce81f7a03c17529e43bab1fa20bde556382ab5a49a3a15, e=0x10001)
Private key: (n=0x9d66c28df6c8d8a327d2efd66974927623fc25d8ed29c34f3acfca0efe132b235ed82feb5ce255fa307ac2aff87a17e54af893c3a0b107b3f524d36af611c89503edc766e623440c151d200b3d63a0a5e04dc1777e4506d0d87a1faab8d1fa15cac4933b42f81ff33f2ce81f7a03c17529e43bab1fa20bde556382ab5a49a3a15, d=0x25a554dbdb75d6d06c512fa706e6a03ac1cea6d6f6e1f6a0cf59a4fb8c564eea824001ac5e115c19d17e29b33a187f6b33ad8059d3481c4b3ed84b9dfeee92a41186b3c9d6c5a4e4c79bce6943a2c209fdcf5ea3c3e225feb2de488b9747b7d24ef52e50b0ab8604f216e09366b17507a14072af516dbe104758e3d6bffd2e9341)
```

## 4. Fast Exponentiation

One potential bottleneck in RSA is the need to compute large exponentials like `m^e mod n`. However, this can be sped up using a technique known as fast exponentiation.

The idea is to use the binary representation of the exponent. For each '1' in the binary, we multiply the current result with the base. For each '0', we square the base.

### 4.1 Example

Let's compute `3^23 mod 17` using fast exponentiation:

```
23 in binary is 10111

3^23 mod 17 ≡ 3^(10111) mod 17
            ≡ 3^(10000) * 3^(0100) * 3^(0010) * 3^(0001) mod 17
            ≡ ((((1^2 * 3)^2)^2 * 3)^2 * 3)^2 * 3 mod 17
            ≡ 11
```

Here's the Python code for fast modular exponentiation:

```python
def fast_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result
```

## 5. Speed Up Techniques for RSA

While RSA is inherently slower than symmetric ciphers, there are techniques to speed it up:

- Use small public exponents (e.g., 3, 17, 65537)
- Use the Chinese Remainder Theorem (CRT) for decryption
- Use Montgomery multiplication for modular arithmetic
- Implement in hardware (e.g., smart cards, dedicated chips)

These optimizations, combined with appropriate key sizes, make RSA practical for many applications.

## Secure Messaging with RSA

Let's consider a simple secure messaging system that uses RSA for encryption. Here's how it would work:

1. Key Generation:
   - Alice generates her RSA public and private keys
   - Bob generates his RSA public and private keys
2. Key Exchange:
   - Alice sends her public key to Bob
   - Bob sends his public key to Alice
3. Secure Messaging:
   - When Alice wants to send a message to Bob:
     - She encrypts the message with Bob's public key
     - She signs the message with her private key
   - When Bob receives the message:
     - He verifies the signature using Alice's public key
     - He decrypts the message with his private key

Here's some Python code that demonstrates this end to end encryption/decryption  process - using python libraries:

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt(message, pub_key):
    rsa_key = RSA.importKey(pub_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)
    encrypted = rsa_key.encrypt(message)
    return encrypted

def decrypt(ciphertext, priv_key):
    rsa_key = RSA.importKey(priv_key)
    rsa_key = PKCS1_OAEP.new(rsa_key)
    decrypted = rsa_key.decrypt(ciphertext)
    return decrypted

def sign(message, priv_key):
    rsa_key = RSA.importKey(priv_key)
    signer = pkcs1_15.new(rsa_key)
    digest = SHA256.new()
    digest.update(message)
    sign = signer.sign(digest)
    return sign

def verify(message, signature, pub_key):
    rsa_key = RSA.importKey(pub_key)
    signer = pkcs1_15.new(rsa_key)
    digest = SHA256.new()
    digest.update(message)
    try:
        signer.verify(digest, signature)
        return True
    except (ValueError, TypeError):
        return False

# Example usage
alice_private, alice_public = generate_keys()
bob_private, bob_public = generate_keys()

message = b'Hello, Bob! This is a secure message from Alice.'
encrypted_message = encrypt(message, bob_public)
signature = sign(message, alice_private)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, bob_private)
print(f"Decrypted Message: {decrypted_message}")

if verify(decrypted_message, signature, alice_public):
    print("Signature verified!")
else:
    print("Signature verification failed.")
```

output:

```
Original Message: b'Hello, Bob! This is a secure message from Alice.'
Encrypted Message: b'\x03\xd1e\x1fL\x01\xfc\xdb\x0f\x86\xdb\xe0\xe3\xd6\x97+.\xfe\xf2 \xfb\xad6\xe4\xf7+\xd7\x8d\xfb#qBB\x9a~\x91\xb0U\xcd\x9c\xb8\x9c\xed\xeb\x10Kh\xb7\xdc\xdd7\xeeG|h\xe9\x84\x1cP\xb4\xe9\t\xbaVU#\xa3\x04u\xd5K\\:\xeb\x8c\x87C\xd1\x0f*w\xb2\x85\xb3k\xeb\xbb[:8\x0f%+\xbdEG\xee\x15\x1d\x12\xcc>\x90\x07\xca\xc6\x8aO\xb3\x10<M\n\x83\x8c\xcb\x98\xec\xd6\x1f_3\xa4$3\xfc\xd2\xd0\xca\xe0r\xe5\xc2\x92\xb6\xe2\xabZpG\xcb\x91\xe6\xc5y\r`b\xaa?6@O\x08\xb4\xda\xaf\x92w\xcf\x86\x94\xe0\xef\xbc\x16\xc5N\xebq\x9e\x92\xa7RD\x99\xaci\x88\xe4\xb3\xe4\xb5\xd5\xfb\x0fP\xa9\x07\xe7\xb5p\x93\xd6\x9b5\xa6\xa1\x82\xccVH4P\xda\xf4g\xe8\xb7^X\xd2\xd9\x1b#\xbfse\x01&\xa6\x9a\xec\xdc\xe2\x92\xee\xb9\xcd\xf8\xe9\x00k\xb6\r\x1fl^>\x87\xf4\xf9\xe6\xfd\xb9G\x87\xa8\xdf\xd2X\xa7\x10\xd0\xda#'
Decrypted Message: b'Hello, Bob! This is a secure message from Alice.'
Signature verified!
```

Next we consider a python implementation of encryption - without using pre-baked python libraries.

The code demonstrates the complete flow of secure messaging using RSA. In practice, you would also need to consider things like user interfaces, key management, and network protocols. But this gives you a good idea of the cryptographic core of such a system.


#### Recap: First Principles of RSA

Key Generation:

Select two large prime numbers (let's call them p and q)
Calculate n = p × q
Calculate φ(n) = (p-1) × (q-1)
Choose public exponent e that is:

Coprime with φ(n)
Usually chosen as 65537 (a prime number)


Calculate private exponent d where:

d × e ≡ 1 (mod φ(n))
Found using extended Euclidean algorithm




Public Key:

Consists of (n, e)
n is the modulus
e is the encryption exponent


Encryption Process:

Convert message M to number m (where m < n)
Calculate ciphertext: c = m^e mod n



Now - let's implement this in Python, focusing on the encryption part.


### Illustrative RSA implementation in python - simplified

```python
import math
from typing import Tuple

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_pair(min_value: int, max_value: int) -> Tuple[int, int]:
    """Generate two distinct prime numbers within a range."""
    primes = [num for num in range(min_value, max_value) if is_prime(num)]
    if len(primes) < 2:
        raise ValueError("Range too small to find two distinct primes")
    p = primes[0]
    q = primes[1]
    return p, q

def calculate_phi(p: int, q: int) -> int:
    """Calculate Euler's totient function φ(n)."""
    return (p - 1) * (q - 1)

def gcd(a: int, b: int) -> int:
    """Calculate Greatest Common Divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def generate_public_key(min_value: int = 100, max_value: int = 1000) -> Tuple[int, int]:
    """
    Generate public key components (n, e).
    Returns tuple of (n, e) where:
    n is the modulus
    e is the public exponent
    """
    # Generate prime numbers
    p, q = generate_prime_pair(min_value, max_value)
    
    # Calculate modulus
    n = p * q
    
    # Calculate φ(n)
    phi = calculate_phi(p, q)
    
    # Choose public exponent e
    # We'll use 65537 if it's suitable, otherwise find another one
    e = 65537
    if e >= phi:
        # Find a smaller e that is coprime with phi
        e = 3
        while e < phi:
            if gcd(e, phi) == 1:
                break
            e += 2
    
    return n, e

def encrypt_message(message: int, public_key: Tuple[int, int]) -> int:
    """
    Encrypt a message using RSA public key.
    
    Args:
        message: Integer representation of message (must be < n)
        public_key: Tuple of (n, e)
    
    Returns:
        Encrypted message (ciphertext)
    """
    n, e = public_key
    if message >= n:
        raise ValueError("Message too large for given key")
    
    # Perform RSA encryption: c = m^e mod n
    ciphertext = pow(message, e, n)
    return ciphertext

# Example usage
def main():
    # Generate public key
    public_key = generate_public_key(100, 1000)
    n, e = public_key
    print(f"Generated public key:")
    print(f"Modulus (n): {n}")
    print(f"Public exponent (e): {e}")
    
    # Encrypt a message
    message = 42  # Simple message for demonstration
    print(f"\nOriginal message: {message}")
    
    encrypted_message = encrypt_message(message, public_key)
    print(f"Encrypted message: {encrypted_message}")

if __name__ == "__main__":
    main()
```

#### Output:

```
Generated public key:
Modulus (n): 10403
Public exponent (e): 7

Original message: 42
Encrypted message: 295
```


### Key Assumptions and Limitations:

* We're using relatively small prime numbers for demonstration (in practice, you'd use much larger primes)
The message must be converted to an integer smaller than n

* We're implementing textbook RSA without padding (in practice, you'd use proper padding schemes like PKCS#1)
This is for educational purposes - in real applications, you should use established cryptographic libraries

### Important Security Notes:

This is a basic implementation for learning purposes
Real-world RSA implementations need:

* Secure prime number generation
* Proper padding schemes
* Much larger key sizes (typically 2048 or 4096 bits)
* Protection against timing attacks
* Protection against other cryptographic attacks


For production use, you should use established cryptographic libraries like pycryptodome or Python's built-in cryptography library rather than implementing RSA yourself.

## Conclusion

In this lecture, we've explored the RSA cryptosystem in depth. We've seen how it uses one-way functions and the integer factorization problem to enable secure public-key encryption. We've also looked at the practical aspects of implementing RSA, including key generation, encryption, decryption, and optimizations.

RSA remains a cornerstone of modern cryptography and is widely used in many secure communication protocols. However, it's important to remember that the security of RSA depends on proper implementation and sufficiently large key sizes.

As you continue your studies in cryptography, I encourage you to experiment further with RSA and other public-key cryptosystems. Understanding these foundational techniques will serve you well as you explore more advanced topics and applications.

## References

- Rivest, R. L., Shamir, A., & Adleman, L. (1978). A method for obtaining digital signatures and public-key cryptosystems. Communications of the ACM, 21(2), 120-126.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms. MIT press.
- Schneier, B. (1996). Applied cryptography: protocols, algorithms, and source code in C. John Wiley & Sons.