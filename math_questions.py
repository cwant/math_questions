import sys
import random
import argparse

def process_arguments():
    parser = argparse.ArgumentParser(description='Ask math questions')
    parser.add_argument('--addition', dest='make_question',
                        action='store_const',
                        const=make_addition_question,
                        default=make_addition_question,
                        help='Ask addition questions')
    parser.add_argument('--subtraction', dest='make_question',
                        action='store_const',
                        const=make_subtraction_question,
                        default=make_addition_question,
                        help='Ask subtraction questions')
    parser.add_argument('--multiplication', dest='make_question',
                        action='store_const',
                        const=make_multiplication_question,
                        default=make_addition_question,
                        help='Ask multiplication questions')

    args = parser.parse_args()
    return args

def make_addition_question():
    x = random.randrange(0, 11)
    y = random.randrange(0, 11)
    print("{} + {}".format(x, y))

def make_subtraction_question():
    x1 = random.randrange(0, 21)
    y1 = random.randrange(0, 11)
    x = max(x1, y1)
    y = min(x1, y1)
    print("{} - {}".format(x, y))

def make_multiplication_question():
    x = random.randrange(0, 11)
    y = random.randrange(0, 11)
    print("{} x {}".format(x, y))

def main():
    args = process_arguments()
    make_question = args.make_question
    count = 0
    while(True):
        try:
            make_question()
            sys.stdin.readline()
            count += 1
        except KeyboardInterrupt:
            break
    print("You have done {} questions".format(count))

if __name__ == "__main__":
    main()
