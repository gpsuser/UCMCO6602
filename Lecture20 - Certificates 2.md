# Cryptography: Lecture 20 - Certificates

## Introduction

Certificates provide a mechanism to establish trust in public keys, solving one of the core challenges in public key cryptography: how do we know that a public key truly belongs to its claimed owner?

In our previous lectures, we've covered various cryptographic primitives and protocols, including symmetric and asymmetric encryption, hash functions, and digital signatures. Certificates build upon these concepts to enable secure key establishment and authentication in distributed systems. They are the cornerstone of Public Key Infrastructure (PKI), which facilitates secure communications across the internet through protocols such as TLS/SSL.

By the end of this lecture, you'll understand how certificates work, their role in establishing secure communications, and the infrastructure that supports their use in real-world applications.

## Learning Objectives

By the end of this lecture, you should be able to:

1. Define and explain the concept of key establishment using certificates
2. Describe the role of a Certificate Authority (CA) in a PKI system
3. Understand the process of certificate generation and validation
4. Explain how Diffie-Hellman key exchange works and how certificates enhance its security
5. Define Public Key Infrastructure and explain its components and operation

Let's begin by exploring the fundamental problem that certificates aim to solve.

## 8. Key Establishment Using Certificates

### 8.1 The Key Distribution Problem

One of the fundamental challenges in cryptography is the secure distribution of keys. In symmetric cryptography, both parties need to share a secret key, which presents a chicken-and-egg problem: how do you securely share the key needed for secure communication before you have a secure channel?

Public key cryptography partially addresses this through the use of key pairs, but introduces a new problem: **key authentication**. How do you know that a public key truly belongs to the entity you want to communicate with?

Consider the following scenario:

1. Alice wants to send a confidential message to Bob
2. Alice obtains what she believes is Bob's public key
3. Alice encrypts her message with this public key and sends it to Bob
4. Bob decrypts the message with his private key

This seems straightforward, but there's a critical vulnerability: if an attacker (Mallory) can convince Alice that Mallory's public key actually belongs to Bob, then Alice will unknowingly encrypt messages that only Mallory can decrypt.

### 8.2 Certificates as a Solution

A **digital certificate** is a document that binds a public key to an identifier (such as a person, organization, or device). It's digitally signed by a trusted third party, known as a Certificate Authority (CA), which verifies the identity of the certificate holder.

The certificate essentially says: "The CA vouches that this public key belongs to this entity."

A standard X.509 certificate typically contains:

1. **Version**: The X.509 version (commonly v3)
2. **Serial Number**: A unique identifier assigned by the CA
3. **Signature Algorithm**: The algorithm used by the CA to sign the certificate
4. **Issuer**: The entity that verified the information and issued the certificate (the CA)
5. **Validity Period**: The time period during which the certificate is valid
6. **Subject**: The identity of the entity associated with the public key
7. **Subject Public Key Info**: The public key and the algorithm with which it is used
8. **Extensions**: Additional information such as key usage constraints
9. **Certificate Signature**: The CA's digital signature

### 8.3 Key Establishment Protocol Using Certificates

Here's a typical protocol for establishing a secure communication channel using certificates:

1. **Certificate Exchange**:
   - Alice sends her certificate (containing her public key) to Bob
   - Bob sends his certificate (containing his public key) to Alice

2. **Certificate Validation**:
   - Alice verifies Bob's certificate using the CA's public key
   - Bob verifies Alice's certificate using the CA's public key

3. **Session Key Establishment**:
   - Once certificates are validated, they use their authenticated public keys to establish a session key
   - This can be done through various key agreement protocols, such as Diffie-Hellman

4. **Secure Communication**:
   - They use the established session key for encrypted communication

The critical advantage of this approach is that neither party needs prior knowledge of the other's public key. They only need to trust the CA that signed the certificates.

## 9. The Role of a Certificate Authority (CA)

A **Certificate Authority (CA)** is a trusted entity that issues digital certificates. Its primary role is to verify the identity of certificate applicants and bind their identities to their public keys through its digital signature.

### 9.1 CA Responsibilities

The CA's responsibilities include:

1. **Identity Verification**: Verifying that the entity requesting a certificate is who they claim to be
2. **Certificate Issuance**: Creating and signing certificates for verified entities
3. **Certificate Revocation**: Maintaining and publishing lists of certificates that are no longer valid
4. **Certificate Repository**: Maintaining a directory of issued certificates

### 9.2 Trust Models

The effectiveness of certificates depends on trust models. There are several approaches:

1. **Hierarchical (Tree) Model**: A root CA issues certificates to intermediate CAs, which issue certificates to end entities. Trust flows from the root down.

2. **Web of Trust**: Used in systems like PGP, where users vouch for each other's identities. No central authority exists.

3. **Bridge CA Model**: Multiple hierarchies are connected through a bridge CA, allowing entities in different hierarchies to establish trust.

The hierarchical model is the most common and is used in the global PKI that secures the web.

### 9.3 Worked Example of a CA

Let's walk through a simplified example of how a CA operates in practice.

Imagine you're setting up a secure web server for your company, `example.com`.

#### Step 1: Generate a Key Pair
First, you generate a public/private key pair for your web server:

```bash
# Generate a private key
openssl genrsa -out example.com.key 2048

# Extract the public key
openssl rsa -in example.com.key -pubout -out example.com.pub
```

#### Step 2: Create a Certificate Signing Request (CSR)
You create a CSR containing your public key and identifying information:

```bash
openssl req -new -key example.com.key -out example.com.csr
```

During this process, you'll be prompted to provide information:
- Common Name (CN): example.com
- Organization (O): Example Corporation
- Organizational Unit (OU): IT Department
- Country (C): US
- State/Province (ST): California
- Locality (L): San Francisco

#### Step 3: CA Verification
You submit your CSR to a commercial CA like DigiCert, Verisign, or Let's Encrypt. The CA will verify your identity through various means:

1. **Domain Validation (DV)**: Proving you control the domain by responding to an email sent to a standard address at that domain or by placing a specific file on your web server.

2. **Organization Validation (OV)**: Additional verification of your organization through official records.

3. **Extended Validation (EV)**: Rigorous verification of organization identity, requiring legal documentation and sometimes physical verification.

#### Step 4: Certificate Issuance
After verifying your identity, the CA signs your certificate:

```bash
# On the CA's system
openssl x509 -req -days 365 -in example.com.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out example.com.crt
```

The CA sends you the signed certificate, which you install on your web server.

#### Step 5: Certificate Usage
When a user visits https://example.com, their browser:
1. Receives your certificate
2. Verifies the CA's signature using the CA's public key (which is pre-installed in the browser)
3. Checks if the certificate is valid (not expired, not revoked)
4. Establishes a secure connection if all checks pass

## 10. Certificate Generation and the Role of the CA

Let's delve deeper into the certificate generation process and the CA's role.

### 10.1 Certificate Generation Process

The certificate generation process involves several key steps:

1. **Key Pair Generation**: The entity (applicant) generates a public/private key pair.

2. **Certificate Signing Request (CSR) Creation**: The applicant creates a CSR containing:
   - The public key
   - Identifying information (name, organization, location)
   - Signature created with the applicant's private key

3. **Identity Verification**: The CA verifies the applicant's identity through various means, depending on the certificate type.

4. **Certificate Creation**: The CA creates a certificate containing:
   - The applicant's public key
   - The applicant's identifying information
   - The CA's identifying information
   - Validity period
   - Serial number
   - Other extensions and parameters

5. **Certificate Signing**: The CA signs the certificate with its private key.

6. **Certificate Issuance**: The CA delivers the signed certificate to the applicant.

### 10.2 Worked Example of Certificate Generation

Let's work through a detailed example of generating a certificate for a web server.

#### Step 1: Generate Key Pair
The server administrator generates a 2048-bit RSA key pair:

```bash
openssl genrsa -out server.key 2048
```

This generates the private key. The public key will be extracted during CSR creation.

#### Step 2: Create Certificate Signing Request
The administrator creates a CSR:

```bash
openssl req -new -key server.key -out server.csr
```

When prompted, they enter:
```
Country Name (2 letter code) [AU]: GB
State or Province Name: London
Locality Name: London
Organization Name: University Cybersecurity Department
Organizational Unit Name: Web Services
Common Name (e.g. server FQDN): secure.university.edu
Email Address: admin@university.edu
```

#### Step 3: CA Processing
The CA receives the CSR and performs validation checks. Let's look at what happens on the CA's side:

1. **Extract CSR Information**:
   ```bash
   openssl req -in server.csr -noout -text
   ```
   This shows the information provided in the CSR, including the public key.

2. **Validate Domain Ownership**:
   The CA might send an email to admin@university.edu or ask the administrator to place a specific file at a specific location on the web server.

3. **Generate Certificate**:
   ```bash
   # Create a configuration file for the certificate
   cat > cert.conf << EOF
   [cert]
   basicConstraints = CA:FALSE
   keyUsage = digitalSignature, keyEncipherment
   subjectAltName = @alt_names
   
   [alt_names]
   DNS.1 = secure.university.edu
   DNS.2 = www.secure.university.edu
   EOF
   
   # Generate the certificate
   openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key \
   -CAcreateserial -out server.crt -days 365 \
   -extfile cert.conf -extensions cert
   ```

4. **Verify the Certificate**:
   ```bash
   openssl x509 -in server.crt -text -noout
   ```

#### Step 4: Certificate Delivery
The CA delivers the signed certificate to the administrator, who installs it on the web server along with the private key.

#### Step 5: Certificate Installation
The certificate is installed on the web server:

```bash
# Apache configuration example
SSLCertificateFile /path/to/server.crt
SSLCertificateKeyFile /path/to/server.key
SSLCertificateChainFile /path/to/ca-chain.crt
```

#### Step 6: Certificate Validation
When a client connects to the server:

1. The server presents its certificate
2. The client verifies the certificate by:
   - Checking the CA's signature using the CA's public key
   - Verifying the certificate hasn't expired
   - Checking the certificate hasn't been revoked
   - Confirming the domain name matches the certificate

3. If validation succeeds, the client establishes a secure connection

### 10.3 Certificate Validation Details

When a client validates a certificate, it performs several checks:

1. **Signature Verification**: Using the CA's public key to verify the signature on the certificate

2. **Certificate Chain Validation**: Following the chain of trust from the server's certificate up to a trusted root CA

3. **Validity Period Check**: Ensuring the current date is within the certificate's validity period

4. **Revocation Check**: Checking Certificate Revocation Lists (CRLs) or using the Online Certificate Status Protocol (OCSP) to verify the certificate hasn't been revoked

5. **Name Check**: Verifying that the certificate's Subject Alternative Name (SAN) or Common Name (CN) matches the server's domain name

## 11. Diffie-Hellman Key Exchange

Diffie-Hellman key exchange is a method for securely establishing a shared secret over an unsecured channel. It allows two parties to jointly establish a shared secret key without ever having to transmit that key.

### 11.1 Basic Diffie-Hellman Protocol

The protocol relies on the mathematical properties of modular exponentiation and the difficulty of the discrete logarithm problem.

The basic protocol works as follows:

1. **Parameter Agreement**:
   - Alice and Bob agree on two public parameters: a large prime number p and a generator g (where 1 < g < p)

2. **Private Value Generation**:
   - Alice generates a random private value a
   - Bob generates a random private value b

3. **Public Value Exchange**:
   - Alice computes A = g^a mod p and sends A to Bob
   - Bob computes B = g^b mod p and sends B to Alice

4. **Shared Secret Computation**:
   - Alice computes the shared secret K = B^a mod p = (g^b)^a mod p = g^(ab) mod p
   - Bob computes the shared secret K = A^b mod p = (g^a)^b mod p = g^(ab) mod p

Both Alice and Bob now have the same shared secret K = g^(ab) mod p, which they can use to derive encryption keys.

### 11.2 Numerical Example

Let's work through a simplified example with small numbers (in practice, much larger numbers are used):

1. **Parameter Agreement**:
   - Alice and Bob agree on p = 23 and g = 5

2. **Private Value Generation**:
   - Alice selects a = 6
   - Bob selects b = 15

3. **Public Value Exchange**:
   - Alice computes A = 5^6 mod 23 = 15625 mod 23 = 8
   - Alice sends 8 to Bob
   - Bob computes B = 5^15 mod 23 = 30517578125 mod 23 = 19
   - Bob sends 19 to Alice

4. **Shared Secret Computation**:
   - Alice computes K = 19^6 mod 23 = 47045881 mod 23 = 2
   - Bob computes K = 8^15 mod 23 = 35184372088832 mod 23 = 2

Both Alice and Bob have computed the same shared secret K = 2.

### 11.3 Man-in-the-Middle Vulnerability

The basic Diffie-Hellman protocol is vulnerable to man-in-the-middle attacks. If an attacker (Mallory) can intercept the communications between Alice and Bob, she can:

1. Intercept A from Alice and B from Bob
2. Generate her own private values c and d
3. Compute C = g^c mod p and send it to Bob
4. Compute D = g^d mod p and send it to Alice
5. Establish shared secrets with both Alice and Bob:
   - K_AM = A^d mod p (shared with Alice)
   - K_BM = B^c mod p (shared with Bob)

Mallory can now decrypt traffic from Alice using K_AM, read or modify it, and re-encrypt it using K_BM before forwarding it to Bob.

## 11.1 Certificates in Diffie-Hellman Key Exchange

To prevent man-in-the-middle attacks, Diffie-Hellman can be enhanced with certificates, creating what's known as **Authenticated Diffie-Hellman**.

### How Certificates Secure Diffie-Hellman

The enhanced protocol, often called Station-to-Station (STS) protocol, works as follows:

1. **Parameter and Certificate Exchange**:
   - Alice sends her certificate (containing her public key) to Bob
   - Bob sends his certificate (containing his public key) to Alice
   - Both verify each other's certificates using CA's public key

2. **Diffie-Hellman Exchange**:
   - They perform the standard Diffie-Hellman exchange with additional authentication

3. **Key Authentication**:
   - Alice signs her DH public value (A) with her private key and sends the signature to Bob
   - Bob verifies Alice's signature using Alice's public key from her certificate
   - Bob signs his DH public value (B) with his private key and sends the signature to Alice
   - Alice verifies Bob's signature using Bob's public key from his certificate

This protocol ensures that:
- The DH public values come from the authenticated parties
- No man-in-the-middle can forge the signatures without the private keys

### TLS Implementation

In TLS (Transport Layer Security), authenticated Diffie-Hellman is implemented as follows:

1. **ClientHello**: Client sends supported cipher suites and a random number

2. **ServerHello**: Server selects a cipher suite and sends another random number

3. **Certificate**: Server sends its certificate

4. **ServerKeyExchange**: Server sends DH parameters (p, g) and its DH public value, signed with its private key

5. **CertificateRequest** (optional): Server requests client certificate

6. **ServerHelloDone**: Server completes its part of the handshake

7. **Certificate** (optional): Client sends its certificate if requested

8. **ClientKeyExchange**: Client sends its DH public value

9. **CertificateVerify** (optional): Client signs a hash of the handshake messages with its private key

10. **ChangeCipherSpec** and **Finished**: Both parties switch to encrypted communication using the derived shared secret

This protocol provides both authentication and forward secrecy (compromising the server's long-term private key doesn't compromise past session keys).

## 12. Public Key Infrastructure (PKI)

**Public Key Infrastructure (PKI)** is a framework of hardware, software, policies, procedures, and roles that creates, manages, distributes, uses, stores, and revokes digital certificates.

### 12.1 Components of PKI

A complete PKI system includes:

1. **Certificate Authority (CA)**: Issues and manages certificates

2. **Registration Authority (RA)**: Verifies the identity of entities requesting certificates

3. **Certificate Repository**: Stores and distributes certificates and Certificate Revocation Lists (CRLs)

4. **Certificate Revocation System**: Maintains and publishes information about revoked certificates

5. **Key Archive and Recovery System**: Securely stores private keys for recovery purposes (optional)

6. **PKI-enabled Applications**: Software that uses the PKI for security services

### 12.2 PKI Hierarchy

PKI typically operates in a hierarchical structure:

1. **Root CA**: The highest level of trust, self-signed certificate
   - Typically kept offline for maximum security
   - Signs certificates for intermediate CAs

2. **Intermediate CAs**: Bridge between Root CAs and end entities
   - Signed by Root CA or higher-level Intermediate CA
   - Sign certificates for other Intermediate CAs or end entities

3. **End-Entity Certificates**: Issued to users, devices, or services
   - Signed by an Intermediate CA
   - Used for encryption, authentication, or digital signatures

### 12.3 Certificate Lifecycle

Certificates in a PKI go through a lifecycle:

1. **Application**: Entity requests a certificate

2. **Verification**: RA verifies the entity's identity

3. **Issuance**: CA issues the certificate

4. **Distribution**: Certificate is distributed to the entity and possibly published in a repository

5. **Use**: Entity uses the certificate for security services

6. **Renewal**: Certificate is renewed before expiration

7. **Revocation**: Certificate is revoked if compromised or no longer needed

8. **Expiration**: Certificate becomes invalid after its validity period

### 12.4 Certificate Revocation

Certificates may need to be revoked before their expiration date for various reasons:
- Private key compromise
- Change in affiliation
- Certificate superseded
- Cessation of operation

Two main mechanisms for certificate revocation are:

1. **Certificate Revocation Lists (CRLs)**: Periodically published lists of revoked certificates
   ```
   Certificate Serial Number: 1234
   Revocation Date: 2023-02-15
   Reason: Key Compromise
   ```

2. **Online Certificate Status Protocol (OCSP)**: Allows real-time certificate status checking
   ```
   Request:
     Certificate ID: 1234 (hash of issuer name, serial number)
   
   Response:
     Certificate Status: good/revoked/unknown
     Revocation Time: 2023-02-15 (if revoked)
     Reason: keyCompromise (if revoked)
   ```

### 12.5 PKI Standards

PKI relies on several standards:

1. **X.509**: Defines certificate format and validation procedures

2. **PKCS (Public Key Cryptography Standards)**: A set of standards:
   - PKCS#10: Certificate Signing Request format
   - PKCS#7: Cryptographic Message Syntax
   - PKCS#12: Personal Information Exchange Syntax (.pfx/.p12 files)

3. **RFC 5280**: Internet X.509 Public Key Infrastructure Certificate and CRL Profile

4. **RFC 6960**: X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP

### 12.6 PKI in Practice

PKI is used in various security applications:

1. **Secure Web Browsing (HTTPS)**: Certificates authenticate websites and enable encrypted connections

2. **Secure Email (S/MIME)**: Certificates enable email encryption and signing

3. **Code Signing**: Certificates authenticate software publishers

4. **Virtual Private Networks (VPNs)**: Certificates authenticate VPN endpoints

5. **Smart Cards and Hardware Security Tokens**: Certificates stored on physical devices for authentication

## Comparison Table: Certificate Types

| Certificate Type | Validation Level | Use Case | Typical Validity Period | Verification Process |
|------------------|------------------|----------|------------------------|----------------------|
| Domain Validation (DV) | Low | Basic HTTPS | 1-3 years | Domain control verification only |
| Organization Validation (OV) | Medium | Business websites | 1-3 years | Organization verification + domain control |
| Extended Validation (EV) | High | Financial institutions | 1-2 years | Rigorous legal and physical verification |
| Wildcard Certificate | Varies | Multiple subdomains | 1-2 years | Same as base type, covers *.domain.com |
| Multi-Domain (SAN) | Varies | Multiple domains | 1-2 years | Each domain validated separately |
| Self-Signed | None | Testing, internal use | Any | None (not trusted by browsers) |

## Summary: PKI Trust Models

| Trust Model | Structure | Advantages | Disadvantages | Example Use |
|-------------|-----------|------------|---------------|-------------|
| Hierarchical | Tree structure with root CA at top | Clear chain of trust, Simple verification | Single point of failure (root CA) | Web PKI, Enterprise PKI |
| Web of Trust | Decentralized peer endorsement | No central authority, Resilient | Difficult to establish global trust | PGP email encryption |
| Bridge CA | Multiple hierarchies connected via bridge | Enables cross-organizational trust | Complex management | Government PKIs |
| Mesh | All CAs cross-certify each other | Full interconnection | Complex, Difficult to scale | Small closed networks |

## Conclusion

In this lecture, we've explored the world of certificates and Public Key Infrastructure. We've seen how certificates solve the key authentication problem in public key cryptography by binding identities to public keys through trusted third parties.

We've examined the role of Certificate Authorities in verifying identities and issuing certificates, and we've walked through the certificate generation process with practical examples. We've also seen how certificates enhance the security of key exchange protocols like Diffie-Hellman by preventing man-in-the-middle attacks.

Finally, we've studied the broader PKI framework that supports certificate management throughout their lifecycle, from issuance to revocation and expiration.

Certificates and PKI form the backbone of secure communications on the internet and in enterprise environments. They enable the secure browsing, email, and numerous other applications that we rely on daily. While the concepts may seem complex at first, they're built on the fundamental cryptographic principles we've covered in previous lectures.

In our next lecture, we'll explore how these concepts are applied in real-world protocols and standards for secure communication.

## References

1. Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice* (7th ed.). Pearson.

2. Schneier, B. (2015). *Applied Cryptography: Protocols, Algorithms, and Source Code in C* (20th Anniversary Edition). Wiley.

3. Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., & Polk, W. (2008). *Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile*. RFC 5280.

4. Rescorla, E. (2018). *The Transport Layer Security (TLS) Protocol Version 1.3*. RFC 8446.

5. Adams, C., & Lloyd, S. (2003). *Understanding PKI: Concepts, Standards, and Deployment Considerations* (2nd ed.). Addison-Wesley Professional.

6. National Institute of Standards and Technology. (2001). *Introduction to Public Key Technology and the Federal PKI Infrastructure*. SP 800-32.