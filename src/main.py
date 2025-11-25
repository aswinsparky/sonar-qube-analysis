import os
import pickle  # Still dangerous when deserializing untrusted data

# Hardcoded credentials (Bandit: B105, SonarQube: sensitive data)
DB_PASSWORD = "SuperSecret456"

def insecure_eval():
    cmd = input("Type a Python expression: ")
    eval(cmd)  # Bandit: B307 - Arbitrary code execution

def insecure_pickle():
    payload = input("Insert raw pickle bytes: ")
    pickle.loads(payload)  # Bandit: B301 - unsafe deserialization

def hardcoded_secret():
    token = "xyz987token"  # Bandit/SonarQube issue: hardcoded secret
    print("Using token...")

def bad_naming():
    Wrong_variableName = 100  # SonarQube: non-conventional name
    return Wrong_variableName

def duplicate_code():
    total1 = 0
    for i in range(5):
        total1 += i

    total2 = 0
    for i in range(5):
        total2 += i

    return total1 * total2  # Sonar: duplicated logic

def possible_bug():
    number = None
    if number < 10:  # SonarQube: TypeError risk (None < int)
        print("Unexpected bug!")

    # Unreachable code
    return
    print("You cannot reach me")

def empty_except():
    try:
        value = int("abc")  # Will throw
    except:
        pass  # Bandit: B110 - bare except

if __name__ == "__main__":
    insecure_eval()
    insecure_pickle()
    hardcoded_secret()
    bad_naming()
    duplicate_code()
    possible_bug()
    empty_except()
