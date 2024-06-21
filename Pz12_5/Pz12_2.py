#Составить генератор (yield), который переведет символы строки из нижнего
#регистра в верхний.
def to_uppercase_generator(input_string):
    for char in input_string:
        if char.islower():
            yield char.upper()
        else:
            yield char


input_string = "abcdefghI"
upper_string = ''.join(to_uppercase_generator(input_string))
print(upper_string)
    