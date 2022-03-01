#__all__ = ['extract_upper'] #It's means that only extract_upper function is imported when you call the module

# If name function starts with underscorde '_' this function is not accesible
def _extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))


if __name__ == "__main__":
    print("Hello from helpers")