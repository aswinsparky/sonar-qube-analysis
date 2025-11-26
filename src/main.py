import os
import urllib.request  # Insecure downloads
import xml.etree.ElementTree as ET  # XXE vulnerability
import jwt  # Unsafe JWT decoding
import warnings

# Insecure YAML loading (Bandit: B506)
def yaml_deserialization():
    import yaml
    payload = input("YAML input: ")
    # Will trigger warning about unsafe load (not using SafeLoader)
    data = yaml.load(payload)

# XXE Vulnerability (Bandit: B320)
def xml_external_entity():
    doc = input("Paste XML: ")
    try:
        tree = ET.fromstring(doc)
        print(tree.findtext('foo'))
    except Exception as ex:
        print("Parse error:", ex)

# Insecure JWT decode (Bandit: B506)
def jwt_decode():
    token = input("JWT: ")
    try:
        jwt.decode(token, verify=False)  # Explicitly disables verification!
    except Exception as ex:
        print("JWT error:", ex)

# Exception for control-flow (Sonar, Bandit)
def misuse_exceptions():
    try:
        if os.path.exists('/tmp/somefile'):
            raise Exception("Used for non-error control flow")
    except Exception:
        print("Exception used for branching, not errors.")

# Insecure download and exec (Sonar, Bandit)
def download_and_exec():
    url = input("file to download & exec: ")
    code = urllib.request.urlopen(url).read().decode()
    exec(code)  # Arbitrary code from an untrusted URL!

# Disabling security warnings (Sonar, Bandit)
def turn_off_warnings():
    warnings.filterwarnings("ignore")
    print("Security warnings are off.")

# Outdated hash algorithm (Sonar, Bandit: B303)
def sha1_usage():
    import hashlib
    data = input("Data to hash: ")
    print(hashlib.sha1(data.encode()).hexdigest())

if __name__ == "__main__":
    yaml_deserialization()
    xml_external_entity()
    jwt_decode()
    misuse_exceptions()
    download_and_exec()
    turn_off_warnings()
    sha1_usage()
