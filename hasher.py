import hashlib
import bcrypt

password = "1234".encode()

# MD5 Hash
md5_hash = hashlib.md5(password).hexdigest()
print("MD5 Hash:", md5_hash)

# Bcrypt Hash
bcrypt_hash = bcrypt.hashpw(password, bcrypt.gensalt())
print("Bcrypt Hash:", bcrypt_hash.decode())
