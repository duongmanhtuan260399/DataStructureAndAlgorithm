#!/usr/bin/env python3
"""
Test suite for InfixToPostfixCalculator

This module tests the conversion from infix to postfix notation and
the evaluation of mathematical expressions using the new method structure.
"""

import unittest
from InfixToPostfixCalculator import InfixToPostfixCalculator


class InfixToPostfixCalculatorTest(unittest.TestCase):
    """Test suite for InfixToPostfixCalculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calculator = InfixToPostfixCalculator()

    def test_solve_method(self):
        """Test the main solve method."""
        test_cases = [
            ("2 + 3", 5.0),
            ("5 - 2", 3.0),
            ("4 * 3", 12.0),
            ("10 / 2", 5.0),
            ("2 + 3 * 4", 14.0),
            ("(2 + 3) * 4", 20.0),
        ]
        
        for infix, expected_result in test_cases:
            with self.subTest(infix=infix):
                result = self.calculator.solve(infix)
                self.assertEqual(result, expected_result)

    def test_basic_operations(self):
        """Test basic arithmetic operations."""
        test_cases = [
            ("2 + 3", "2 3 +", 5.0),
            ("5 - 2", "5 2 -", 3.0),
            ("4 * 3", "4 3 *", 12.0),
            ("10 / 2", "10 2 /", 5.0),
        ]
        
        for infix, expected_postfix, expected_result in test_cases:
            with self.subTest(infix=infix):
                postfix, result = self.calculator.calculate(infix)
                self.assertEqual(postfix, expected_postfix)
                self.assertEqual(result, expected_result)

    def test_operator_precedence(self):
        """Test operator precedence handling."""
        test_cases = [
            ("2 + 3 * 4", "2 3 4 * +", 14.0),
            ("3 * 4 + 2", "3 4 * 2 +", 14.0),
            ("10 / 2 + 3 * 4", "10 2 / 3 4 * +", 17.0),
            ("2 + 3 * 4 - 1", "2 3 4 * + 1 -", 13.0),
        ]
        
        for infix, expected_postfix, expected_result in test_cases:
            with self.subTest(infix=infix):
                postfix, result = self.calculator.calculate(infix)
                self.assertEqual(postfix, expected_postfix)
                self.assertEqual(result, expected_result)

    def test_parentheses(self):
        """Test parentheses handling."""
        test_cases = [
            ("(2 + 3) * 4", "2 3 + 4 *", 20.0),
            ("2 + (3 * 4)", "2 3 4 * +", 14.0),
            ("(10 / 2) + (3 * 4)", "10 2 / 3 4 * +", 17.0),
            ("((2 + 3) * 4) + 1", "2 3 + 4 * 1 +", 21.0),
        ]
        
        for infix, expected_postfix, expected_result in test_cases:
            with self.subTest(infix=infix):
                postfix, result = self.calculator.calculate(infix)
                self.assertEqual(postfix, expected_postfix)
                self.assertEqual(result, expected_result)

    def test_complex_expressions(self):
        """Test complex mathematical expressions."""
        test_cases = [
            ("2 + 3 * 4 - 6 / 2", "2 3 4 * + 6 2 / -", 11.0),
            ("(2 + 3) * (4 - 1)", "2 3 + 4 1 - *", 15.0),
            ("10 / (2 + 3) * 4", "10 2 3 + / 4 *", 8.0),
        ]
        
        for infix, expected_postfix, expected_result in test_cases:
            with self.subTest(infix=infix):
                postfix, result = self.calculator.calculate(infix)
                self.assertEqual(postfix, expected_postfix)
                self.assertEqual(result, expected_result)

    def test_decimal_numbers(self):
        """Test decimal number handling."""
        test_cases = [
            ("3.5 + 2.5", "3.5 2.5 +", 6.0),
            ("10.5 / 2.5", "10.5 2.5 /", 4.2),
            ("2.5 * 3.2 + 1.5", "2.5 3.2 * 1.5 +", 9.5),
        ]
        
        for infix, expected_postfix, expected_result in test_cases:
            with self.subTest(infix=infix):
                postfix, result = self.calculator.calculate(infix)
                self.assertEqual(postfix, expected_postfix)
                self.assertAlmostEqual(result, expected_result, places=10)

    def test_multi_digit_numbers(self):
        """Test multi-digit number handling."""
        test_cases = [
            ("123 + 456", "123 456 +", 579.0),
            ("1000 / 100", "1000 100 /", 10.0),
            ("25 * 40 + 15", "25 40 * 15 +", 1015.0),
        ]
        
        for infix, expected_postfix, expected_result in test_cases:
            with self.subTest(infix=infix):
                postfix, result = self.calculator.calculate(infix)
                self.assertEqual(postfix, expected_postfix)
                self.assertEqual(result, expected_result)

    def test_spaces_handling(self):
        """Test that spaces are handled correctly."""
        test_cases = [
            ("2+3", "2 3 +", 5.0),
            ("2 +3", "2 3 +", 5.0),
            ("2+ 3", "2 3 +", 5.0),
            ("  2  +  3  ", "2 3 +", 5.0),
        ]
        
        for infix, expected_postfix, expected_result in test_cases:
            with self.subTest(infix=infix):
                postfix, result = self.calculator.calculate(infix)
                self.assertEqual(postfix, expected_postfix)
                self.assertEqual(result, expected_result)

    def test_division_by_zero(self):
        """Test division by zero error handling."""
        with self.assertRaises(ValueError) as context:
            self.calculator.solve("10 / 0")
        self.assertIn("Division by zero", str(context.exception))

    def test_mismatched_parentheses(self):
        """Test mismatched parentheses error handling."""
        with self.assertRaises(ValueError) as context:
            self.calculator.solve("(2 + 3")
        self.assertIn("Mismatched parentheses", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            self.calculator.solve("2 + 3)")
        self.assertIn("Mismatched parentheses", str(context.exception))

    def test_invalid_expression_insufficient_operands(self):
        """Test invalid expression with insufficient operands."""
        with self.assertRaises(ValueError) as context:
            self.calculator.solve("2 +")
        self.assertIn("insufficient operands", str(context.exception))

    def test_unknown_operator(self):
        """Test unknown operator error handling."""
        with self.assertRaises(ValueError) as context:
            self.calculator.solve("2 % 3")
        self.assertIn("Unknown operator", str(context.exception))

    def test_single_number(self):
        """Test expression with single number."""
        result = self.calculator.solve("42")
        self.assertEqual(result, 42.0)

    def test_negative_numbers(self):
        """Test negative number handling."""
        # Note: This implementation doesn't handle unary minus
        # For negative numbers, they need to be entered as expressions like "0 - 5"
        result = self.calculator.solve("0 - 5")
        self.assertEqual(result, -5.0)

    def test_tokenize_method(self):
        """Test the _tokenize method separately."""
        test_cases = [
            ("2 + 3", ["2", "+", "3"]),
            ("10.5 * 2", ["10.5", "*", "2"]),
            ("(2 + 3) * 4", ["(", "2", "+", "3", ")", "*", "4"]),
            ("  2  +  3  ", ["2", "+", "3"]),
            ("123+456", ["123", "+", "456"]),
        ]
        
        for expression, expected_tokens in test_cases:
            with self.subTest(expression=expression):
                tokens = self.calculator._tokenize(expression)
                self.assertEqual(tokens, expected_tokens)

    def test_precedence_of_method(self):
        """Test the _precedenceOf method."""
        # Test precedence
        self.assertEqual(self.calculator._precedenceOf("+"), 1)
        self.assertEqual(self.calculator._precedenceOf("-"), 1)
        self.assertEqual(self.calculator._precedenceOf("*"), 2)
        self.assertEqual(self.calculator._precedenceOf("/"), 2)
        self.assertEqual(self.calculator._precedenceOf("("), 0)
        self.assertEqual(self.calculator._precedenceOf(")"), 0)

    def test_is_operator_method(self):
        """Test the _is_operator method."""
        operators = ['+', '-', '*', '/']
        non_operators = ['a', '1', '(', ')', ' ', '.', '^']
        
        for op in operators:
            self.assertTrue(self.calculator._is_operator(op))
        
        for char in non_operators:
            self.assertFalse(self.calculator._is_operator(char))

    def test_is_operand_method(self):
        """Test the _is_operand method."""
        operands = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        non_operands = ['a', '+', '-', '*', '/', '(', ')', ' ']
        
        for char in operands:
            self.assertTrue(self.calculator._is_operand(char))
        
        for char in non_operands:
            self.assertFalse(self.calculator._is_operand(char))

    def test_execute_operation_method(self):
        """Test the _executeOperation method."""
        test_cases = [
            ("+", 5.0, 3.0, 8.0),
            ("-", 5.0, 3.0, 2.0),
            ("*", 5.0, 3.0, 15.0),
            ("/", 6.0, 2.0, 3.0),
        ]
        
        for operator, op1, op2, expected in test_cases:
            with self.subTest(operator=operator):
                result = self.calculator._executeOperation(operator, op1, op2)
                self.assertEqual(result, expected)

    def test_edge_cases(self):
        """Test various edge cases."""
        # Empty expression
        with self.assertRaises(ValueError):
            self.calculator.solve("")
        
        # Expression with only spaces
        with self.assertRaises(ValueError):
            self.calculator.solve("   ")
        
        # Expression with only parentheses
        with self.assertRaises(ValueError):
            self.calculator.solve("()")
        
        # Expression with only operators
        with self.assertRaises(ValueError):
            self.calculator.solve("++")

    def test_large_numbers(self):
        """Test with large numbers."""
        result = self.calculator.solve("999999 + 1")
        self.assertEqual(result, 1000000.0)

    def test_floating_point_precision(self):
        """Test floating point precision."""
        result = self.calculator.solve("0.1 + 0.2")
        # Note: 0.1 + 0.2 = 0.30000000000000004 due to floating point precision
        self.assertAlmostEqual(result, 0.3, places=10)

    def test_parse_infix_to_postfix_method(self):
        """Test the _parseInfixToPostfix method directly."""
        from DSAQueue import CircularQueue
        
        # Test basic conversion
        postfix_queue = self.calculator._parseInfixToPostfix("2 + 3 * 4")
        
        # Verify it's a CircularQueue
        self.assertIsInstance(postfix_queue, CircularQueue)
        
        # Convert to string for verification
        postfix_str = self.calculator._queue_to_string(postfix_queue)
        self.assertEqual(postfix_str, "2 3 4 * +")

    def test_evaluate_postfix_method(self):
        """Test the _evaluatePostfix method directly."""
        from DSAQueue import CircularQueue
        
        # Create a postfix queue manually
        postfix_queue = CircularQueue()
        postfix_queue.enqueue(2.0)
        postfix_queue.enqueue(3.0)
        postfix_queue.enqueue(4.0)
        postfix_queue.enqueue("*")
        postfix_queue.enqueue("+")
        
        # Evaluate it
        result = self.calculator._evaluatePostfix(postfix_queue)
        self.assertEqual(result, 14.0)

    def test_queue_to_string_method(self):
        """Test the _queue_to_string method."""
        from DSAQueue import CircularQueue
        
        # Create a queue with mixed types
        queue = CircularQueue()
        queue.enqueue(2.0)
        queue.enqueue(3.0)
        queue.enqueue("+")
        
        # Convert to string
        result = self.calculator._queue_to_string(queue)
        self.assertEqual(result, "2 3 +")


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2) 