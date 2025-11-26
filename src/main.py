import os
import pickle  # Dangerous (Bandit: B301)
import getpass

# Hardcoded credentials (Bandit: B105/SonarQube)
API_SECRET = "hardcoded_secret_1234"

def unsafe_deserialize():
    # Unsafe user input for pickle (Bandit: B301)
    data = input("Paste pickle bytes: ").encode()
    try:
        pickle.loads(data)
    except Exception as e:
        print("Error:", e)

def hardcoded_password_usage():
    password = "P@ssw0rd!"  # Bandit: B105
    print("Connecting with password:", password)

def directory_traversal():
    # Directory traversal vulnerability
    filename = input("What file in ./private/? ")
    with open(f"./private/{filename}", "r") as f:
        print(f.read())  # User may type '../../../etc/passwd'

def eval_input():
    # Unsafe eval (Bandit: B307)
    user_input = input("Dangerous code: ")
    eval(user_input)

def running_as_root():
    # Dangerous file created as root; file injection possibility
    if os.geteuid() == 0:
        with open('/tmp/pwned.txt', 'w') as f:
            f.write('Root-owned file\n')

def unsafe_tempfile_use():
    # Predictable temp filename (Bandit: B108)
    tmpname = "/tmp/mytempfile.txt"
    with open(tmpname, "w") as f:
        f.write("Temp file, but not secure!\n")
    print("Temporary file at", tmpname)

def bare_except():
    try:
        1 / 0
    except:
        pass  # Bandit: B110

def password_in_log():
    pw = getpass.getpass("Password please: ")
    print(f"LOG: user typed {pw}")  # SonarQube: sensitive data in logs

def unreachable_code():
    print("Do work")
    return
    print("Oops this never runs")  # SonarQube: unreachable

def too_many_branches(val):
    # Cyclomatic complexity (SonarQube)
    if val == 1:
        print("One")
    elif val == 2:
        print("Two")
    elif val == 3:
        print("Three")
    elif val == 4:
        print("Four")
    elif val == 5:
        print("Five")
    else:
        print("Other")

if __name__ == "__main__":
    unsafe_deserialize()
    hardcoded_password_usage()
    directory_traversal()
    eval_input()
    running_as_root()
    unsafe_tempfile_use()
    bare_except()
    password_in_log()
    unreachable_code()
    too_many_branches(3)
