def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

def user_input():
    name = input('Enter your name: ')
    return name
print(greetings(user_input))