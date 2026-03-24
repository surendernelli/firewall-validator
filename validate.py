import sys

def validate_ip(ip):
    ip_parts = ip.split(".")

    if len(ip_parts) != 4:
        return False

    for part in ip_parts:
        try:
            num = int(part)
        except:
            return False

        if num < 0 or num > 255:
            return False

    return True


def validate_port(port):
    try:
        num = int(port)
    except:
        return False

    if num < 1 or num > 65535:
        return False

    return True


def validate_protocol(protocol):
    allowed = ["tcp", "udp", "http", "https"]

    if protocol not in allowed:
        return False

    return True


# Read file
with open("rule.txt", "r") as file:
    data = file.read()

lines = data.splitlines()

rule = {}

for line in lines:
    key, value = line.split("=")
    rule[key] = value

source = rule["source"]
destination = rule["destination"]
port = rule["port"]
protocol = rule["protocol"]


if validate_ip(source) and validate_ip(destination) and validate_port(port) and validate_protocol(protocol):
    print("Valid rule")
else:
    print("Invalid rule")
    sys.exit(1)
