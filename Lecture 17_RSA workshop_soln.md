# RSA Cryptography Exercises Solutions

## Exercise 1

Given: p = 11 and q = 5 as set-up parameters for RSA.

### a) Given that e = 7, compute the corresponding private key d

1. Calculate n = p × q
   * n = 11 × 5 = 55

2. Calculate φ(n) = (p-1) × (q-1)
   * φ(n) = 10 × 4 = 40

3. To find d, solve the congruence:
   * e × d ≡ 1 (mod φ(n))
   * 7d ≡ 1 (mod 40)
   * Need to find d such that 7d = 40k + 1 for some integer k

4. Using extended Euclidean algorithm:
   * 40 = 5 × 7 + 5
   * 7 = 1 × 5 + 2
   * 5 = 2 × 2 + 1
   * 2 = 2 × 1 + 0

   Working backwards:
   * 1 = 5 - 2 × 2
   * 1 = 5 - 2 × (7 - 1 × 5)
   * 1 = 3 × 5 - 2 × 7
   * 1 = 3 × (40 - 5 × 7) - 2 × 7
   * 1 = 3 × 40 - 17 × 7

Therefore, d = -17 ≡ 23 (mod 40)

### b) What other values can be used for e?

* e must be coprime with φ(n) = 40
* e must be between 1 and φ(n)
* Factors of 40 are: 1, 2, 4, 5, 8, 10, 20, 40
* Valid values for e: 3, 7, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39

## Exercise 2

Given: p = 41 and q = 17 as set-up parameters for RSA.

1. Calculate n = p × q
   * n = 41 × 17 = 697

2. Calculate φ(n) = (p-1) × (q-1)
   * φ(n) = 40 × 16 = 640

### c) Which of the parameters e₁ = 32, e₂ = 49 is a valid RSA exponent?

For e₁ = 32:

* 32 is less than 640 ✓
* gcd(32, 640) = 32 ≠ 1 ✗
* 32 = 2⁵, and 640 = 2⁷ × 5, share factors
* Therefore e₁ = 32 is NOT valid

For e₂ = 49:

* 49 is less than 640 ✓
* gcd(49, 640) = 1 ✓
* 49 = 7², and 640 = 2⁷ × 5, no common factors
* Therefore e₂ = 49 is valid

### d) Compute the corresponding private key d

Using extended Euclidean algorithm:

* 640 = 13 × 49 + 3
* 49 = 16 × 3 + 1
* 3 = 3 × 1 + 0

Working backwards:

* 1 = 49 - 16 × 3
* 1 = 49 - 16 × (640 - 13 × 49)
* 1 = 209 × 49 - 16 × 640

Therefore, d = 209

## Exercise 3

Encrypt and decrypt using RSA algorithm with given parameters.

### a) p = 5, q = 11, e = 3, X = 9

1. Calculate parameters:
   * n = p × q = 5 × 11 = 55
   * φ(n) = (p-1) × (q-1) = 4 × 10 = 40

2. Encryption (Y = X^e mod n):
   * Y = 9³ mod 55
   * Y = 729 mod 55
   * Y = 14

3. Find d (private key):
   * 3d ≡ 1 (mod 40)
   * d = 27

4. Decryption (X = Y^d mod n):
   * X = 14²⁷ mod 55
   * X = 9 (original message)

### b) p = 3, q = 11, d = 7, X = 5

1. Calculate parameters:
   * n = p × q = 3 × 11 = 33
   * φ(n) = (p-1) × (q-1) = 2 × 10 = 20

2. Find e:
   * 7e ≡ 1 (mod 20)
   * e = 3

3. Encryption:
   * Y = 5³ mod 33
   * Y = 125 mod 33
   * Y = 26

4. Decryption:
   * X = 26⁷ mod 33
   * X = 5 (original message)

## Exercise 4

Square-and-multiply steps for calculating x²⁹ with x = 2

1. Convert 29 to binary: 
   * 29₁₀ = 11101₂

2. Square-and-multiply steps:
   * Step 1 (leftmost 1): 2 → Result = 2
   * Step 2 (second 1): 2² = 4, 4 × 2 = 8 → Result = 8
   * Step 3 (third 1): 8² = 64, 64 × 2 = 128 → Result = 128
   * Step 4 (fourth 0): 128² = 16,384 → Result = 16,384
   * Step 5 (fifth 1): 16,384² = 268,435,456, × 2 = 536,870,912

Final result: 2²⁹ = 536,870,912

## Exercise 5

Bob's RSA setup with p = 7 and q = 17.

1. Calculate n:
   * n = p × q = 7 × 17 = 119

2. Calculate φ(n):
   * φ(n) = (p-1) × (q-1) = 6 × 16 = 96

3. Find e (given d = 77):
   * e × 77 ≡ 1 (mod 96)
   * e = 5

Bob's key pair:

* Public key: (n = 119, e = 5)
* Private key: (n = 119, d = 77)

4. Encrypt X = 4:
   * Y = 4⁵ mod 119
   * Y = 72

5. Decrypt Y = 72:
   * X = 72⁷⁷ mod 119
   * X = 4 (original message)

## Exercise 6

Problem: Bob encrypted his message to Alice with his private key.

### Issues with Bob's approach:

1. Privacy Issue:
   * Anyone can decrypt using Bob's public key
   * Message is not confidential
   * No privacy protection

2. Authentication Issue:
   * While it proves message came from Bob
   * This is an incorrect use of private key encryption
   * Should use digital signatures instead

### Correct Approach Should Be:

1. Encrypt with Alice's public key (for privacy)
2. Sign with Bob's private key (for authentication)
3. Send both encrypted message and signature

### Why Alice is Upset:

* No message privacy
* Inefficient authentication method
* Misuse of public key cryptography principles

### Solution:

Bob should:
1. Encrypt message using Alice's public key
2. Create digital signature using his private key
3. Send both components to Alice

This provides both privacy and authentication properly.