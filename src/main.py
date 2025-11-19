import os
import hashlib

def hardcoded_password():
    # Sensitive data exposure (hardcoded)
    password = "SuperSecret123!"
    print(f"Password is: {password}")

def command_injection():
    # Take input from user, use it directly in a system command (command injection)
    filename = input("Enter filename: ")
    os.system(f"cat {filename}")

def unsafe_eval():
    # Unsafe use of eval(), allows code injection
    user_input = input("Enter a Python expression: ")
    print(eval(user_input))

def bad_hashing(data):
    # Insecure hash algorithm (MD5)
    return hashlib.md5(data.encode()).hexdigest()

def sql_injection():
    # Simulate insecure SQL statement (plain string concatenation, dangerous in real code)
    username = input("Username: ")
    password = input("Password: ")
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    print(f"Simulated query: {query}")  # Would be sent to database in real code

if __name__ == "__main__":
    hardcoded_password()
    command_injection()
    unsafe_eval()
    print(bad_hashing("userpassword"))
    sql_injection()
