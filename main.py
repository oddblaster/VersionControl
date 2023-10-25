#Chuyang Zhang
def print_menu():
    print("Menu \n-------------\n1. Encode\n2. Decode\n3. Quit")

def decode_password(password):
    output = ""
    for digit in password:
        decoded_digit = int(digit) - 3
        if decoded_digit < 0:
            output += str(decoded_digit + 10)
        else:
            output += str(decoded_digit)
    print(password)
    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    password = ""
    encoded_password = ""
    while True:
        print_menu()
        userinput = input("Please enter an option")
        if userinput == "1":
            password = input("Please enter your password to encode:")

            for i in range(len(password)):
                 encoded_password = encoded_password + str(int(password[i]) + 3)
            print("Your password has been encoded and stored!")

        if userinput == "2":
            print(f"The encoded password is {encoded_password}, and the original password is {decode_password(encoded_password)}.")
        if userinput == "3":
            break
