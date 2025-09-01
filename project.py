## My Improved character set.
CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!?.,"

def get_mode():
    while True:
        response = input("Would you like to (e)ncrypt or (d)ecrypt? (e/d): ").lower()
        if response.startswith("e"):
            return "encrypt"
        elif response.startswith("d"):
            return "decrypt"
        else:
            print("Please enter either 'e' or 'd'.")

def get_key():
    limitkey = len(CHARSET) - 1
    while True:
        response = input(f"Please enter the key (0 to {limitkey}) to use: ").upper()
        if not response.isdecimal():
            continue
        key = int(response)
        if 0 <= key < len(CHARSET):
            return key

def get_message(mode):
    return input(f"Enter the message to {mode}: ")

def caesar_cipher(message, key, mode):
    message = message.upper()
    translated = ""

    for char in message:
        if char in CHARSET:
            num = CHARSET.find(char)
            if mode == "encrypt":
                num += key
            elif mode == "decrypt":
                num -= key

            if num >= len(CHARSET):
                num -= len(CHARSET)
            elif num < 0:
                num += len(CHARSET)


            translated += CHARSET[num]
        else:
            translated = translated + CHARSET

    return translated

def main():
    mode = get_mode()
    key = get_key()
    message = get_message(mode)
    result = caesar_cipher(message, key, mode)
    print(f"\n{mode.title()}ed message: {result}")

if __name__ == "__main__":
    main()

