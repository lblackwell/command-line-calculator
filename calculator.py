class Calculator(object):
    def __init__(self, last_result=0, input=None):
        self.last_result = last_result
        if input is None:
            self.input = []
        else:
            self.input = input

    def perform_calculation(self):
        if len(self.input) <= 0:
            return

        # Remove whitespace
        # TODO

        # Find multiple-digit numbers
        for i in range(0, len(self.input) - 1):
            try:
                if self.input[i].isdigit():
                    if self.input[i + 1].isdigit():
                        self.input[i] += self.input[i + 1]
                        del(self.input[i + 1])
                        i -= 1
            # We may change the length of the input list
            except IndexError:
                continue

        # Find decimals
        for i in range(0, len(self.input) - 1):
            try:
                if self.input[i] == '.':
                    # Attach it to the surrounding digits
                    to_decrement = 0
                    del_before = False
                    del_after = False
                    if i > 0 and self.input[i - 1].isdigit():
                        self.input[i] = self.input[i - 1] + self.input[i]
                        to_decrement += 1
                    if i < len(self.input) + 1 and self.input[i + 1].isdigit():
                        self.input[i] += self.input[i + 1]
                        to_decrement += 1
                    i -= to_decrement
                    if del_before is True:
                        del(self.input[i - 1])
                    if del_after is True:
                        del(self.input[i + 1])
            except IndexError:
                continue

        # If first piece of input is a digit, start a new calculation
        if self.input[0] is not None and self.input[0].isdigit():
            self.last_result = float(self.input[0])

        # Clear input
        self.input = []


    def print_output(self):
        print self.last_result

    def get_input(self):
        char = raw_input()
        if char.lower() == 'q':
            return False
        elif char == '=':
            self.perform_calculation()
            self.print_output()
        else:
            self.input.append(char)

        return True


def main():
    calc = Calculator()
    run = False
    while run is True:
        run = calc.get_input()


if __name__ == '__main__':
    main()
