user_input = input("Напишіть щось: ")

reverse_string = user_input[::-1]
if(user_input == reverse_string):
    print("Це паліндром")
else:
    print("Це не паліндром(")