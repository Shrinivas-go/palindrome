import sys
if len(sys.argv) < 2:
    print("Usage: python palindrome.py <string>")
    sys.exit(1)
string = sys.argv[1]
if string == string[::-1]:
    print("Palindrome")
else: 
    print("Not a Palindrome")

