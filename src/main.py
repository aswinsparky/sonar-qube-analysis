import os
import subprocess  # Dangerous for unsanitized user input!
import hashlib  # Weak hash usage warning (Bandit: B303)
import random  # Predictable randoms used for security (Bandit: B311)
import sqlite3  # Unsafe SQL string composition
import secrets

# Dangerous command execution (Bandit: B602)
def command_injection():
    filename = input("Type a filename to read: ")
    # Vulnerable: unsanitized string passed to shell
    subprocess.call(f"cat {filename}", shell=True)

# Improper file permissions (Bandit: B106)
def create_insecure_file():
    with open("mydata.txt", "w") as f:
        f.write("Not secure permissions!")
    os.chmod("mydata.txt", 0o777)  # World-writable file

# SQL Injection (Bandit: B608)
def sql_injection():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    username = input("Username? ")
    # Insecure: direct string interpolation allows SQL injection
    cur.execute(f"SELECT * FROM users WHERE name = '{username}'")
    print(cur.fetchall())

# Weak cryptographic use (Bandit: B303)
def weak_hashing():
    data = input("Type data to hash: ")
    print(hashlib.md5(data.encode()).hexdigest())  # Weak hash

# Predictable random for security token (Bandit: B311)
def insecure_token():
    # Using random instead of secrets for tokens
    token = str(random.randint(1000, 9999))
    print("Auth token:", token)

# Open redirect vulnerability (OWASP Top 10)
def open_redirect():
    url = input("Where should we redirect?")
    # Unsafe user-controlled redirect
    print(f"Redirecting to: {url}")

if __name__ == "__main__":
    command_injection()
    create_insecure_file()
    sql_injection()
    weak_hashing()
    insecure_token()
    open_redirect()
