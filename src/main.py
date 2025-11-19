import os

def get_user_password():
    # Hardcoded password (Sensitive Data Exposure)
    password = "SuperSecret123!"
    print("Password is:", password)

def read_file():
    filename = input("Enter filename: ")
    # Command injection vulnerability
    os.system(f"cat {filename}")

def unsafe_eval():
    user_input = input("Enter expression: ")
    print(eval(user_input))

def bad_hash(data):
    import hashlib
    # Insecure hash algorithm for security use
    return hashlib.md5(data.encode()).hexdigest()

if __name__ == "__main__":
    get_user_password()
    read_file()
    unsafe_eval()
    print(bad_hash("test123"))
