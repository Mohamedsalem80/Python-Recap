# Read a complex number from the user input
complex_number_str = input("Please enter a complex number: ")

# Convert the input string into a complex number object
complex_number = complex(complex_number_str)

# Define a function to print the real and imaginary parts of a complex number
def print_complex_parts(complex_num):
    # Print the real part of the complex number
    print("The real part is", complex_num.real)
    # Print the imaginary part of the complex number
    print("The imaginary part is", complex_num.imag)

# Call the function with the user-provided complex number
print_complex_parts(complex_number)