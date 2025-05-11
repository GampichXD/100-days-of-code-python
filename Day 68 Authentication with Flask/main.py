# Authentication 
# Why do we need authentication? -> To protect our data and resources from unauthorized access.
# Create an account to access the system.
# Log in -> To access the system.
# Restrict access to certain resources.
# Level 1 : Email and Password

# Encryption and Hashing
# Level 2 : Encryption is the process of converting data into a code to prevent unauthorized access.
# Enigma machine is a famous example of an encryption device used in World War II.
# Caesar cipher is a simple encryption technique that shifts letters by a fixed number.
# cryptii.com is a website that provides various encryption and hashing algorithms.

# Level 3 : Hashing is a one-way function that converts data into a fixed-size string of characters.
# Old Encyption Method
# Password + Key -- Chiper Method --> Chiper Text
# qwert + 1 -- CM --> rvfsuz
# Old Decryption Method
# Key + Chiper Text -- Decrypt Method --> Password
# rvfsuz + 1 -- DM --> qwert
# Hashing is used to store passwords securely.
# Password + Salt -- Hashing Method --> Hash
# Hash Function - Calculates a fixed-size hash value from the input data.
# Registration Password + Salt -- Hashing Method --> Hash (Store in DB)
# Login Password + Salt -- Hashing Method --> Hash (Compare with stored hash)

# How to Hack Passwords 101
# plaintextoffenders.com is a website that provides information on how to hack passwords.
# YOU'VE BEEN HACKED
# haveibeenpwned.com is a website that provides information on whether your email has been compromised in a data breach.
# Same password == Same hash
# Let's make a hash table
# All words from the dictionary (~150k)
# All numbers from 0 to 9999
# All combinations of characters up to 6 characters
# GTX 1080 - 20000000000 MD5 hashes per second
# More long your password is, more secure it is because more long time to cracking computation that increases exponentially
# password-checker.online-domain-tools.com is a website that provides a password strength checker.
# hackertyper.net is a website that simulates a hacker typing on a keyboard.

# Level 4 : Hashing & Salting
# Hashing is a one-way function that converts data into a fixed-size string of characters.
# Salting is the process of adding random data to the input of a hash function to make it more secure.
# qwerty + 28891 -- Hashing Method --> 9f4b2c3e4d5f6a7b8c9d0e1f2g3h4i5j6
# cryptii.com is a website that provides various encryption and hashing algorithms.
# GTX 1080 - 17k bcrypt hashes per second
# Salt Round - Number of iterations to make the hash more secure. (More Salt in every round)