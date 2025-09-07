#!/usr/bin/env python3
"""
Demonstration script for the Infix to Postfix Calculator

This script shows various examples of converting infix expressions to postfix
and evaluating them, demonstrating the power of stack-based expression evaluation.
"""

from InfixToPostfixCalculator import InfixToPostfixCalculator


def demonstrate_basic_operations():
    """Demonstrate basic arithmetic operations."""
    print("=" * 60)
    print("BASIC ARITHMETIC OPERATIONS")
    print("=" * 60)
    
    calculator = InfixToPostfixCalculator()
    
    basic_operations = [
        "2 + 3",
        "10 - 4",
        "6 * 7",
        "20 / 5"
    ]
    
    for expression in basic_operations:
        result = calculator.solve(expression)
        postfix, _ = calculator.calculate(expression)
        print(f"Infix:  {expression}")
        print(f"Postfix: {postfix}")
        print(f"Result:  {result}")
        print()


def demonstrate_operator_precedence():
    """Demonstrate operator precedence handling."""
    print("=" * 60)
    print("OPERATOR PRECEDENCE")
    print("=" * 60)
    
    calculator = InfixToPostfixCalculator()
    
    precedence_examples = [
        ("2 + 3 * 4", "Multiplication has higher precedence than addition"),
        ("3 * 4 + 2", "Same result, different order of operations"),
        ("10 / 2 + 3 * 4", "Division and multiplication before addition"),
        ("2 + 3 * 4 - 6 / 2", "Complex precedence example")
    ]
    
    for expression, explanation in precedence_examples:
        result = calculator.solve(expression)
        postfix, _ = calculator.calculate(expression)
        print(f"Expression: {expression}")
        print(f"Explanation: {explanation}")
        print(f"Postfix: {postfix}")
        print(f"Result: {result}")
        print()


def demonstrate_parentheses():
    """Demonstrate parentheses handling."""
    print("=" * 60)
    print("PARENTHESES HANDLING")
    print("=" * 60)
    
    calculator = InfixToPostfixCalculator()
    
    parentheses_examples = [
        ("(2 + 3) * 4", "Parentheses force addition before multiplication"),
        ("2 + (3 * 4)", "Parentheses around multiplication (same as no parentheses)"),
        ("((2 + 3) * 4) + 1", "Nested parentheses"),
        ("10 / (2 + 3) * 4", "Parentheses in denominator")
    ]
    
    for expression, explanation in parentheses_examples:
        result = calculator.solve(expression)
        postfix, _ = calculator.calculate(expression)
        print(f"Expression: {expression}")
        print(f"Explanation: {explanation}")
        print(f"Postfix: {postfix}")
        print(f"Result: {result}")
        print()


def demonstrate_complex_expressions():
    """Demonstrate complex mathematical expressions."""
    print("=" * 60)
    print("COMPLEX EXPRESSIONS")
    print("=" * 60)
    
    calculator = InfixToPostfixCalculator()
    
    complex_examples = [
        ("2 + 3 * 4 - 6 / 2", "Multiple operations with precedence"),
        ("(2 + 3) * (4 - 1)", "Two parenthesized expressions multiplied"),
        ("10 / (2 + 3) * 4", "Division with parenthesized denominator"),
        ("3.5 * 2 + 1.5", "Decimal numbers"),
        ("123 + 456", "Large numbers")
    ]
    
    for expression, explanation in complex_examples:
        result = calculator.solve(expression)
        postfix, _ = calculator.calculate(expression)
        print(f"Expression: {expression}")
        print(f"Explanation: {explanation}")
        print(f"Postfix: {postfix}")
        print(f"Result: {result}")
        print()


def demonstrate_error_handling():
    """Demonstrate error handling."""
    print("=" * 60)
    print("ERROR HANDLING")
    print("=" * 60)
    
    calculator = InfixToPostfixCalculator()
    
    error_examples = [
        ("10 / 0", "Division by zero"),
        ("(2 + 3", "Mismatched parentheses (missing closing)"),
        ("2 + 3)", "Mismatched parentheses (missing opening)"),
        ("2 +", "Insufficient operands"),
        ("2 % 3", "Unknown operator")
    ]
    
    for expression, error_type in error_examples:
        try:
            result = calculator.solve(expression)
            print(f"Expression: {expression}")
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Expression: {expression}")
            print(f"Error: {e}")
        print()


def demonstrate_step_by_step():
    """Demonstrate step-by-step conversion process."""
    print("=" * 60)
    print("STEP-BY-STEP CONVERSION PROCESS")
    print("=" * 60)
    
    calculator = InfixToPostfixCalculator()
    
    expression = "2 + 3 * 4"
    print(f"Original infix expression: {expression}")
    print()
    
    # Show tokenization
    tokens = calculator._tokenize(expression)
    print(f"Tokenization: {tokens}")
    print()
    
    # Show conversion to postfix queue
    postfix_queue = calculator._parseInfixToPostfix(expression)
    print(f"Postfix queue created: {type(postfix_queue).__name__}")
    print()
    
    # Show postfix string representation
    postfix_str = calculator._queue_to_string(postfix_queue)
    print(f"Postfix string: {postfix_str}")
    print()
    
    # Show evaluation
    result = calculator._evaluatePostfix(postfix_queue)
    print(f"Postfix evaluation: {result}")
    print()
    
    print("The process works as follows:")
    print("1. Tokenize the expression into numbers and operators")
    print("2. Use a stack to convert infix to postfix (Shunting Yard algorithm)")
    print("3. Store postfix terms in a queue as objects (Doubles for operands, Characters for operators)")
    print("4. Use a stack to evaluate the postfix expression")
    print()


def demonstrate_algorithm_comparison():
    """Demonstrate the difference between infix and postfix evaluation."""
    print("=" * 60)
    print("ALGORITHM COMPARISON")
    print("=" * 60)
    
    calculator = InfixToPostfixCalculator()
    
    expression = "(2 + 3) * 4"
    result = calculator.solve(expression)
    postfix, _ = calculator.calculate(expression)
    
    print(f"Infix expression: {expression}")
    print(f"Postfix expression: {postfix}")
    print(f"Result: {result}")
    print()
    
    print("Why use postfix notation?")
    print("- No need for parentheses or precedence rules")
    print("- Can be evaluated using a simple stack")
    print("- More efficient for computer evaluation")
    print("- Eliminates ambiguity in expression evaluation")
    print()
    
    print("The Shunting Yard algorithm (infix to postfix):")
    print("1. Read tokens from left to right")
    print("2. If token is a number, output it")
    print("3. If token is an operator:")
    print("   - Pop operators from stack with higher precedence")
    print("   - Push current operator to stack")
    print("4. If token is '(', push to stack")
    print("5. If token is ')', pop operators until '('")
    print("6. At end, pop all remaining operators")
    print()
    
    print("Postfix evaluation algorithm:")
    print("1. Read tokens from left to right")
    print("2. If token is a number, push to stack")
    print("3. If token is an operator:")
    print("   - Pop two operands from stack")
    print("   - Apply operator")
    print("   - Push result back to stack")
    print("4. Final result is the only value on stack")


def demonstrate_method_structure():
    """Demonstrate the new method structure."""
    print("=" * 60)
    print("METHOD STRUCTURE")
    print("=" * 60)
    
    calculator = InfixToPostfixCalculator()
    
    print("The calculator now has the following method structure:")
    print()
    print("1. solve(equation): Main method that calls parseInfixToPostfix() then evaluatePostfix()")
    print("2. _parseInfixToPostfix(equation): Converts infix to postfix, stores in queue")
    print("3. _evaluatePostfix(postfixQueue): Evaluates the postfix queue")
    print("4. _precedenceOf(theOp): Helper function for operator precedence")
    print("5. _executeOperation(op, op1, op2): Helper function for binary operations")
    print()
    
    # Demonstrate the solve method
    expression = "2 + 3 * 4"
    result = calculator.solve(expression)
    print(f"Using solve('{expression}'): {result}")
    print()
    
    # Demonstrate the individual methods
    postfix_queue = calculator._parseInfixToPostfix(expression)
    print(f"Using _parseInfixToPostfix('{expression}'): Queue with {postfix_queue.get_count()} items")
    
    result = calculator._evaluatePostfix(postfix_queue)
    print(f"Using _evaluatePostfix(): {result}")
    print()
    
    # Demonstrate helper methods
    precedence = calculator._precedenceOf("*")
    print(f"Using _precedenceOf('*'): {precedence}")
    
    operation_result = calculator._executeOperation("+", 5, 3)
    print(f"Using _executeOperation('+', 5, 3): {operation_result}")


def main():
    """Main demonstration function."""
    print("INFIX TO POSTFIX CALCULATOR DEMONSTRATION")
    print("This demonstration shows how mathematical expressions are converted")
    print("from infix notation to postfix notation and evaluated using stacks and queues.")
    print()
    
    try:
        demonstrate_basic_operations()
        demonstrate_operator_precedence()
        demonstrate_parentheses()
        demonstrate_complex_expressions()
        demonstrate_error_handling()
        demonstrate_step_by_step()
        demonstrate_algorithm_comparison()
        demonstrate_method_structure()
        
        print("=" * 60)
        print("DEMONSTRATION COMPLETE")
        print("=" * 60)
        print()
        print("Key takeaways:")
        print("- Stacks are essential for expression parsing and evaluation")
        print("- Queues are used to store postfix terms as objects")
        print("- Postfix notation eliminates the need for precedence rules")
        print("- The Shunting Yard algorithm efficiently converts infix to postfix")
        print("- Stack-based evaluation is simple and efficient")
        print("- This approach is used in many programming languages and calculators")
        print()
        print("Method Structure:")
        print("- solve(): Main entry point")
        print("- _parseInfixToPostfix(): Converts infix to postfix queue")
        print("- _evaluatePostfix(): Evaluates postfix queue")
        print("- _precedenceOf(): Helper for operator precedence")
        print("- _executeOperation(): Helper for binary operations")
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main() 