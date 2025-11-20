import os
import hashlib

def hardcoded_password():
    # Hardcoded password (Sensitive data exposure)
    password = "P@ssword123"
    print("The password is:", password)

def command_injection():
    # Command injection vulnerability
    filename = input("Enter file to list: ")
    os.system(f"ls {filename}")

def unsafe_eval():
    # Unsafe eval() (Code injection risk)
    expr = input("Enter a calculation: ")
    print("Result:", eval(expr))

def weak_hash(password):
    # Use of weak hash algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()

def insecure_sql():
    # Insecure SQL query (simulated, not real database code)
    name = input("Username: ")
    pwd = input("Password: ")
    query = "SELECT * FROM users WHERE username='" + name + "' AND password='" + pwd + "'"
    print("Executing:", query)

if __name__ == "__main__":
    hardcoded_password()
    command_injection()
    unsafe_eval()
    print(weak_hash("password"))
    insecure_sql()
