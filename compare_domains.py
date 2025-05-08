def compare_domains():
    authentic_domain = input("Please enter the authentic domain by copying and pasting it from your web browser(eg. testdomain.io): ")
    suspicious_domain = input("Please enter the domain you want to check by copying and pasting it directly from its source (eg. from the email header): ")

    if authentic_domain == suspicious_domain:
        print("The two domains are identical.")
    else:
        print("The two domains are different.")



if __name__ == "__main__":
    compare_domains()
