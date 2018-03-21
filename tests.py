import unittest
import calculator


class TestCalculator(unittest.TestCase):
    # Input
    def test_no_ops_single(self):
        # Single digit
        c = calculator.Calculator(input=['5'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 5)

    def test_no_ops_double(self):
        # Double-digit integer
        c = calculator.Calculator(input=['4', '5'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 45)

    def test_no_ops_multiple(self):
        # Multiple-digit decimal
        c = calculator.Calculator(input=['4', '5', '.', '6', '7'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 45.67)

    def test_no_ops_negative(self):
        # Negative single digit
        c = calculator.Calculator(input=['-', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -3)

    # Addition
    def test_addition_positive(self):
        # All positive
        c = calculator.Calculator(input=['1', '+', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 1 + 2)

    def test_addition_neg_to_pos(self):
        # Add negative to positive
        c = calculator.Calculator(input=['3', '+', '-', '1'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3 + -1)

    def test_addition_pos_to_neg(self):
        # Add positive to negative
        c = calculator.Calculator(input=['-', '1', '+', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -1 + 3)

    def test_addition_neg_result(self):
        # Get a negative result
        c = calculator.Calculator(input=['1', '+', '-', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 1 + -3)

    def test_addition_decimals(self):
        # With decimals
        c = calculator.Calculator(input=['1', '.', '4', '+', '2', '.', '5'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 1.4 + 2.5)

    # Subtraction
    def test_subtraction_pos(self):
        # All positive
        c = calculator.Calculator(input=['3', '-', '1'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3 - 1)

    def test_subtraction_neg_from_pos(self):
        # Subtract negative from positive
        c = calculator.Calculator(input=['3', '-', '-', '1'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3 - -1)

    def test_subtraction_pos_from_neg(self):
        # Subtract positive from negative (bonus: negative result)
        c = calculator.Calculator(input=['-', '1', '-', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -1 - 3)

    def test_subtraction_decimals(self):
        # With decimals
        c = calculator.Calculator(input=['4', '.', '2', '-', '1', '.', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 4.2 - 1.3)

    # Multiplication
    def test_multiplication_pos(self):
        # All positive
        c = calculator.Calculator(input=['3', '*', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3 * 2)

    def test_mult_pos_by_neg(self):
        # Multiply positive by negative
        c = calculator.Calculator(input=['3', '*', '-', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3 * -2)

    def test_mult_both_neg(self):
        # Multiply two negatives
        c = calculator.Calculator(input=['-', '3', '*', '-', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -3 * -2)

    def test_mult_decimals(self):
        # With decimals
        c = calculator.Calculator(input=['3', '.', '1', '*', '2', '.', '5'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 3.1 * 2.5)

    # Division
    def test_division(self):
        # All positive
        c = calculator.Calculator(input=['6', '/', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 6 / 2)

    def test_div_pos_by_neg(self):
        # Divide positive by negative
        c = calculator.Calculator(input=['6', '/', '-', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 6 / -2)

    def test_div_two_negs(self):
        # Divide two negatives
        c = calculator.Calculator(input=['-', '6', '/', '-', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -6 / -2)

    def test_div_decimal_result(self):
        # With decimal result
        c = calculator.Calculator(input=['7', '/', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 7 / 2)

    def test_div_decimals(self):
        # With decimal result
        c = calculator.Calculator(input=['2', '.', '4', '2', '/', '1', '.', '1'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 2.42 / 1.1)

    # Multiple operations
    def test_multiple_same_operations(self):
        # Addition
        c = calculator.Calculator(input=['1', '+', '2', '+', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 1 + 2 + 3)

    def test_mult_ops_sub(self):
        # Subtraction
        c = calculator.Calculator(input=['8', '-', '2', '-', '1'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 8 - 2 - 1)

    def test_mult_ops_mult(self):
        # Multiplication
        c = calculator.Calculator(input=['4', '*', '2', '*', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 4 * 2 * 3)

    def test_mult_ops_div(self):
        # Division
        c = calculator.Calculator(input=['24', '/', '3', '/', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 24 / 3 / 2)

    # Order of operations
    def test_order_of_operations(self):
        # All positive
        c = calculator.Calculator(input=['1', '+', '2', '*', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 1 + 2 * 3)

    def test_ooo_neg(self):
        # Including negatives
        c = calculator.Calculator(input=['-', '1', '+', '2', '*', '3'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -1 + 2 * 3)

    # Continuing from previous line
    def test_continuing_operations(self):
        # All positive
        c = calculator.Calculator(last_result=4, input=['+', '2'])
        c.perform_calculation()
        self.assertEqual(c.last_result, 4 + 2)

    def test_continue_neg(self):
        # Including negatives
        c = calculator.Calculator(last_result=2, input=['-', '6'])
        c.perform_calculation()
        self.assertEqual(c.last_result, -6)
