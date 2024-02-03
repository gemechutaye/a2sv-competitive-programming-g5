#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    if len(first) not in range(1, 11):
        print("First name must be inclusively between 1 and 10")
        exit()
        
    if len(last) not in range(1, 11):
        print("Last name must be inclusively between 1 and 10")
        exit()
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)