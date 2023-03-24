
def encode(password):
    string_output = ''
    for num in password:
        if num == '7':
            string_output += '0'
        elif num == '8':
            string_output += '1'
        elif num == '9':
            string_output += '2'
        else:
            output = int(num) + 3
            string_output += str(output)
    return string_output


def decode(encoded_pass):
    back = ''
    for j in encoded_pass:
        back += str((int(j) - 3) % 10)
    return back


def main():
    print('Menu')
    print('-------------')
    print("""1. Encode
2. Decode
3. Quit""")
    print()

    while True:
        option = int(input("Please enter an option: "))
        if option == 1:
            password_encode = input("Please enter your password to encode: ")
            final_value = encode(password_encode)
            print('Your password has been encoded and stored!')
        if option == 2:
            display_value = decode(final_value)
            print('The encoded password is',final_value, 'and the original password is', display_value, '.')
        if option == 3:
            False


if __name__ == '__main__':
    main()

