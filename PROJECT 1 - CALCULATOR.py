def calculator():
     while True:
      print("Welcome to Staxtech calculator")
      num1 = int(input("Enter first no:"))
      num2 = int(input("Enter second no:"))
      operation = input("Enter operator for the operation(*,%,+,-):")
      if operation =="*":
       print("Answer:",num1 * num2)
      elif operation == "%":
       print("Answer:",num1 % num2)
      elif operation == "+":
       print("Answer:",num1 + num2)
      elif operation == "-":
       print("Answer:",num1 - num2)
      choice = input("DO you want to continue(y/n):")
      if choice =="n":
        print("Thank you")
        break
      else:
        continue
calculator()