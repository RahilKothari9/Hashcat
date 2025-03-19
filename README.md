

---

## Demo 1: Basic Hash Cracking (Dictionary Attack)
**What it does:** Tries passwords from a **wordlist**.  

### **Run the Dictionary Attack**
```bash
hashcat -m 0 -a 0 -o cracked.txt hash.txt wordlist.txt
```


---

## 🛠 Demo 2: Brute-Force Attack (Short Passwords)
**What it does:** Tries **all possible combinations** within a length range.  


### **Run a Brute-Force Attack for 4-Digit PINs**
```bash
hashcat -m 0 -a 3 hash.txt ?d?d?d?d
```

---

## 🛠 Demo 3: Mask Attack (Targeted Cracking)
**What it does:** If part of the password is known, it reduces guessing time.  


### **1 Run a Mask Attack (Known Prefix "rahil")**
```bash
hashcat -m 0 -a 3 hash.txt rahil?d?d?d
```


---

🛠 Demo 4: MD5 vs. Bcrypt Hashing (4-Digit Number)
What it does: Compares the time taken to crack MD5 and bcrypt hashes of the same 4-digit number.

1. Generate Hashes for a 4-Digit Number (e.g., 1234)
Run the following Python script to generate both MD5 and bcrypt hashes:


MD5: hashcat -m 0 -a 3 md5_hash.txt ?d?d?d?d
bcrypt: hashcat -m 3200 -a 3 bcrypt_hash.txt ?d?d?d?d
Observations:
MD5 is fast but insecure and can be cracked quickly.
Bcrypt is slow due to its computational cost, making brute-force attacks much harder.

