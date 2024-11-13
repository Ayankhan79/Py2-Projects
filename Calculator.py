# Functions to add two numbers
def add(x,y):
    return x + y

# Functions to subtract two numbers
def subtract(x,y):
    return x - y

# Functions to multiply two numbers
def multiply(x,y):
    return x * y

# Functions to divide two numbers
def divide(x,y):
    if y==0:
        return "Error! Division by Zero not allowed"
    else:
         return x / y
     
def calculator():
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        #take Input From User;
        choice = input("Enter Choices (1/2/3/4): ")
        
        #Check If Input is One Of these Four Options
        if choice in ['1','2','3','4']:
            num1 = float(input("Enter the First Number: "))
            num2 = float(input("Enter the First Number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1,num2)}")
                
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1,num2)}")
                
            if choice == '3':
                print(f"{num1} * {num2} = {multiply(num1,num2)}")
                
            if choice == '4':
                print(f"{num1} / {num2} = {divide(num1,num2)}")
            
        #Option to Exit Loop
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
        
    print("Exiting Calculator. Goodbye! ")
        
#Calling the calculator function
calculator()
