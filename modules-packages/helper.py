def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))
print("something in helper")
if __name__ == "__main__":
    print("Hello from helpers")