import getch

class Calculator(object):
    def __init__(self, last_result=0, input=None):
        """Command line calculator. Takes input until 'q' or '=' is entered,
        then either quits ('q') or evaluates the previous input ('=').

        Args:
            last_result (float): Result of the last completed calculation. Used
                for testing. Defaults to 0.
            input (List[char]): User input in the form of a list of single
                characters. Example: ['1', '+', '2']. Used for testing. If no
                list is given, an empty list is used. Defaults to None.
        """
        self.last_result = last_result
        if input is None:
            self.input = []
        else:
            self.input = input

    def _is_number(self, n):
        """Determines whether a string represents a number, including negatives
        (unlike isdigit).

        Args:
            n (str): String to evaluate

        Returns:
            bool: True if the string contains only a positive or negative
                number, otherwise False
        """
        if n.lstrip('-').isdigit():
            return True
        return False

    def _condense_negatives(self):
        """Loops through self.input and condenses any negative signs with their
        corresponding digits. Assumes input starting with a - is a negative,
        rather than a subtraction from the previous result.
        """
        for i in range(0, len(self.input)):
            try:
                if self.input[i] == '-':
                    if i == 0 or self._is_number(self.input[i - 1]) is False:
                        self.input[i] += self.input[i + 1]
                        del(self.input[i + 1])
                        i -= 1
            except IndexError:
                continue

    def _condense_multi_digit_numbers(self):
        """Loops through self.input and condenses any single digits with any
        other adjacent digits.
        """
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

    def _condense_decimals(self):
        """Loops through self.input and condenses any decimal points with their
        surrounding digits.
        """
        for i in range(0, len(self.input)):
            try:
                if self.input[i] == '.':
                    # Attach it to the surrounding digits
                    to_decrement = 0
                    del_before = False
                    del_after = False
                    if i > 0 and self.input[i - 1].isdigit():
                        self.input[i] = self.input[i - 1] + self.input[i]
                        to_decrement += 1
                        del_before = True
                    if i < len(self.input) + 1 and self.input[i + 1].isdigit():
                        self.input[i] += self.input[i + 1]
                        to_decrement += 1
                        del_after = True
                    if del_before is True:
                        del(self.input[i - 1])
                    if del_after is True:
                        del(self.input[i])
                    i -= to_decrement
            except IndexError:
                continue

    def _operate(self, operation, index):
        """Performs the indicated operation on self.input and returns the number
        of indices the calculation discovery loop should decrement (due to
        deleted list items).

        Args:
            operation (char): *, /, +, or - -- the operation to perform
            index (int): The index of self.input currently being evaluated

        Returns:
            int: The number of indices the calling loop should decrement due
                to list items being deleted
        """
        # If this is the first char, multiply current result
        if index == 0:
            first = self.last_result
        # Otherwise, multiply surrounding input
        else:
            first = float(self.input[index - 1])

        if operation == '*':
            self.input[index] = str(first * float(self.input[index + 1]))
        elif operation == '/':
            self.input[index] = str(first / float(self.input[index + 1]))
        elif operation == '+':
            self.input[index] = str(first + float(self.input[index + 1]))
        elif operation == '-':
            self.input[index] = str(first - float(self.input[index + 1]))

        if index == 0:
            del(self.input[index + 1])
            return 1
        else:
            del(self.input[index + 1])
            del(self.input[index - 1])
            return 2

    def _multiply_and_divide(self):
        """Loops through self.input and performs any multiplication and
        division operations in left-to-right order.
        """
        # Look for * or /
        while '*' in self.input or '/' in self.input:
            for i in range(0, len(self.input)):
                try:
                    if self.input[i] in ['*', '/']:
                        i -= self._operate(self.input[i], i)
                except IndexError:
                    continue

    def _add_and_subtract(self):
        """Loops through self.input and performs any addition and subtraction
        operations in left-to-right order.
        """
        while '+' in self.input or '-' in self.input:
            for i in range(0, len(self.input)):
                try:
                    if self.input[i] in ['+', '-']:
                        i -= self._operate(self.input[i], i)
                except IndexError:
                    continue

    def perform_calculation(self):
        """Evaluates any input entered registered '=' was entered. Clears
        input for the next calculation."""
        if len(self.input) <= 0:
            return

        # Remove spaces
        self.input = [x for x in self.input if x != ' ']

        # Find negatives
        self._condense_negatives()

        # Find multiple-digit numbers
        self._condense_multi_digit_numbers()

        # Find decimals
        self._condense_decimals()

        # If first piece of input is a digit, start a new calculation
        if self.input[0] is not None:
            try:
                float(self.input[0])
                self.last_result = 0
            except ValueError:
                pass

        # Perform operations in order -- (PE)MDAS and left-to-right
        self._multiply_and_divide()
        self._add_and_subtract()

        # Save result
        self.last_result = float(self.input[0])

        # Clear input
        self.input = []

    def print_output(self):
        """Prints the latest calculation result to stdout."""
        print(self.last_result)

    def get_input(self):
        """Retrieves input from command line. Accepts input until user enters
        'q', which will quit the program, or '=', which will evaluate entered
        input."""
        char = getch.getch()
        print(char)
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
    run = True
    while run is True:
        run = calc.get_input()


if __name__ == '__main__':
    main()
