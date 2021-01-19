#!/usr/bin/env python3

import sys

# This function adds spaces after a '(' and before a ')' so that we can split on the spaces to get a list of "tokens"
def convert_to_list(expression):
    spaced_string = ""
    for char in expression:
        if(char == '('):
            spaced_string += char + ' '
        elif(char == ')'):
            spaced_string += ' ' + char
        else:
            spaced_string += char

    return spaced_string.split()

# This function returns the next overarching argument in the list of tokens, and deletes them from the list
def get_argument(expression_list):
    # If we have a simple numeric argument, return the value
    if(expression_list[0] != '('):
        return expression_list[0], 1

    # Check for a balanced set of parentheses which would be an argument
    index = 1
    count = 1
    while(count != 0):
        if(expression_list[index] == '('):
            count += 1
        elif(expression_list[index] == ')'):
            count -= 1
        index += 1

    return expression_list[:index], index

# This function takes a list of tokens corresponding to an expression and returns [operation, arg1, arg2, ...argn]
def parse(expression_list):
    formatted_expression = []

    # Store operation
    formatted_expression.append(expression_list[1])
    expression_list = expression_list[2:]

    # Get arguments
    while(len(expression_list) > 1):
        argument, end_index = get_argument(expression_list)
        expression_list = expression_list[end_index:]
        formatted_expression.append(argument)

    return formatted_expression

# This function evaluates an expression and returns the integer value resulting from simplifying the expression
def evaluate(expression_list):
    # Base case when we are given just a number
    if (expression_list[0] != '('):
        return int(expression_list[0])

    formatted_expression = parse(expression_list);
    answer = 0

    # If we wanted to do multiple arguments (i.e. more than 2), we simply iterate through the 
    # formatted_expression and constantly apply the operation.
    # Similarly, any error checking for # of arguments would be done here.
    if(formatted_expression[0] == 'add'):
        answer = evaluate(formatted_expression[1]) + evaluate(formatted_expression[2])
    elif(formatted_expression[0] == 'multiply'):
        answer = evaluate(formatted_expression[1]) * evaluate(formatted_expression[2])
    return answer

def main():
    # Check number of arguments and set to variable
    if (len(sys.argv) - 1 == 0):
        sys.exit("Missing expression")

    expression = sys.argv[1]
    expression_list = convert_to_list(expression);
    answer = evaluate(expression_list)
    print(answer)

if __name__ == '__main__':
    main()
