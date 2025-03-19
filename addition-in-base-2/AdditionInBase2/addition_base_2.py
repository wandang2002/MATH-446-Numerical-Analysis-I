import numpy as np 

def add_integral(x, y):
    '''Adds two integers in base 2
    Arguments:
    x, y: numpy array representing two positive intergers in base 2
    Returns:
    z: a vector representing the sum of x and y in base 2
    '''
    # Without loss of generality, we assume that x is longer than y
    if len(x) < len(y):
        x, y = y, x
    # Inverse the array
    x = x[::-1]
    # Pad the shorter array with zeros
    y = np.pad(y[::-1], (0, len(x) - len(y)))
    # Intialized the carry
    carry = 0
    # Intialized the result
    z = []
    # Loop through the array
    for i in range(len(x)):
        # Calculate the sum
        s = x[i] + y[i] + carry
        # Append the result to the list
        z.append(s % 2)
        # Update the carry
        carry = s // 2
    # If there is a carry left
    if carry:
        z.append(carry)
    # Return the result
    return np.array(z[::-1])

def add_fractional(x,y):
    '''
    Adds two fractions in base 2
    Arguments:
    x, y: numpy array representing two positive fractions in base 2
    Returns:
    I: integer part of the sum
    F: fractional part of the sum
    '''
    # WLOG, we assume that x is longer than y
    if len(x) < len(y):
        x, y = y, x
    # Inverse the array
    x = x[::-1]
    # Pad the shorter array with zeros
    y = np.pad(y, (0, len(x) - len(y)))
    y = y[::-1]
    # Initialize the carry
    carry = 0
    # Initialize the result
    F = []
    # Loop through the array
    for i in range(len(x)):
        # Calculate the sum
        s = x[i] + y[i] + carry
        # Append the result to the list
        F.append(s % 2)
        # Update the carry
        carry = s // 2
    return carry, np.array(F[::-1])

def add_binary(Ix, Fx, Iy, Fy):
    '''
    Adds two binary numbers
    Arguments:
    Ix, Fx: integer and fractional part of the first number
    Iy, Fy: integer and fractional part of the second number
    Returns:
    I: integer part of the sum
    F: fractional part of the sum
    '''
    # Add the fractional part
    carry, F = add_fractional(Fx, Fy)
    # Add the integer part
    I = add_integral(Ix, Iy)
    # If there is a carry left
    if carry:
        I = add_integral(I, np.array([1]))
    return I, F

def main_func(Fx, Fy):
    '''
    Operate on two positive numbers x and y in IEEE single precision
    Assuming intergral parts equal to 1 and an exponent equal to zero
    Arguments:
    Fx, Fy: fractional part of the two numbers
    Returns:
    I: the integral part of the sum of x and y
    F: the fractional part of the sum of x and y
    E: the exponent of the sum of x and y
    '''
    I = 1
    carry, F = add_fractional(Fx, Fy)
    E = 0
    if carry:
        F = np.insert(F, 0, carry)
        E += 1
    if len(F) > 23:
        F = np.delete(F, -1)
    return I, F, E

