#!/usr/bin/env python3
"""
Infix to Postfix Calculator

This program converts mathematical expressions from infix notation to postfix notation
and then evaluates the result. It uses stacks to handle operator precedence and
parentheses, and queues to store postfix terms.

Examples:
    Infix: 2 + 3 * 4
    Postfix: 2 3 4 * +
    Result: 14

    Infix: (2 + 3) * 4
    Postfix: 2 3 + 4 *
    Result: 20
"""

from DSAStack import DSAStack
from DSAQueue import CircularQueue


class InfixToPostfixCalculator:
    """
    A calculator that converts infix expressions to postfix and evaluates them.
    
    Supports:
    - Basic arithmetic operations: +, -, *, /
    - Parentheses for grouping
    - Multi-digit numbers
    - Decimal numbers
    - Spaces in expressions
    """
    
    def __init__(self):
        """Initialize the calculator."""
        pass

    def solve(self, equation):
        """
        Main method to solve an infix equation.
        
        Args:
            equation (str): The infix equation to solve
            
        Returns:
            float: The result of the equation
        """
        try:
            # Convert infix to postfix and store in queue
            postfix_queue = self._parseInfixToPostfix(equation)
            
            # Evaluate the postfix expression
            result = self._evaluatePostfix(postfix_queue)
            
            return result
            
        except Exception as e:
            raise ValueError(f"Error solving equation: {e}")

    def _parseInfixToPostfix(self, equation):
        """
        Converts infix form equation into postfix.
        Stores the postfix terms into a queue as Objects.
        Uses Doubles for operands and Characters for operators.
        
        Args:
            equation (str): The infix equation to convert
            
        Returns:
            CircularQueue: Queue containing postfix terms as objects
        """
        # Tokenize the equation
        tokens = self._tokenize(equation)
        
        postfix_queue = CircularQueue()
        operator_stack = DSAStack()
        
        for token in tokens:
            if self._is_operand_token(token):
                # If token is an operand, add it to postfix queue as Double
                postfix_queue.enqueue(float(token))
            
            elif token == '(':
                # If token is opening parenthesis, push to stack
                operator_stack.push(token)
            
            elif token == ')':
                # If token is closing parenthesis, pop operators until '('
                while not operator_stack.is_empty() and operator_stack.top() != '(':
                    postfix_queue.enqueue(operator_stack.pop())
                
                # Pop the '(' from stack
                if not operator_stack.is_empty():
                    operator_stack.pop()
                else:
                    # No matching '(' found
                    raise ValueError("Mismatched parentheses")
            
            elif self._is_operator(token):
                # If token is an operator
                while (not operator_stack.is_empty() and 
                       operator_stack.top() != '(' and 
                       self._precedenceOf(operator_stack.top()) >= self._precedenceOf(token)):
                    postfix_queue.enqueue(operator_stack.pop())
                
                operator_stack.push(token)
            else:
                # Unknown token
                raise ValueError(f"Unknown operator: {token}")
        
        # Pop remaining operators from stack
        while not operator_stack.is_empty():
            if operator_stack.top() == '(':
                raise ValueError("Mismatched parentheses")
            postfix_queue.enqueue(operator_stack.pop())
        
        return postfix_queue

    def _evaluatePostfix(self, postfix_queue):
        """
        Takes the postfixQueue and evaluates it.
        
        Args:
            postfix_queue (CircularQueue): Queue containing postfix terms
            
        Returns:
            float: The result of the evaluation
        """
        operand_stack = DSAStack()
        
        # Create a temporary queue to iterate through the postfix terms
        temp_queue = CircularQueue()
        
        # Copy all items from postfix_queue to temp_queue
        while not postfix_queue.is_empty():
            item = postfix_queue.dequeue()
            temp_queue.enqueue(item)
        
        # Process each term in the queue
        while not temp_queue.is_empty():
            term = temp_queue.dequeue()
            
            if isinstance(term, (int, float)):
                # If term is a number (operand), push to stack
                operand_stack.push(float(term))
            
            elif isinstance(term, str) and self._is_operator(term):
                # If term is an operator, pop operands and apply operation
                if operand_stack.get_count() < 2:
                    raise ValueError("Invalid expression: insufficient operands")
                
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                
                result = self._executeOperation(term, operand1, operand2)
                operand_stack.push(result)
        
        if operand_stack.get_count() != 1:
            raise ValueError("Invalid expression: too many operands")
        
        return operand_stack.pop()

    def _precedenceOf(self, the_op):
        """
        Helper function for parseInfixToPostfix().
        Returns the precedence (as an integer) of the Operator.
        
        Args:
            the_op (str): The operator to check precedence for
            
        Returns:
            int: The precedence level (1 for +/-, 2 for */)
        """
        if the_op in ['+', '-']:
            return 1
        elif the_op in ['*', '/']:
            return 2
        else:
            return 0  # For parentheses and other characters

    def _executeOperation(self, op, op1, op2):
        """
        Helper function for evaluatePostfix().
        Executes the binary operation implied by op.
        
        Args:
            op (str): The operator to apply
            op1 (float): First operand
            op2 (float): Second operand
            
        Returns:
            float: The result of the operation
        """
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op1 - op2
        elif op == '*':
            return op1 * op2
        elif op == '/':
            if op2 == 0:
                raise ValueError("Division by zero")
            return op1 / op2
        else:
            raise ValueError(f"Unknown operator: {op}")

    def _tokenize(self, expression):
        """
        Convert expression string to list of tokens.
        Handles multi-digit numbers and decimal numbers.
        
        Args:
            expression (str): The expression string
            
        Returns:
            list: List of tokens (numbers and operators)
        """
        tokens = []
        current_number = ""
        
        for char in expression:
            if char.isspace():
                # Skip spaces
                continue
            elif self._is_operand(char):
                # Build multi-digit or decimal number
                current_number += char
            else:
                # If we have a number being built, add it to tokens
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
                
                # Add operator or parenthesis
                tokens.append(char)
        
        # Don't forget the last number if there is one
        if current_number:
            tokens.append(current_number)
        
        return tokens

    def _is_operator(self, char):
        """Check if a character is an operator."""
        return char in '+-*/'

    def _is_operand(self, char):
        """Check if a character is an operand (digit or decimal point)."""
        return char.isdigit() or char == '.'

    def _is_operand_token(self, token):
        """Check if a token is an operand (number)."""
        try:
            float(token)
            return True
        except ValueError:
            return False

    def calculate(self, infix_expression):
        """
        Calculate the result of an infix expression.
        This is a convenience method that provides the same interface as before.
        
        Args:
            infix_expression (str): The infix expression to evaluate
            
        Returns:
            tuple: (postfix_expression, result)
        """
        try:
            # Convert to postfix queue
            postfix_queue = self._parseInfixToPostfix(infix_expression)
            
            # Create a string representation of postfix for display
            postfix_str = self._queue_to_string(postfix_queue)
            
            # Create a copy of the queue for evaluation
            eval_queue = CircularQueue()
            temp_queue = CircularQueue()
            
            # Copy items to both queues
            while not postfix_queue.is_empty():
                item = postfix_queue.dequeue()
                eval_queue.enqueue(item)
                temp_queue.enqueue(item)
            
            # Restore original queue
            while not temp_queue.is_empty():
                postfix_queue.enqueue(temp_queue.dequeue())
            
            # Evaluate postfix
            result = self._evaluatePostfix(eval_queue)
            
            return postfix_str, result
            
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {e}")

    def _queue_to_string(self, queue):
        """
        Convert a queue of postfix terms to a string representation.
        
        Args:
            queue (CircularQueue): Queue containing postfix terms
            
        Returns:
            str: String representation of postfix expression
        """
        # Create a temporary queue to iterate through the terms
        temp_queue = CircularQueue()
        terms = []
        
        # Copy all items from queue to temp_queue and collect terms
        while not queue.is_empty():
            item = queue.dequeue()
            temp_queue.enqueue(item)
            if isinstance(item, (int, float)):
                # Convert to string without decimal if it's a whole number
                if item == int(item):
                    terms.append(str(int(item)))
                else:
                    terms.append(str(item))
            else:
                terms.append(item)
        
        # Restore the original queue
        while not temp_queue.is_empty():
            queue.enqueue(temp_queue.dequeue())
        
        return ' '.join(terms)


def main():
    """Main function to run the calculator interactively."""
    calculator = InfixToPostfixCalculator()
    
    print("Infix to Postfix Calculator")
    print("=" * 40)
    print("Enter mathematical expressions in infix notation.")
    print("Supported operations: +, -, *, /")
    print("Use parentheses for grouping.")
    print("Enter 'quit' to exit.")
    print()
    
    # Example expressions
    examples = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "10 / 2 + 3 * 4",
        "3.5 * 2 + 1.5"
    ]
    
    print("Examples:")
    for example in examples:
        try:
            postfix, result = calculator.calculate(example)
            print(f"  {example} = {result} (Postfix: {postfix})")
        except ValueError as e:
            print(f"  {example} = Error: {e}")
    print()
    
    while True:
        try:
            # Get input from user
            expression = input("Enter expression: ").strip()
            
            if expression.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not expression:
                continue
            
            # Calculate result using the new solve method
            result = calculator.solve(expression)
            
            # Also get postfix representation for display
            postfix, _ = calculator.calculate(expression)
            
            # Display results
            print(f"Postfix: {postfix}")
            print(f"Result: {result}")
            print()
            
        except ValueError as e:
            print(f"Error: {e}")
            print()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main() 