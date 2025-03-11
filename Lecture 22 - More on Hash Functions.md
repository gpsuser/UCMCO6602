# Cryptography: Lecture 22
# Hash Functions and Message Authentication Codes

## Introduction

Hash functions represent one of the fundamental building blocks of modern cryptography. While encryption algorithms focus on confidentiality, hash functions provide integrity checking, allowing us to verify that data has not been modified. This lecture explores the properties and applications of cryptographic hash functions, their design principles, and their role in message authentication.

Hash functions take an input message of arbitrary length and produce a fixed-length output called a hash value or digest. This transformation is deterministic, meaning the same input will always produce the same output. However, cryptographic hash functions are designed to make it computationally infeasible to find two different inputs that produce the same output, a property that makes them invaluable for data integrity verification, password storage, digital signatures, and many other security applications.

Today's session will examine the theoretical foundations of hash functions, explore several prominent hash algorithms including MD4 and the SHA family, and discuss how hash functions can be constructed from block ciphers. The lecture will conclude with an exploration of Message Authentication Codes (MACs) and their relationship to hash functions.

## Learning Objectives

By the end of this lecture, students should be able to:

1. Identify and explain the key properties of cryptographic hash functions
2. Understand the concept and design of dedicated hash functions
3. Describe the structure and operation of MD4 and the SHA family of hash functions
4. Explain how hash functions can be constructed from block ciphers
5. Analyze the detailed workings of the SHA-1 algorithm
6. Define Message Authentication Codes and their security properties
7. Compare different approaches to constructing MACs using hash functions
8. Understand the structure and security properties of HMAC

## 1. Properties of Hash Functions

A cryptographic hash function maps binary strings of arbitrary length to binary strings of fixed length, called hash values, message digests, or simply hashes. For a hash function to be cryptographically secure, it must satisfy several essential properties:

### 1.1 Pre-image Resistance (One-way Property)

For a given hash value h, it should be computationally infeasible to find any message m such that hash(m) = h. This property ensures that even if an attacker obtains a hash value, they cannot determine the original input that produced it.

Mathematically, given h, it should be difficult to find any m such that:
h = hash(m)

### 1.2 Second Pre-image Resistance (Weak Collision Resistance)

Given an input m₁, it should be computationally infeasible to find another input m₂ ≠ m₁ such that hash(m₁) = hash(m₂). This property prevents an attacker from substituting one message for another without detection.

Mathematically, given m₁, it should be difficult to find any m₂ ≠ m₁ such that:
hash(m₁) = hash(m₂)

### 1.3 Collision Resistance (Strong Collision Resistance)

It should be computationally infeasible to find any pair of distinct inputs m₁ and m₂ such that hash(m₁) = hash(m₂). This is a stronger property than second pre-image resistance because the attacker is free to choose both inputs.

Mathematically, it should be difficult to find any m₁ ≠ m₂ such that:
hash(m₁) = hash(m₂)

### 1.4 Avalanche Effect

A small change in the input (even a single bit) should produce a significant change in the output hash value. Ideally, each output bit should change with a probability of 0.5 when a single input bit is flipped. This property helps ensure that even small modifications to the input are readily detectable.

### 1.5 Deterministic

For the same input, the hash function must always produce the same output.

### 1.6 Efficiency

The hash function should be computationally efficient, making it practical to calculate the hash value for any given input.

| Property | Description | Security Implication |
|----------|-------------|----------------------|
| Pre-image Resistance | Cannot find m given h = hash(m) | Protects against reversal attacks |
| Second Pre-image Resistance | Given m₁, cannot find m₂ such that hash(m₁) = hash(m₂) | Prevents document forgery |
| Collision Resistance | Cannot find any m₁ ≠ m₂ such that hash(m₁) = hash(m₂) | Prevents birthday attacks |
| Avalanche Effect | Small input changes cause significant output changes | Ensures sensitivity to input modifications |
| Deterministic | Same input always produces same output | Ensures consistency and reliability |
| Efficiency | Computation is reasonably fast | Ensures practical usability |

## 2. Dedicated Hash Functions

A dedicated hash function is a function specifically designed from the ground up to serve as a cryptographic hash function, as opposed to being derived from another cryptographic primitive like a block cipher. These functions are engineered specifically to satisfy the security properties required for hash functions while optimizing for performance.

### 2.1 Design Principles

Dedicated hash functions typically follow these design principles:

1. **Compression Construction**: Most dedicated hash functions use an iterative structure that processes the input message in fixed-sized blocks, compressing each block into an internal state using a compression function.

2. **Merkle-Damgård Construction**: Many dedicated hash functions, including MD4, MD5, and the SHA family, use the Merkle-Damgård construction. This approach:
   - Divides the input message into fixed-size blocks
   - Processes each block sequentially with a compression function
   - Maintains an internal state between block processing
   - Applies appropriate padding to ensure the message length is a multiple of the block size
   - Appends the message length at the end (length strengthening)

3. **Wide Pipe Construction**: Some modern hash functions use a wide pipe approach where the internal state size is larger than the final hash output, providing increased security against certain types of attacks.

### 2.2 Advantages of Dedicated Hash Functions

Dedicated hash functions offer several advantages:

1. **Optimization**: They can be optimized specifically for hashing operations, often resulting in better performance than hash functions derived from other primitives.

2. **Security Focus**: Their design can focus exclusively on the security properties required for hash functions without compromises needed for other cryptographic uses.

3. **Flexibility**: They can implement novel design techniques specifically suited to hashing rather than adapting techniques from other cryptographic domains.

### 2.3 Examples of Dedicated Hash Functions

- **MD4/MD5** family
- **SHA** family (SHA-1, SHA-2, SHA-3)
- **RIPEMD** family
- **Whirlpool**
- **BLAKE2** and **BLAKE3**

## 3. MD4 (Message Digest Algorithm 4)

MD4 is a cryptographic hash function designed by Ron Rivest in 1990. While now considered insecure and obsolete for cryptographic applications, understanding MD4 is valuable because it forms the foundation for many subsequent hash functions, including MD5, SHA-1, and RIPEMD.

### 3.1 Specifications

- **Input**: Message of arbitrary length
- **Output**: 128-bit (16-byte) hash value
- **Block Size**: 512 bits (64 bytes)
- **Word Size**: 32 bits (4 bytes)

### 3.2 MD4 Algorithm Structure

The MD4 algorithm follows these steps:

1. **Padding**: The message is padded so its length is congruent to 448 modulo 512. Padding consists of a single '1' bit followed by enough '0' bits to reach the required length.

2. **Length Appending**: A 64-bit representation of the original message length is appended, making the total padded message length a multiple of 512 bits.

3. **Buffer Initialization**: Four 32-bit registers (A, B, C, D) are initialized with specific constants:
   - A = 0x67452301
   - B = 0xEFCDAB89
   - C = 0x98BADCFE
   - D = 0x10325476

4. **Message Processing**: The message is processed in 512-bit blocks. Each block undergoes three rounds of processing, with each round containing 16 operations.

### 3.3 MD4 Compression Function

The compression function processes each 512-bit block in three rounds, with each round applying a different nonlinear function:

1. **Round 1 Function F(x, y, z) = (x AND y) OR ((NOT x) AND z)**
2. **Round 2 Function G(x, y, z) = (x AND y) OR (x AND z) OR (y AND z)**
3. **Round 3 Function H(x, y, z) = x XOR y XOR z**

Each round consists of 16 operations that update the four registers using a specific message word, a nonlinear function, and a left circular rotation.

### 3.4 Security Status of MD4

MD4 is now considered completely broken:
- Collisions can be found in less than a second on modern computers
- The first full collision attack was published by Hans Dobbertin in 1996
- Various cryptanalytic techniques, including differential cryptanalysis, have been successfully applied to break MD4

Despite its obsolescence, MD4's influence on hash function design makes it an important algorithm to study in cryptography courses.

## 4. The SHA Family (Secure Hash Algorithms)

The Secure Hash Algorithm (SHA) family comprises a series of cryptographic hash functions designed by the National Security Agency (NSA) and published by the National Institute of Standards and Technology (NIST). The family has evolved over time to address security concerns and changing requirements.

### 4.1 SHA-0 and SHA-1

- **SHA-0**: Published in 1993, it was quickly withdrawn due to a significant flaw.
- **SHA-1**: Published in 1995 as a replacement for SHA-0, producing a 160-bit hash value.
  - Designed to be used with the Digital Signature Standard (DSS)
  - Widely deployed throughout the 1990s and 2000s
  - Now deprecated due to theoretical attacks that were later practically demonstrated

### 4.2 SHA-2 Family

The SHA-2 family, introduced in 2001, includes:

- **SHA-224**: Produces a 224-bit hash value
- **SHA-256**: Produces a 256-bit hash value
- **SHA-384**: Produces a 384-bit hash value
- **SHA-512**: Produces a 512-bit hash value
- **SHA-512/224 and SHA-512/256**: Variants of SHA-512 with truncated outputs

SHA-2 algorithms share a similar structure but differ in word size, number of rounds, and message block size:

| Algorithm | Word Size | Rounds | Message Block Size | Hash Size |
|-----------|-----------|--------|-------------------|-----------|
| SHA-224/256 | 32 bits | 64 | 512 bits | 224/256 bits |
| SHA-384/512 | 64 bits | 80 | 1024 bits | 384/512 bits |

The SHA-2 family has demonstrated good security properties, though they share some structural similarities with SHA-1.

### 4.3 SHA-3 (Keccak)

SHA-3 represents a significant departure from the previous SHA algorithms:

- Selected through a public competition run by NIST (2007-2012)
- Based on the Keccak algorithm designed by Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche
- Uses a sponge construction rather than the Merkle-Damgård construction
- Offers the same output sizes as SHA-2: 224, 256, 384, and 512 bits
- Designed to be resistant to attacks that work against SHA-2
- Computationally different from SHA-1 and SHA-2, providing algorithm diversity

### 4.4 Comparison of SHA Family Members

| Feature | SHA-1 | SHA-256 | SHA-512 | SHA-3-256 |
|---------|-------|---------|---------|-----------|
| Output Size | 160 bits | 256 bits | 512 bits | 256 bits |
| Block Size | 512 bits | 512 bits | 1024 bits | 1088 bits (rate) |
| Word Size | 32 bits | 32 bits | 64 bits | 64 bits |
| Rounds | 80 | 64 | 80 | 24 |
| Construction | Merkle-Damgård | Merkle-Damgård | Merkle-Damgård | Sponge |
| Security Status | Broken | Secure | Secure | Secure |
| Speed | Fastest | Medium | Slowest | Medium |

## 5. Constructing Hash Functions from Block Ciphers

Block ciphers can be used to construct cryptographic hash functions. This approach leverages the security properties of well-established encryption algorithms to create hash functions with provable security characteristics.

### 5.1 Theoretical Approaches

Several constructions can transform a block cipher into a hash function:

1. **Davies-Meyer Construction**: h_i = E(m_i, h_{i-1}) ⊕ h_{i-1}
   - The message block is used as the encryption key
   - The previous hash value is both encrypted and XORed with the result

2. **Matyas-Meyer-Oseas Construction**: h_i = E(h_{i-1}, m_i) ⊕ m_i
   - The previous hash value is used as the encryption key
   - The message block is both encrypted and XORed with the result

3. **Miyaguchi-Preneel Construction**: h_i = E(h_{i-1}, m_i) ⊕ m_i ⊕ h_{i-1}
   - Combines aspects of both previous constructions
   - Adds an extra XOR with the previous hash value

### 5.2 Worked Example: Davies-Meyer Construction with AES

Let's construct a simple hash function using the Davies-Meyer construction with AES-128 as the underlying block cipher.

**Step 1**: Initialize the hash value (H₀)
- Choose an initialization vector (IV), typically a fixed constant
- For this example, we'll use H₀ = 0000000000000000 (in hexadecimal)

**Step 2**: Prepare the message
- Pad the message to ensure it's a multiple of the block size
- Divide the padded message into blocks M₁, M₂, ..., Mₙ of 128 bits each

**Step 3**: Process each message block
- For each block Mᵢ (i = 1 to n):
  - Use the message block Mᵢ as the AES key
  - Encrypt the previous hash value H_{i-1} using this key
  - XOR the encryption result with H_{i-1} to get the new hash value Hᵢ
  - Hᵢ = AES(Mᵢ, H_{i-1}) ⊕ H_{i-1}

**Worked Example**:
Let's say we have two message blocks after padding:
- M₁ = 000102030405060708090A0B0C0D0E0F (hex)
- M₂ = 101112131415161718191A1B1C1D1E1F (hex)

Starting with H₀ = 0000000000000000:

1. For M₁:
   - Encrypt H₀ using M₁ as key: AES(M₁, H₀) = 7DF76B0C1AB899B33E42F047B91B546F
   - H₁ = 7DF76B0C1AB899B33E42F047B91B546F ⊕ 0000000000000000 = 7DF76B0C1AB899B33E42F047B91B546F

2. For M₂:
   - Encrypt H₁ using M₂ as key: AES(M₂, H₁) = 9E4BC1E0C497C8610ADBF71F144C1D0F
   - H₂ = 9E4BC1E0C497C8610ADBF71F144C1D0F ⊕ 7DF76B0C1AB899B33E42F047B91B546F = E3BC8AEC7E2F51D234997748A5D7C560

The final hash value is H₂ = E3BC8AEC7E2F51D234997748A5D7C560.

### 5.3 Advantages and Disadvantages

**Advantages**:
- Leverages the security properties of well-studied block ciphers
- May have provable security properties related to the underlying cipher
- Can reuse existing hardware or software implementations of block ciphers

**Disadvantages**:
- Often slower than dedicated hash functions
- Block size limitations of the cipher affect the construction
- May require more processing power for the same level of security

## 6. SHA-1 Algorithm

SHA-1 (Secure Hash Algorithm 1) was designed by the NSA and published by NIST in 1995. It produces a 160-bit (20-byte) hash value and was widely used until vulnerabilities were discovered. While now deprecated for security applications, understanding its design provides valuable insights into hash function construction.

### 6.1 SHA-1 Initial Hash Value

SHA-1 initializes five 32-bit registers with the following hexadecimal values:
- H₀ = 67452301
- H₁ = EFCDAB89
- H₂ = 98BADCFE
- H₃ = 10325476
- H₄ = C3D2E1F0

These values represent the initial state of the hash before any message blocks are processed.

### 6.2 SHA-1 Padding

The padding process ensures that the message length is congruent to 448 modulo 512 bits:

1. Append a '1' bit to the end of the message
2. Append '0' bits until the message length is congruent to 448 modulo 512
3. Append the original message length as a 64-bit big-endian integer

This padding ensures that the message can be processed in complete 512-bit blocks and incorporates the message length as a security measure (length strengthening).

### 6.3 SHA-1 Message Schedule

For each 512-bit message block, SHA-1 derives 80 32-bit words (W₀ through W₇₉) as follows:

1. Divide the 512-bit block into sixteen 32-bit words W₀ through W₁₅
2. For t = 16 to 79:
   - Wₜ = (W_{t-3} ⊕ W_{t-8} ⊕ W_{t-14} ⊕ W_{t-16}) ≪ 1

Where ≪ 1 denotes a left circular shift by 1 bit.

The message schedule expands the 16 original words into 80 words used in the compression function, introducing diffusion in the algorithm.

### 6.4 SHA-1 Compression Function

The compression function processes each message block to update the hash state. For each block:

1. Initialize working variables with the current hash value:
   - a = H₀
   - b = H₁
   - c = H₂
   - d = H₃
   - e = H₄

2. Apply 80 rounds of processing (detailed in section 6.5)

3. Update the hash value:
   - H₀ = a + H₀
   - H₁ = b + H₁
   - H₂ = c + H₂
   - H₃ = d + H₃
   - H₄ = e + H₄

All additions are performed modulo 2³².

### 6.5 SHA-1 Compression Rounds

The 80 rounds of processing are divided into four groups of 20 rounds each. Each group uses a different logical function (F) and constant (K):

| Rounds | Function F(b,c,d) | Constant K (hex) |
|--------|-------------------|------------------|
| 0-19 | (b AND c) OR ((NOT b) AND d) | 5A827999 |
| 20-39 | b XOR c XOR d | 6ED9EBA1 |
| 40-59 | (b AND c) OR (b AND d) OR (c AND d) | 8F1BBCDC |
| 60-79 | b XOR c XOR d | CA62C1D6 |

These operations provide the nonlinearity necessary for the security of the hash function.

### 6.6 SHA-1 Individual Round

Each round t (0 ≤ t ≤ 79) performs the following operations:

1. T = (a ≪ 5) + F(b,c,d) + e + K + W_t
2. e = d
3. d = c
4. c = b ≪ 30
5. b = a
6. a = T

Where:
- ≪ denotes a left circular shift
- F is the round function determined by the round number
- K is the round constant determined by the round number
- W_t is the message word for the round
- All additions are performed modulo 2³²

## 7. Message Authentication Codes (MACs)

Message Authentication Codes (MACs) are cryptographic techniques used to verify both the integrity and authenticity of a message. Unlike hash functions, which only verify integrity, MACs incorporate a secret key to provide authentication.

### 7.1 Definition and Purpose

A MAC is a function that takes two inputs—a message and a secret key—and produces a fixed-size output called a tag or MAC value. This tag serves as a cryptographic checksum that can only be verified by someone who possesses the same secret key.

The primary purposes of MACs are:

1. **Data Integrity**: To verify that the message has not been altered during transmission
2. **Authentication**: To confirm that the message originated from the claimed sender who possesses the secret key
3. **Non-repudiation** (in certain contexts): To prevent the sender from denying having sent the message

### 7.2 Basic MAC Operation

The MAC process involves two main operations:

1. **MAC Generation**:
   - The sender computes MAC = MAC_Algorithm(K, M) where K is the secret key and M is the message
   - The sender transmits both the message M and the MAC value

2. **MAC Verification**:
   - The receiver computes MAC' = MAC_Algorithm(K, M) using the received message and the shared secret key
   - The receiver compares MAC' with the received MAC value
   - If MAC' = MAC, the message is both authentic and unaltered

### 7.3 Types of MACs

Several approaches can be used to construct MACs:

1. **Hash-based MAC (HMAC)**: Uses cryptographic hash functions
2. **Cipher-based MAC (CMAC)**: Uses block ciphers
3. **One-time MAC**: Uses universal hash functions and is information-theoretically secure
4. **Polynomial MAC**: Based on polynomial evaluation, such as GMAC

## 8. Properties of Message Authentication Codes (MACs)

To be effective security tools, MACs must satisfy several important properties:

### 8.1 Security Properties

1. **Computation Resistance**:
   - It should be computationally infeasible to compute a valid MAC value without knowledge of the secret key, even with access to a large number of message-MAC pairs.

2. **Verification Resistance**:
   - Given a message and its MAC value, it should be computationally infeasible to verify the MAC without knowledge of the secret key.

3. **Key Non-recovery**:
   - Given one or more message-MAC pairs, it should be computationally infeasible to recover the secret key.

4. **Collision Resistance**:
   - It should be computationally infeasible to find two different messages that produce the same MAC value with the same key.

### 8.2 Functional Properties

1. **Deterministic**:
   - For the same message and key, the MAC algorithm must always produce the same output.

2. **Efficient Computation**:
   - The MAC algorithm should be computationally efficient for both generation and verification.

3. **Variable Input Length**:
   - The MAC algorithm should accept messages of arbitrary length.

4. **Fixed Output Length**:
   - The MAC algorithm should produce a fixed-length output regardless of input length.

### 8.3 Attack Models

MACs should be secure against various attack scenarios:

1. **Known-message Attack**:
   - The attacker has access to a set of messages and their corresponding MAC values.

2. **Chosen-message Attack**:
   - The attacker can choose messages and obtain their MAC values from the legitimate sender.

3. **Adaptive Chosen-message Attack**:
   - The attacker can choose messages adaptively based on previously obtained MACs.

4. **Key Recovery Attack**:
   - The attacker attempts to discover the secret key.

5. **Forgery Attack**:
   - The attacker attempts to generate a valid MAC for a message without knowing the key.

## 9. Generating MACs Using Cryptographic Hash Functions

Hash functions can be adapted to create MACs by incorporating a secret key into the hashing process. These constructions leverage the security properties of cryptographic hash functions while adding the authentication provided by secret keys.

### 9.1 Advantages of Hash-Based MACs

1. **Reuse of Existing Code**: Implementations of cryptographic hash functions are widely available and well-tested.

2. **Performance**: Hash functions are generally faster than symmetric encryption algorithms.

3. **Security Analysis**: The security properties of hash functions are well-studied, providing a foundation for analyzing the security of the MAC.

4. **No Export Restrictions**: In some jurisdictions, hash functions may face fewer export restrictions than encryption algorithms.

### 9.2 General Approaches

There are several approaches to constructing MACs from hash functions, with different security properties:

1. **Secret Prefix Method**: MAC(K, M) = Hash(K || M)
2. **Secret Suffix Method**: MAC(K, M) = Hash(M || K)
3. **Envelope Method**: MAC(K, M) = Hash(K || M || K)
4. **HMAC**: A standardized construction described in section 12

Each approach has different security characteristics and vulnerabilities.

## 10. MAC Secret Prefix

The secret prefix method is one of the simplest ways to construct a MAC using a hash function. In this approach, the secret key is prepended to the message before hashing.

### 10.1 Definition

MAC(K, M) = Hash(K || M)

Where:
- K is the secret key
- M is the message
- || denotes concatenation
- Hash is a cryptographic hash function (e.g., SHA-256)

### 10.2 Operation

1. The sender concatenates the secret key K with the message M
2. The sender computes the hash of this concatenated value
3. The sender sends the message M along with the computed hash value
4. The receiver, who knows K, performs the same computation and compares the result

### 10.3 Security Considerations

While simple, the secret prefix method has significant vulnerabilities:

1. **Length Extension Attacks**:
   - For hash functions based on the Merkle-Damgård construction (like MD5, SHA-1, SHA-2), an attacker who knows Hash(K || M) can compute Hash(K || M || padding || X) for any X without knowing K
   - This allows the attacker to forge MACs for messages that are extensions of legitimate messages

2. **Collision Attacks**:
   - If the underlying hash function is vulnerable to collision attacks, an attacker might find M and M' such that Hash(K || M) = Hash(K || M')
   - This would allow message forgery even without knowing the key

Due to these vulnerabilities, especially the length extension attack, the secret prefix method is not recommended for practical applications.

## 11. MAC Secret Suffix

The secret suffix method is another simple approach to constructing a MAC using a hash function. In this method, the secret key is appended to the message before hashing.

### 11.1 Definition

MAC(K, M) = Hash(M || K)

Where:
- K is the secret key
- M is the message
- || denotes concatenation
- Hash is a cryptographic hash function

### 11.2 Operation

1. The sender concatenates the message M with the secret key K
2. The sender computes the hash of this concatenated value
3. The sender sends the message M along with the computed hash value
4. The receiver, who knows K, performs the same computation and compares the result

### 11.3 Security Considerations

The secret suffix method addresses the length extension vulnerability of the secret prefix method since an attacker cannot perform a length extension attack without knowing K. However, it has other vulnerabilities:

1. **Collision Attacks**:
   - If collisions can be found in the underlying hash function, an attacker might find M and M' such that Hash(M) = Hash(M')
   - This could lead to Hash(M || K) = Hash(M' || K) for some messages, allowing forgery

2. **Hash Function Weaknesses**:
   - For certain hash functions with specific weaknesses, it might be possible to construct forgeries even without finding full collisions
   - For example, some attacks on early hash functions allowed for the computation of Hash(M || X) given Hash(M) for certain values of X

While more resistant to length extension attacks than the secret prefix method, the secret suffix method still has security concerns that make it unsuitable for high-security applications.

## 12. HMAC (Hash-based Message Authentication Code)

HMAC is a specific construction for creating a MAC from a cryptographic hash function. It was designed to address the weaknesses of simpler constructions like the secret prefix and secret suffix methods. HMAC is standardized in RFC 2104 and FIPS 198.

### 12.1 HMAC Construction

The HMAC algorithm is defined as:

HMAC(K, M) = Hash((K' ⊕ opad) || Hash((K' ⊕ ipad) || M))

Where:
- K is the secret key
- K' is the derived key (K padded to the block size of the hash function)
- M is the message
- || denotes concatenation
- ⊕ denotes bitwise XOR
- Hash is a cryptographic hash function
- opad is the outer padding (0x5c repeated to form a block)
- ipad is the inner padding (0x36 repeated to form a block)

### 12.2 HMAC Algorithm Steps

1. **Key Preparation**:
   - If K is longer than the block size, hash it: K = Hash(K)
   - If K is shorter than the block size, pad it with zeros to the right

2. **Inner Hash Computation**:
   - XOR K' with ipad to create the inner padded key
   - Concatenate the result with the message M
   - Compute the hash of this concatenation: Inner_Hash = Hash((K' ⊕ ipad) || M)

3. **Outer Hash Computation**:
   - XOR K' with opad to create the outer padded key
   - Concatenate the result with the Inner_Hash
   - Compute the hash of this concatenation: HMAC = Hash((K' ⊕ opad) || Inner_Hash)

### 12.3 Security Properties of HMAC

HMAC has several important security advantages:

1. **Resistance to Length Extension Attacks**:
   - The nested hash structure prevents length extension attacks that affect simple hash-based MAC constructions

2. **Proven Security**:
   - HMAC's security can be proven under reasonable assumptions about the underlying hash function
   - It remains secure even if the hash function is only weakly collision-resistant

3. **Key Separation**:
   - The use of different paddings (ipad and opad) ensures that the keys used in the inner and outer hash operations are effectively different

4. **Widespread Adoption and Analysis**:
   - HMAC has undergone extensive cryptanalysis and is widely used in security protocols such as TLS, IPsec, and SSH

### 12.4 HMAC Implementation Example (Pseudocode)

```
function HMAC(key, message, hash_function, block_size, output_size)
    // Compute inner hash
    inner = hash_function(i_key_pad + message)
    
    // Compute outer hash (the HMAC result)
    result = hash_function(o_key_pad + inner)
    
    return result
end function
```

### 12.5 HMAC Applications

HMAC is widely used in security protocols and standards:

1. **Transport Layer Security (TLS)**: Used for message authentication in secure web communications
2. **IPsec**: Used for authentication in secure network communications
3. **SSH**: Used for data integrity verification
4. **JSON Web Tokens (JWT)**: Used for token signature and verification
5. **API Authentication**: Used in many RESTful APIs for request authentication
6. **Blockchain Technologies**: Used in various cryptocurrency implementations

### 12.6 HMAC vs. Other MAC Constructions

| MAC Type | Security | Performance | Key Management | Resistance to Collision Attacks |
|----------|----------|-------------|---------------|--------------------------------|
| HMAC | High | Good | Single key | Strong |
| CMAC | High | Moderate | Single key | Strong |
| Secret Prefix | Low | Excellent | Single key | Weak |
| Secret Suffix | Moderate | Excellent | Single key | Moderate |
| GMAC | High | Excellent | Key and nonce | Strong |

## Conclusion

This lecture has explored the fundamental concepts of cryptographic hash functions and their application in message authentication codes. We've examined the essential properties that make hash functions valuable for security applications, including pre-image resistance, collision resistance, and the avalanche effect. The journey through specific hash algorithms—from MD4 to the SHA family—illustrates the evolution of hash function design and the ongoing effort to address emerging security threats.

We've also seen how hash functions can be constructed from block ciphers, providing an alternative approach with different security properties. The detailed examination of SHA-1, though now deprecated, offers valuable insights into the internal workings of modern hash algorithms and the design principles that guide their development.

The latter part of the lecture focused on message authentication codes, which extend hash functions to provide not only integrity but also authenticity. The progression from simple constructions like the secret prefix and suffix methods to the more robust HMAC demonstrates how cryptographic primitives evolve to address identified vulnerabilities.

As future cybersecurity professionals, it's crucial to understand both the theoretical foundations of these cryptographic tools and their practical applications. The security of many systems relies on the appropriate selection and implementation of hash functions and MACs, making this knowledge essential for designing secure systems and for analyzing potential vulnerabilities in existing ones.

Remember that cryptography is a rapidly evolving field. While the fundamental principles discussed in this lecture remain valid, specific algorithms may become obsolete as computational power increases and new cryptanalytic techniques emerge. Staying informed about current standards and recommendations is an essential practice for any cybersecurity professional.

## References

Bellare, M., Canetti, R. and Krawczyk, H. (1996) 'Keying hash functions for message authentication', in Koblitz, N. (ed.) *Advances in Cryptology — CRYPTO '96*. Berlin, Heidelberg: Springer Berlin Heidelberg, pp. 1-15.

Dobbertin, H. (1996) 'The Status of MD5 After a Recent Attack', *CryptoBytes*, 2(2), pp. 1-6.

Federal Information Processing Standards Publication 180-4 (2015) *Secure Hash Standard (SHS)*. Gaithersburg, MD: National Institute of Standards and Technology.

Federal Information Processing Standards Publication 198-1 (2008) *The Keyed-Hash Message Authentication Code (HMAC)*. Gaithersburg, MD: National Institute of Standards and Technology.

Katz, J. and Lindell, Y. (2020) *Introduction to Modern Cryptography*. 3rd edn. Boca Raton: CRC Press.

Paar, C. and Pelzl, J. (2010) *Understanding Cryptography: A Textbook for Students and Practitioners*. Berlin, Heidelberg: Springer Berlin Heidelberg.

Preneel, B. (2010) 'Hash Functions and MAC Algorithms Based on Block Ciphers', in Avanzi, R., Keliher, L. and Sica, F. (eds.) *Selected Areas in Cryptography*. Berlin, Heidelberg: Springer Berlin Heidelberg, pp. 248-250.

Rivest, R. (1992) *The MD4 Message Digest Algorithm*, RFC 1320. Internet Engineering Task Force.

Rivest, R. (1992) *The MD5 Message-Digest Algorithm*, RFC 1321. Internet Engineering Task Force.

Stevens, M., Bursztein, E., Karpman, P., Albertini, A. and Markov, Y. (2017) 'The first collision for full SHA-1', in Katz, J. and Shacham, H. (eds.) *Advances in Cryptology – CRYPTO 2017*. Cham: Springer International Publishing, pp. 570-596.

Wang, X., Yin, Y.L. and Yu, H. (2005) 'Finding Collisions in the Full SHA-1', in Shoup, V. (ed.) *Advances in Cryptology – CRYPTO 2005*. Berlin, Heidelberg: Springer Berlin Heidelberg, pp. 17-36.