import sys
import random
import argparse

class MathQuestions:
    def __init__(self):
        self.make_question = self.make_addition_question
        self.max_value = 10

    def process_arguments(self):
        parser = argparse.ArgumentParser(description='Ask math questions')
        parser.add_argument('--addition', dest='make_question',
                            action='store_const',
                            const=self.make_addition_question,
                            default=self.make_question,
                            help='Ask addition questions')
        parser.add_argument('--subtraction', dest='make_question',
                            action='store_const',
                            const=self.make_subtraction_question,
                            default=self.make_question,
                            help='Ask subtraction questions')
        parser.add_argument('--multiplication', dest='make_question',
                            action='store_const',
                            const=self.make_multiplication_question,
                            default=self.make_question,
                            help='Ask multiplication questions')

        parser.add_argument('--max', dest='max_value', type=int,
                            default=self.max_value,
                            help='Maximum value (double for subtraction)')

        args = parser.parse_args()
        self.make_question = args.make_question
        self.max_value = args.max_value

        return args

    def make_addition_question(self):
        x = random.randrange(0, self.max_value + 1)
        y = random.randrange(0, self.max_value + 1)
        print("{} + {}".format(x, y))

    def make_subtraction_question(self):
        x1 = random.randrange(0, 2 * self.max_value + 1)
        y1 = random.randrange(0, self.max_value + 1)
        x = max(x1, y1)
        y = min(x1, y1)
        print("{} - {}".format(x, y))

    def make_multiplication_question(self):
        x = random.randrange(0, self.max_value + 1)
        y = random.randrange(0, self.max_value + 1)
        print("{} x {}".format(x, y))

    def main(self):
        self.process_arguments()

        count = 0
        while(True):
            try:
                self.make_question()
                sys.stdin.readline()
                count += 1
            except KeyboardInterrupt:
                break
        print("You have done {} questions".format(count))

if __name__ == "__main__":
    MathQuestions().main()
