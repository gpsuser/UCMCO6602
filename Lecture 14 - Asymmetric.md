# Lecture 14: Asymmetric (Public Key) Encryption

## Introduction 

Today we will be diving into the world of asymmetric, or public key, encryption. Asymmetric encryption is a cornerstone of modern cryptography and enables many of the secure communications and transactions we rely on every day. 

By the end of this lecture, you will have a solid grasp of how asymmetric encryption works, its various applications, and how it combines with other cryptographic primitives like hashing and digital signatures to enable secure systems.

## Learning Objectives

By the end of this lecture, you should be able to:

1. Explain the core concepts of asymmetric encryption, including public and private keys 
2. Understand the relationship between public and private keys and how they are used for encryption and decryption
3. Identify the main applications of asymmetric encryption, such as key exchange, digital signatures, and hybrid encryption
4. Describe how hash functions work and their important uses in cryptography  
5. Understand how digital signatures provide authentication and integrity
6. Explain the role of digital certificates and public key infrastructure (PKI) in establishing trust

## Asymmetric (Public Key) Encryption

### Core Concepts

Asymmetric encryption, also known as public key cryptography, is a cryptographic system that uses pairs of keys: public keys, which may be disseminated widely, and private keys, which are known only to the owner.

Imagine you have a special mailbox. Anyone who knows your address can put a letter in (that's the public key), but only you have the key to open it and read the contents (that's the private key). 

That's asymmetric encryption in a nutshell.


The beauty of this system is that it solves the age-old problem of how to securely exchange keys over an insecure channel. With symmetric encryption, where the same key is used to encrypt and decrypt, you'd need to find a secure way to get the key to your recipient. 

But with asymmetric encryption, all you need is their public key, which, as the name suggests, can be public knowledge.
Here's a high-level view of how it works:

---

Alice and Bob each generate a pair of public and private keys.
They exchange their public keys over an insecure network.

When Alice wants to send a secure message to Bob, she encrypts it using Bob's public key.

Bob receives the encrypted message and decrypts it with his private key.

Even if someone intercepts the encrypted message, they can't decrypt it without Bob's private key.

* This is the core principle that enables secure communication over the internet.

---

- **Asymmetric Keys**: In asymmetric encryption, keys come in related pairs consisting of a public key and private key. 

    * The public key, as the name suggests, can be freely shared with anyone. The private key must be kept secret by its owner.

- **Public Key Certificate**: A public key certificate is a digitally signed statement that binds a public key to the identity of its owner. 

    * It is issued by a trusted certificate authority (CA). This allows others to verify that a given public key genuinely belongs to a specific individual or organization.

- **Public Key Cryptographic Algorithms**: Asymmetric encryption relies on mathematical algorithms that have the property of being easy to compute in one direction but very difficult to reverse without knowing some secret. 

    * Common algorithms include RSA, Elliptic Curve Cryptography, and Diffie-Hellman.

- **Public Key Infrastructure (PKI)**: PKI is the combination of technologies, policies, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates and public keys. It provides the framework for establishing trust in public keys.

### Goal of Asymmetric Encryption

The main goal of asymmetric encryption can be summarized by the mnemonic PANIC:

- **P**rivacy: Ensuring only authorized parties can read the data 
- **A**uthentication: Verifying the identity of the communicating parties
- **N**on-repudiation: Providing proof of origin to prevent senders denying having sent a message
- **I**ntegrity: Detecting if data has been modified in transit
- **C**onfidentiality: Preventing unauthorized disclosure of information

### Principles of Asymmetric Encryption

The security of asymmetric encryption relies on a few key principles:

`One-way functions`: The mathematical operations used to generate the public and private keys are based on "one-way" functions. These are functions that are easy to compute in one direction but very difficult to reverse. It's easy to multiply two large prime numbers, but much harder to factor the product of two large primes. This is the basis of the RSA algorithm, one of the most widely used public key cryptosystems.

`Computationally infeasible to derive the private key`: Given a public key, it should be computationally infeasible to derive the corresponding private key. This is what keeps your private key private even if your public key is known to the world.

`Encrypt with public, decrypt with private`: Any message encrypted with a public key can only be decrypted by the corresponding private key. This is how you can send secure messages to someone even if you don't have a secure channel to exchange keys.

`Encrypt with private, decrypt with public (digital signatures)`: Conversely, any message encrypted (or more accurately, signed) with a private key can be decrypted with the corresponding public key. This doesn't provide confidentiality (since anyone with the public key can read the message), but it does provide authentication and integrity. If you can decrypt a message with Alice's public key, you know Alice sent it (authentication) and that it hasn't been altered (integrity). This is the basis for digital signatures.

---

- **Private Key**: The private key is kept secret by its owner and is used for decrypting messages encrypted with the corresponding public key or for creating digital signatures. 
- **Public Key**: The public key can be freely distributed and is used for encrypting messages destined for the owner of the corresponding private key, or for verifying digital signatures made by the private key.
- **Relationship Between Keys**: Public and private keys are mathematically related such that data encrypted by the public key can only be decrypted by the corresponding private key. However, it is computationally infeasible to determine the private key given only the public key.

#### Example: Asymmetric Encryption*

Let's consider a simple messaging scenario between Alice and Bob:

1. Bob generates a public-private key pair and sends his public key to Alice. 
2. Alice encrypts her message using Bob's public key and sends the encrypted message.
3. Bob uses his private key to decrypt Alice's message. 
The message was securely transferred because only Bob's private key could decrypt what was encrypted with his public key. Even if someone intercepted the encrypted message, they could not read it without Bob's closely guarded private key.

### Applications of Public Key Cryptosystems

Asymmetric encryption has a wide range of applications, including:

`Secure Communication`: As we've seen, asymmetric encryption enables secure communication over insecure channels. This is the foundation for protocols like HTTPS, which is used to secure web traffic.

- `Encryption/Decryption`: Providing confidentiality by encrypting with the public key and decrypting with the private key.

`Key Exchange`: Asymmetric encryption is often used to securely exchange symmetric keys, which are then used for bulk data encryption. This hybrid approach combines the convenience of asymmetric encryption with the speed of symmetric encryption.

Enabling secure exchange of symmetric keys over insecure channels. This is often used in hybrid cryptosystems.

`Digital Signatures`: Asymmetric encryption is the basis for digital signatures, which are used to verify the authenticity and integrity of messages, software, or digital documents.

Providing authentication and integrity by signing with the private key. The signature can be verified by anyone with the public key, ensuring it came from the owner of the private key.

`Email Security`: Protocols like PGP and S/MIME use asymmetric encryption to secure email communications.

`Cryptocurrencies`: Cryptocurrencies like Bitcoin and Ethereum use asymmetric encryption to prove ownership of funds and to sign transactions.

Public key cryptography has three main uses:


| Algorithm | Enc/Dec | Digital Signature | Key Exchange |
|-----------|---------|-------------------|--------------|
| RSA | Yes | Yes | Yes |
| ElGamal | Yes | Yes (variant) | Yes |
| DSA | No | Yes | No |
| Diffie-Hellman | No | No | Yes |
| ECC | Yes | Yes | Yes |

*Table 1: Asymmetric algorithms and their uses*

### Conditions for Public Key Cryptosystems

For a public key cryptosystem to be secure and practical, it must meet certain conditions:

1. It must be computationally infeasible to determine the private key from the public key. 
2. It must be computationally easy for the owner of the private key to generate the public and private keys.
3. It must be computationally easy for the sender, knowing the public key and the message, to generate the ciphertext.
4. It must be computationally easy for the receiver, knowing the private key and the ciphertext, to decrypt and recover the original message.
5. The two keys must be such that the private key cannot be deduced from knowledge of the public key.

### Key Exchange

One of the most important applications of asymmetric encryption is in solving the key distribution problem, i.e., how to securely exchange keys over an insecure network.

*Diffie-Hellman Key Exchange*

Diffie-Hellman key exchange, invented in 1976, was the first practical method for establishing a shared secret over an unsecured communication channel. It works as follows:

1. Alice and Bob agree on a large prime number `p` and a base `g` (a primitive root modulo `p`). These can be public.
2. Alice chooses a secret integer `a`, computes `A = g^a mod p`, and sends `A` to Bob.
3. Bob chooses a secret integer `b`, computes `B = g^b mod p`, and sends `B` to Alice.
4. Alice computes `s = B^a mod p`.
5. Bob computes `s = A^b mod p`.

Alice and Bob now share the secret `s`, which they can use as a key for symmetric encryption. An eavesdropper who knows `p`, `g`, `A`, and `B` cannot calculate `s` due to the computational difficulty of the discrete logarithm problem.

*Hybrid Encryption in HTTPS*

Most real-world cryptosystems, like those used in HTTPS, use hybrid encryption. Asymmetric encryption is used to securely exchange a symmetric key, which is then used to encrypt the actual communication data. This combines the convenience of public-key cryptography with the efficiency of symmetric-key cryptography. Here's a simplified view of how it works in a typical HTTPS session:

1. The client requests a secure page (usually https://).
2. The server sends its public key with its certificate.
3. The client verifies the certificate, generates a symmetric key, encrypts it with the server's public key, and sends it to the server.
4. The server decrypts the symmetric key using its private key.
5. The client and server now share a symmetric key. All communication is encrypted and decrypted using this key and a symmetric cipher like AES. 
6. To ensure integrity, messages include a hash (like SHA-256) of the contents encrypted with the symmetric key.

### Hashing

Hashing is another fundamental concept in cryptography. 

A hash function is a mathematical function that converts an input value into a compressed numerical value – the hash or hash value. They provide a way to check the integrity of data without needing to see the data itself. They are used in digital signatures, message authentication codes, password verification, and more

Here are the key principles of cryptographic hash functions:

`Fixed Size`: No matter the size of the input data, the output hash is always a fixed size. For example, SHA-256 always outputs a 256-bit hash.

`Deterministic`: The same input always produces the same output hash.

`Easy to compute`: Given an input, it's easy to calculate the hash value.

`Infeasible to reverse`: Given a hash value, it's infeasible to determine the original input. This is why hashes are sometimes described as "one-way" functions.

`Collision-resistant`: It's infeasible to find two inputs that produce the same hash output.
A hash collision occurs when two different inputs produce the same hash output. For a secure hash function, collisions should be extremely unlikely. Functions like SHA-256 are designed to be collision resistant.

---

These properties make hash functions incredibly useful in cryptography and cybersecurity:

`Data Integrity`: Changes to the input data will result in a different hash output, which makes hash functions useful for checking data integrity. This is used in file download checksums, blockchain integrity checks, and more.

`Password Storage`: When you create an account on a website, the site typically hashes your password before storing it. When you log in, the password you enter is hashed and compared to the stored hash. This way, even if the password database is compromised, the attacker doesn't get the actual passwords.

`Digital Signatures`: As part of creating a digital signature, the signer typically hashes the message and then encrypts the hash with their private key. This proves they had access to the private key and that the message hasn't changed.

`Blockchain`: In blockchain systems like Bitcoin, transactions are hashed and added to the block. The block header contains a hash of the previous block's header, chaining the blocks together. This, combined with the distributed nature of blockchain, provides immutability and prevents tampering.


#### Example: Hashing

Suppose Alice wants to send a message to Bob and have Bob be sure the message wasn't altered in transit.

1. Alice creates a hash of her message using a hash function like SHA-256. 
2. Alice sends her message along with the hash to Bob.
3. Bob receives the message and computes the hash of the received message using the same hash function.
4. Bob compares the computed hash to the hash Alice sent. If they match, Bob can be confident the message wasn't altered.

### Digital Signatures

Digital signatures provide authentication and integrity by allowing the sender to "sign" a message or document with their private key. The signature can then be verified by anyone who has access to the sender's public key.

*Creating a Digital Signature*

1. The sender creates a hash of their message.
2. The sender encrypts the hash with their private key. This is the digital signature.
3. The sender sends the message and the signature to the recipient.

*Verifying a Digital Signature*

1. The recipient creates a hash of the received message.
2. The recipient decrypts the signature using the sender's public key. This gives them the original hash.
3. The recipient compares the hash they computed to the hash from the signature. If they match, the signature is valid.

#### Example: Digital Signature

Suppose Bob wants to digitally sign a contract and send it to Alice.

1. Bob creates a hash of the contract using a hash function like SHA-256.
2. Bob encrypts the hash with his private key. This is his digital signature.
3. Bob sends the contract and his signature to Alice.
4. Alice creates a hash of the received contract.
5. Alice decrypts the signature using Bob's public key and gets the original hash.
6. Alice compares the hash she computed to the hash from the signature. If they match, she knows the contract came from Bob and hasn't been altered.

### Digital Certificates

A digital certificate is an electronic document used to prove ownership of a public key. The certificate includes information about the key, its owner's identity, and the digital signature of an entity that has verified the certificate's contents. If the signature is valid, and the person examining the certificate trusts the signer, then they know they can use that key to communicate with its owner.

#### Example: Digital Certificate

When you visit a secure website (one that uses https), your browser obtains the site's digital certificate. The certificate contains the site's public key, information about the site's identity, and a signature from a trusted certificate authority (CA). Your browser checks that the certificate is valid and has been signed by a CA it trusts. If everything checks out, it uses the public key in the certificate to set up a secure connection with the site.

## Case Study: Secure Messaging

Let's walk through a simplified scenario of secure messaging using asymmetric encryption, symmetric encryption, hashing, digital signatures, and digital certificates. 

*Setup*

1. Alice and Bob each generate a pair of public and private keys. 
2. They obtain digital certificates for their public keys from a trusted certificate authority.
3. They exchange their public keys and verify each other's certificates.

*Sending a Message*

1. Alice wants to send a confidential message to Bob. 
2. She generates a random symmetric key and encrypts her message with it using a symmetric cipher like AES.
3. She encrypts the symmetric key with Bob's public key.
4. She creates a hash of her message and encrypts it with her private key to create a digital signature.
5. She sends the encrypted message, the encrypted symmetric key, and her digital signature to Bob.

*Receiving the Message* 

1. Bob receives the encrypted message, the encrypted symmetric key, and Alice's digital signature.
2. He decrypts the symmetric key using his private key.
3. He uses the symmetric key to decrypt the message.
4. He creates a hash of the decrypted message. 
5. He decrypts Alice's digital signature using her public key and gets her original hash.
6. He compares the hash he computed to the one from Alice's signature. If they match, he knows the message is from Alice and hasn't been altered.

In this scenario:

- The symmetric encryption provides confidentiality. 
- The asymmetric encryption allows secure exchange of the symmetric key.
- The hashing and digital signature provide authentication and integrity.
- The digital certificates establish trust in the public keys.

## Conclusion

Asymmetric encryption is a powerful tool that forms the basis for much of the security we rely on in the digital world. Its unique properties enable secure communication and transactions between parties without prior contact. When combined with symmetric encryption, hashing, and digital signatures, it allows for systems that provide confidentiality, authentication, integrity, and non-repudiation. Understanding these concepts is crucial for anyone working in cybersecurity.

## References

1. Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th Edition). Pearson.
2. Ferguson, N., Schneier, B., & Kohno, T. (2010). Cryptography Engineering: Design Principles and Practical Applications. Wiley.
3. Katz, J., & Lindell, Y. (2014). Introduction to Modern Cryptography (2nd Edition). Chapman & Hall/CRC.
4. Diffie, W., & Hellman, M. (1976). New directions in cryptography. IEEE Transactions on Information Theory, 22(6), 644-654.