# Lecture 19: Key Establishment

## Introduction

In modern cryptographic systems, one of the most critical challenges we face is not the encryption algorithms themselves, but rather the secure establishment and management of cryptographic keys. This lecture focuses on key establishment protocols, their implementation, and security considerations.

## Learning Objectives

By the end of this lecture, students will be able to:
- Understand the fundamental concepts of key establishment and its importance in cryptographic systems
- Explain the n² key distribution problem and its implications
- Describe key transport protocols and their implementation
- Comprehend the role and functionality of Key Distribution Centers (KDC)
- Analyze security considerations in symmetric key establishment
- Understand and implement the Kerberos authentication protocol
- Evaluate the limitations and challenges of KDC-based approaches

## 1. Background Context to Key Establishment

Key establishment refers to the processes and protocols by which cryptographic keys are shared between two or more parties who wish to communicate securely. There are two main methods of key establishment:

1. **Key Transport**: One party creates the key and securely transfers it to other parties
2. **Key Agreement**: All parties contribute information to derive a shared secret key

The choice between these methods depends on various factors including:
- The security requirements of the system
- The computational capabilities of the parties involved
- The network infrastructure available
- The trust relationships between parties

## 2. The n² Key Distribution Problem

In symmetric key cryptography, each pair of communicating parties needs a unique shared key. For a network with n parties, the total number of keys needed is:

```
Total keys = n(n-1)/2
```

For example:
- With 10 users: 45 keys needed
- With 100 users: 4,950 keys needed
- With 1000 users: 499,500 keys needed

This quadratic growth in key requirements presents significant challenges:
- Key storage becomes impractical
- Key distribution becomes complex
- Key updates become time-consuming
- Security risks increase with each additional key

# 2.1 A note on E() notation

You may have noticed the notation E(K, M) in the lecture slides and other references. This notation is commonly used in cryptography to represent encryption operations.

In cryptographic notation, E(K, M) means "encrypt message M using key K". Let me break this down with a simple example:

Let's say Alice wants to send the message "Hello" to Bob using a shared key "abc123". In standard notation, we would write this as:

```
E("abc123", "Hello")
```

When we write more complex protocols like in the lecture, we use additional notation:
- || means concatenation (joining strings together)
- [x || y] means x and y are concatenated before encryption

Here's a practical example of sending a message with a timestamp:

```
Original message: "Hello"
Timestamp: "2024-02-12"
Key: "abc123"

Written in notation:
E("abc123", ["Hello" || "2024-02-12"])
```

This means we:
1. First join "Hello" and "2024-02-12" together
2. Then encrypt the combined string using the key "abc123"

Let's look at one of the protocol examples from the lecture:
```
A → B: E(K_AB, [ID_A || K || T])
```

This means:
1. Take three pieces of information:
   - ID_A (Alice's identifier, maybe "ALICE")
   - K (a new key, maybe "xyz789")
   - T (a timestamp, maybe "2024-02-12")
2. Concatenate them: ["ALICE" || "xyz789" || "2024-02-12"]
3. Encrypt the whole thing using key K_AB (the shared key between A and B)

This notation helps us understand complex cryptographic protocols more clearly.

Next, we'll dive into key transport protocols and how they work.

## 3. Key Transport

Key transport involves the secure transfer of a key from one party to another. This process must ensure:
- Confidentiality of the key during transmission
- Authentication of the sender
- Integrity of the key
- Protection against replay attacks

### 3.1 Key Transport Protocols

A basic key transport protocol follows this general structure:

```
A → B: E(K_AB, [ID_A || K || T])
```

Where:
- K_AB is a pre-existing shared key
- ID_A is the identifier of party A
- K is the new key being transported
- T is a timestamp or nonce
- || represents concatenation
- E() represents symmetric encryption

## 4. Key Establishment Using Symmetric Key Techniques

Symmetric key establishment techniques rely on trusted third parties to facilitate secure key distribution between communicating parties.

### 4.1 Key Distribution Centre (KDC) Protocol

The KDC protocol involves three parties:
1. Party A (initiator)
2. Party B (target)
3. KDC (trusted third party)

Basic KDC Protocol Steps:

```
1. A → KDC: [ID_A || ID_B || N1]
2. KDC → A: E(K_A-KDC, [K_S || ID_B || N1 || E(K_B-KDC, [K_S || ID_A])])
3. A → B: E(K_B-KDC, [K_S || ID_A])
```

Where:
- K_S is the session key
- K_A-KDC is the key shared between A and KDC
- K_B-KDC is the key shared between B and KDC
- N1 is a nonce

### 4.2 Modified KDC Protocol

To reduce communication overhead, the protocol can be modified:

```
1. A → KDC: [ID_A || ID_B || N1]
2. KDC → A: E(K_A-KDC, [K_S || ID_B || N1 || Ticket])
   where Ticket = E(K_B-KDC, [K_S || ID_A || Timestamp])
3. A → B: [Ticket]
```

This modification:
- Reduces the number of messages
- Improves efficiency
- Maintains security properties

## 5. Security of Symmetric Key Establishment Techniques

### 5.1 Passive vs. Non-Passive Attacks

#### Passive Attacks:
- Eavesdropping on key establishment messages
- Traffic analysis
- No modification of messages

#### Non-Passive (Active) Attacks:
- Replay attacks
- Message modification
- Man-in-the-middle attacks
- Impersonation attacks

Example of a replay attack:
```
Attacker captures: A → B: E(K_AB, [K || T1])
Later replays: Attacker → B: E(K_AB, [K || T1])
```

### 5.2 Key Confirmation Attack

In this attack, an adversary attempts to verify guessed keys:

1. Adversary captures encrypted message
2. Guesses potential key K'
3. Attempts decryption with K'
4. Verifies if result matches expected format

Prevention measures:
- Use of random padding
- Implementation of secure key derivation functions
- Addition of integrity checks

## 6. Kerberos Authentication System

Kerberos is a network authentication protocol that uses ticket-based authentication to allow nodes communicating over a non-secure network to prove their identity securely.

### 6.1 Kerberos Implementation Example

Step-by-step implementation:

```
# 1. Authentication Service Exchange
Client → AS: ID_C || ID_TGS || Time1

AS → Client: E(K_C, [K_C-TGS || ID_TGS || Time2 || Lifetime2 || Ticket_TGS])
where Ticket_TGS = E(K_TGS, [K_C-TGS || ID_C || ADC || ID_TGS || Time2 || Lifetime2])

# 2. Ticket-Granting Service Exchange
Client → TGS: ID_V || Ticket_TGS || Authenticator_C

TGS → Client: E(K_C-TGS, [K_C-V || ID_V || Time4 || Ticket_V])
where Ticket_V = E(K_V, [K_C-V || ID_C || ADC || ID_V || Time4 || Lifetime4])

# 3. Client/Server Authentication Exchange
Client → Server: Ticket_V || Authenticator_C

Server → Client: E(K_C-V, [Time5 + 1]) (optional)
```

Key components:
- AS: Authentication Server
- TGS: Ticket Granting Server
- K_C: Client's secret key
- K_C-TGS: Session key for Client and TGS
- K_C-V: Session key for Client and Server
- ADC: Client's network address

## 7. Problems with the KDC Approach

Several limitations exist with the KDC approach:

1. **Single Point of Failure**
   - If KDC is compromised, all keys are compromised
   - System availability depends on KDC availability

2. **Scalability Issues**
   - KDC must maintain keys for all users
   - Performance bottleneck for large networks

3. **Trust Requirements**
   - All parties must trust the KDC completely
   - KDC has access to all session keys

4. **Cross-Domain Authentication**
   - Difficult to implement across different administrative domains
   - Requires trust relationships between KDCs

## Conclusion

Key establishment remains a crucial aspect of cryptographic systems. While symmetric key techniques offer efficient solutions for closed networks, they face significant challenges in large-scale deployments. Understanding these protocols, their security implications, and their limitations is essential for designing and implementing secure systems.

## References

1. Menezes, A. J., Van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.

2. Kaufman, C., Perlman, R., & Speciner, M. (2002). Network Security: Private Communication in a Public World. Prentice Hall.

3. MIT Kerberos Consortium. (2021). Kerberos: The Network Authentication Protocol. Retrieved from https://web.mit.edu/kerberos/

4. Boyd, C., & Mathuria, A. (2003). Protocols for Authentication and Key Establishment. Springer-Verlag.

5. NIST Special Publication 800-56A Rev. 3. (2018). Recommendation for Pair-Wise Key Establishment Schemes Using Discrete Logarithm Cryptography.

---
*Note: This lecture material is designed for third-year B.Sc. Cyber Security students and covers approximately two hours of lecture time.*