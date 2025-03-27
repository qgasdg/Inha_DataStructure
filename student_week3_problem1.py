import array
class Node:
    def __init__(self):
        self.data =

class Stack:
    '''=======Student's code======='''

def reverse_number_with_stack(number):
    '''=======Student's code======='''

def is_palindrome(number):
    '''=======Student's code======='''


def palindrome_process(number, max_iterations=1000):
    iteration = 0
    print(f"Begin number: {number}")

    while not is_palindrome(number):
        reversed_num = reverse_number_with_stack(number)
        print(f"{number} + {reversed_num} = {number + reversed_num}")
        number += reversed_num
        iteration += 1

        if iteration > max_iterations:
            print("It's not a palindrome. stopping the process.")
            return None

    print(f"Final palindrome: {number} (repeats: {iteration})")
    return number

def main():
    palindrome_process(125)
    palindrome_process(12321)

if __name__ == "__main__":
    main()