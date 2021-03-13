# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:31:38 2021

@author: Charles
"""

def main():
    
    def calculate(input1, operator, input2):
        output = 0
        if operator == "+":
            output = input1 + input2
        elif operator == "-":
            output = input1 - input2
        elif operator == "x":
            output = input1 * input2
        elif operator == "/":
            output - input1 / input2
        return output
    
    def start_calculation():
        first_number = float(input("Please enter the first number: "))
        chosen_operator = input("Please select an operator (+,-,x,/): ").lower()
        second_number = float(input("Please select the second number: "))
        answer = calculate(first_number, chosen_operator, second_number)
        print(f"The answer is: {answer}")
        _continue = input("Would you like to continue with your answer as the first number? Y or N \n").lower()    
    
        if _continue == "y":
            continue_calculation(answer)
        else:
            new_calc = input("Would you like to do a new calculation? Y or N \n").lower()
            if new_calc == "y":
                    start_calculation()

    def continue_calculation(input1):
        print(f"Continuing with {input1}")
        chosen_operator = input("Please select an operator (+,-,x,/): ").lower()
        second_number = float(input("Please select the second number"))       
        answer = calculate(input1, chosen_operator, second_number)
        print(f"The answer is: {answer}")
        print(f"The answer is: {answer}")
        _continue = input("Would you like to continue with your answer as the first number? Y or N \n").lower()    
    
        if _continue == "y":
            continue_calculation(answer)
        else:
            new_calc = input("Would you like to do a new calculation? Y or N \n").lower()
            if new_calc == "y":
                start_calculation()        
        
    print("Welcome to PyCalculator")
    start_calculation()
    


            


if __name__ == "__main__":
  main()        