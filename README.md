

---

## 🛠 Demo 1: Basic Hash Cracking (Dictionary Attack)
**What it does:** Tries passwords from a **wordlist**.  
🔹 Works well when the password exists in common lists like **rockyou.txt**.  

### **1️⃣ Generate an MD5 Hash (Target Password: "hello123") using a tool or online**


### **2️⃣ Create a Wordlist**
```bash
echo -e "password123\nhello123\nqwerty\n12345678\nletmein" > wordlist.txt
```

### **3️⃣ Run the Dictionary Attack**
```bash
hashcat -m 0 -a 0 -o cracked.txt hash.txt wordlist.txt
```

### **4️⃣ Check Results**
```bash
cat cracked.txt
```

---

## 🛠 Demo 2: Brute-Force Attack (Short Passwords)
**What it does:** Tries **all possible combinations** within a length range.  

### **1️⃣ Generate a Hash (Target Password: "1234")**
```bash
echo -n "1234" | md5sum > hash.txt
```

### **2️⃣ Run a Brute-Force Attack for 4-Digit PINs**
```bash
hashcat -m 0 -a 3 hash.txt ?d?d?d?d
```

### **3️⃣ Run a Brute-Force Attack for 6-Digit PINs**
```bash
hashcat -m 0 -a 3 hash.txt ?d?d?d?d?d?d
```

---

## 🛠 Demo 3: Mask Attack (Targeted Cracking)
**What it does:** If part of the password is known, it reduces guessing time.  

### **1️⃣ Generate a Hash (Target Password: "P@ss1234")**
```bash
echo -n "P@ss1234" | md5sum > hash.txt
```

### **2️⃣ Run a Mask Attack (Known Prefix "P@ss")**
```bash
hashcat -m 0 -a 3 hash.txt P@ss?d?d?d?d
```

---

## 🛠 Demo 4: Hash Type Comparison (MD5 vs bcrypt)
**What it does:** Shows why modern hashes are **harder to crack**.  

### **1️⃣ Generate an MD5 Hash (Fast to Crack)**
```bash
echo -n "password123" | md5sum > hash.txt
```

### **2️⃣ Run Dictionary Attack on MD5**
```bash
hashcat -m 0 -a 0 -o cracked.txt hash.txt wordlist.txt
```

### **3️⃣ Generate a bcrypt Hash (Much Harder)**
Run in Python:  
```python
import bcrypt
password = b"password123"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed.decode())
```
Copy the output (starts with `$2b$12$...`) into `hash.txt`.  

### **4️⃣ Try Cracking bcrypt (Will Take Too Long)**
```bash
hashcat -m 3200 -a 0 -o cracked.txt hash.txt wordlist.txt
```

📌 **Conclusion:**  
- **MD5 is weak**, cracks in seconds.  
- **Bcrypt is strong**, may take **years** to crack.  


