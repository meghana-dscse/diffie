p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = (g ** a) % p
B = (g ** b) % p

print("\nAlice's public key:", A)
print("Bob's public key:", B)

alice_key = (B ** a) % p
bob_key = (A ** b) % p

print("\nAlice's shared secret key:", alice_key)
print("Bob's shared secret key:", bob_key)

if alice_key == bob_key:
    print("\nKey exchange successful.")
    print("Shared secret key:", alice_key)
else:
    print("\nKey exchange failed.")
