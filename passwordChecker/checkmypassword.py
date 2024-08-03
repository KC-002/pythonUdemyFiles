import requests
import hashlib
import sys
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching {res.status_code}, try again.')
    return res


def get_pass_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines(':'))
    for h, counts in hashes:
        #print(h, counts)
        if h == hash_to_check:
            # print(h, counts)
            return counts
    return 0
def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1_password[:5], sha1_password[5:]
    # print(first5, tail)

    response = request_api_data(first5)
    print(response)

    return get_pass_leaks_count(response, tail)

# pwned_api_check('hello')

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} is been used by {count} times. You should probably change the password.\n')

        else:
            print(f'{password} is perfect.\n')

if __name__ == '__main__':
    with open('pass_file.txt', 'r+') as passlist:
        read = passlist.read()
        new_list = read.split(' ')
        main(new_list)