first_step = float(input('Enter the first number: '))
second_step = float(input('Enter the second number: '))

action = input('Enter action (+ - / *): ')

if action == '+':
    print(first_step + second_step)
elif action == '-':
    print(first_step - second_step)
elif action == '/':
    if second_step == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(first_step / second_step)
elif action == '*':
    print(first_step * second_step)
else:
    print('Wrong action')