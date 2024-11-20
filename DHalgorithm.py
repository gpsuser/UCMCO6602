def calculate_power(base, exponent, modulus):
   """Power function to return value of (base ^ exponent) mod modulus."""
   if exponent == 1:
      return base
   else:
      return pow(base, exponent) % modulus

# Driver code
if __name__ == "__main__":
   prime = 23
   generator = 5
   private_key_alice = 6
   private_key_bob = 15

   # Generating public keys
   x = calculate_power(generator, private_key_alice, prime)
   y = calculate_power(generator, private_key_bob, prime)

   # Generating secret keys after the exchange of keys
   secret_key_alice = calculate_power(y, private_key_alice, prime)
   secret_key_bob = calculate_power(x, private_key_bob, prime)

   # Output
   print("Prime number (P):", prime)
   print("Generator value (G):", generator)
   print("Alice's private key (a):", private_key_alice)
   print("Bob's private key (b):", private_key_bob)
   print("Secret key for Alice:", secret_key_alice)
   print("Secret key for Bob:", secret_key_bob)