

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


