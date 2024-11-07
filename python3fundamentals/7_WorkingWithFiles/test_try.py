"""
acronyms = {"LOL":"laughing out loud",
            "IDK":"I don't know",
            "TBH":"to be honest"}

try:
    definition = acronyms["BTW"]
except:
    print("That key does not exist.")
finally:
    print("LOL")
"""

def remainder_division(a, b):
    if b == 0:
        raise Exception("Divisor cannot be 0")
        
    result = a//b
    remainder = a%b
    print(a, "/", b, "is", result, "remainder", remainder)

# Main program
remainder_division(10, 0)
