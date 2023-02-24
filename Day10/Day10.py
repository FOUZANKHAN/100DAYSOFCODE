from art import logo

# def calc (firstnumber, secondnumber, operand):
#   if operand == "/":
#     return firstnumber/secondnumber
#   elif operand == "*":
#     return firstnumber*secondnumber
#   elif operand == "+":
#     return firstnumber+secondnumber
#   elif operand == "-":
#     return firstnumber-secondnumber
    
# fnumber = int(input("Give me the first number >>  "))
# print("+ \n""* \n""- \n""/ \n")
# operand = input("Select Operation")
# snumber = int(input("Give me the next number >> "))
# result = calc(fnumber,snumber,operand)

# choice = input(f"Type 'y' to continue with the {result}, or type 'n' to start a new calculation")
# if choice == 'y':
#     print("+ \n""* \n""- \n""/ \n")
#     operand = input("Select Operation")
#     snumber = int(input("Give me the next number >> "))
#     result = calc()
# else:
#   exit()
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

operations = {"+":add, 
              "-":subtract,
              "*":multiply, 
              "/":divide
             }
def calc():
  #print(logo)
  flag = True
  num1 = float(input("Give me the first number:   "))
  for key in operations:
    print(key)
  while flag:
    operan = input("choose an operation: ")
    num2 = float(input("Give me the next number: "))
    calc = operations[operan]
    result = calc(num1,num2)
    choice = input(f"Type 'y' to use the {result} or type n to quit: ")
    if choice == 'y':
      num1 = result
    else:
      flag = False
      calc()
#print(f"The result of {num1} and {num2} = {result}")
