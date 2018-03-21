import unittest
import calculator


class TestCalculator(unittest.TestCase):
    # Input
    def test_no_ops(self):
        # Single digit
        c = calculator.Calculator(input=['5'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 5)

        # Double-digit integer
        c = calculator.Calculator(input=['4', '5'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 45)

        # Multiple-digit decimal
        c = calculator.Calculator(input=['4', '5', '.', '6', '7'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 45.67)

    # Addition
    def test_addition(self):
        # All positive
        c = calculator.Calculator(input=['1', '+', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3)

        # Add negative to positive
        c = calculator.Calculator(input=['3', '+', '-', '1'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 2)

        # Add positive to negative
        c = calculator.Calculator(input=['-', '1', '+', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 2)

        # Get a negative result
        c = calculator.Calculator(input=['1', '+', '-', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -2)

        # With decimals
        c = calculator.Calculator(input=['1', '.', '4', '+', '2', '.', '5'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3.9)

    # Subtraction
    def test_subtraction(self):
        # All positive
        c = calculator.Calculator(input=['3', '-', '1'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 2)

        # Subtract negative from positive
        c = calculator.Calculator(input=['3', '-', '-', '1'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 4)

        # Subtract positive from negative (bonus: negative result)
        c = calculator.Calculator(input=['-', '1', '-', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -4)

        # With decimals
        c = calculator.Calculator(input=['4', '.', '2', '-', '1', '.', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 2.9)

    # Multiplication
    def test_multiplication(self):
        # All positive
        c = calculator.Calculator(input=['3', '*', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 6)

        # Multiply positive by negative
        c = calculator.Calculator(input=['3', '*', '-', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -6)

        # Multiply two negatives
        c = calculator.Calculator(input=['-', '3', '*', '-', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 6)

        # With decimals
        c = calculator.Calculator(input=['3', '.', '1', '*', '2', '.', '5'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 7.75)

    # Division
    def test_division(self):
        # All positive
        c = calculator.Calculator(input=['6', '/', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3)

        # Divide positive by negative
        c = calculator.Calculator(input=['6', '/', '-', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -3)

        # Divide two negatives
        c = calculator.Calculator(input=['-', '6', '/', '-', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3)

        # With decimals
        c = calculator.Calculator(input=['7', '/', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3.5)

    # Multiple operations
    def test_multiple_same_operations(self):
        # Addition
        c = calculator.Calculator(input=['1', '+', '2', '+', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 6)

        # Subtraction
        c = calculator.Calculator(input=['8', '-', '2', '-', '1'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 5)

        # Multiplication
        c = calculator.Calculator(input=['4', '*', '2', '*', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 24)

        # Division
        c = calculator.Calculator(input=['24', '/', '3', '/', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 4)

    # Order of operations
    def test_order_of_operations(self):
        # All positive
        c = calculator.Calculator(input=['1', '+', '2', '*', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 7)

        # Including negatives
        c = calculator.Calculator(input=['-', '1', '+', '2', '*', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 5)

    # Continuing from previous line
    def test_continuing_operations(self):
        # All positive
        c = calculator.Calculator(last_result=4, input=['+', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 6)

        # Including negatives
        c = calculator.Calculator(last_result=2, input=['-', '6'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -4)
