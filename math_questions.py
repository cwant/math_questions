import sys
import random
import argparse

class MathQuestions:
    def __init__(self):
        self.make_question = self.make_addition_question
        self.min_value = 0
        self.max_value = 10
        self.must_have = None
        self.squares = False

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

        parser.add_argument('--min', dest='min_value', type=int,
                            default=self.min_value,
                            help='Minimum value')
        parser.add_argument('--max', dest='max_value', type=int,
                            default=self.max_value,
                            help='Maximum value (double for subtraction)')
        parser.add_argument('--must-have', dest='must_have', type=str,
                            default=self.must_have,
                            help='Must have this/these value ' +
                            '(comma separated)')
        parser.add_argument('--squares', dest='squares',
                            default=self.squares,
                            action='store_true',
                            help='Multiplication with squares')

        args = parser.parse_args()
        self.make_question = args.make_question
        self.min_value = args.min_value
        self.max_value = args.max_value

        if args.must_have:
            self.must_have = list(map(int, args.must_have.split(',')))

        self.squares = args.squares
        if self.squares:
            self.make_question = self.make_multiplication_question

        return args

    def make_addition_question(self):
        x = random.randrange(self.min_value, self.max_value + 1)
        y = random.randrange(self.min_value, self.max_value + 1)
        (x, y) = self.generate_must_have(x, y)
        print("{} + {}".format(x, y))

    def make_subtraction_question(self):
        x1 = random.randrange(self.min_value, 2 * self.max_value + 1)
        y1 = random.randrange(self.min_value, self.max_value + 1)
        (x1, y1) = self.generate_must_have(x1, y1)
        x = max(x1, y1)
        y = min(x1, y1)
        print("{} - {}".format(x, y))

    def make_multiplication_question(self):
        x = random.randrange(self.min_value, self.max_value + 1)
        if self.squares:
            y = x
        else:
            y = random.randrange(self.min_value, self.max_value + 1)
        (x, y) = self.generate_must_have(x, y)
        print("{} x {}".format(x, y))

    def generate_must_have(self, x, y):
        if self.must_have is None:
            return (x, y)
        must_have = self.must_have[0]
        if len(self.must_have) > 1:
            must_have = random.choice(self.must_have)

        if random.randrange(0, 2) == 0:
            return (must_have, y)
        return (x, must_have)
        
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
