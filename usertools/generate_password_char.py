from passlib.hash import sha256_crypt

src = raw_input("Input password without encoding:\n")
enc = sha256_crypt.encrypt(src)

print("Your encrypted password is:\n %s" % enc)

print("\n")
print("Verify your encryption:")
print(sha256_crypt.verify(src, enc))
