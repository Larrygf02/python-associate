import errno

try:
    f = open('fake.txt', 'r')
except OSError as err:
    if err.errno == errno.ENOENT:
        print("File not found")
    elif err.errno == errno.EACCES:
        print("Bad permissions")
