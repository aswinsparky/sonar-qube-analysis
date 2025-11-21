import sys
import pickle  # Bandit will flag as risky if used improperly

# Hardcoded password (Bandit: B105; SonarQube: Sensitive info)
PASSWORD = "MySecret123"

def insecure_eval():
    user_input = input("Enter code: ")
    eval(user_input)  # Bandit: B307 (eval used)

def insecure_pickle():
    data = input("Paste pickle data: ")
    pickle.loads(data)  # Bandit: B301, SonarQube: risky deserialization

def hardcoded_secret():
    api_key = "abc123xyz"  # Bandit/SonarQube issue

def bad_naming():
    BADVariableName = 42  # SonarQube code smell
    return BADVariableName

def duplicate_code():
    result = 0
    for n in range(3):
        result += n

    result2 = 0
    for n in range(3):
        result2 += n

    return result + result2

def possible_bug():
    value = None
    if value > 0:  # SonarQube: possible TypeError
        print("Bug!")

    # Unreachable code
    return
    print("Unreachable code")

def empty_except():
    try:
        x = 1 / 0
    except:
        pass  # Bandit: B110 (bare except)

if __name__ == "__main__":
    insecure_eval()
    insecure_pickle()
    hardcoded_secret()
    bad_naming()
    duplicate_code()
    possible_bug()
    empty_except()
