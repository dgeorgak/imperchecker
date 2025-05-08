def compare_domains():
    authentic_domain = input("Please enter the authentic domain by copying and pasting it from your web browser(eg. testdomain.io): ")
    suspicious_domain = input("Please enter the domain you want to check by copying and pasting it directly from its source (eg. from the email header): ")

    if authentic_domain == suspicious_domain:
        print("The two domains are identical.")
    else:
        print("The two domains are different. Analyzing differences:")
        len_auth = len(authentic_domain)
        len_susp = len(suspicious_domain)

        if len_auth == len_susp:
            print("Comparing character by character:")
            char_diff_found_at_same_length = False
            for i in range(len_auth):
                if authentic_domain[i] != suspicious_domain[i]:
                    print(f"Character mismatch at position {i+1}:")
                    print(f"Character in Authentic domain is: '{authentic_domain[i]}' (U+{ord(authentic_domain[i]):04X})")
                    print(f"Character in Suspicious domain is: '{suspicious_domain[i]}' (U+{ord(suspicious_domain[i]):04X})")
                    char_diff_found_at_same_length = True
# TODO: Add cases for:
# difference in length 
#   include case for mixed matching and mismathing chars    
# non-visual char differences


if __name__ == "__main__":
    compare_domains()
