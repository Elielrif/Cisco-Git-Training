# Caesar cipher
text = input("Enter your message: ")
ok = False
while not ok:
    number = int(input("enter Number:"))
    if number < 1 or number > 25:
        print("enter a number between 1 and 25")
    else:
        ok = True

cipher = ''

for char in text:
    if not char.isalpha():
        cipher += char

    if char.isupper():
        code = ord(char) +number

        if code > ord('Z'):
            code = code - ord('Z')
            code = ord('A') + code -1
        cipher += chr(code)
    if char.islower():
        code = ord(char) +number
        if code > ord('z'):
            code = code - ord('z')
            code = ord('a') + code -1
        cipher += chr(code)

print(cipher)