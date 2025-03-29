import numpy as np

def AddIntegral (x,y) :
    # Put the longer list in first
    if len(x) < len(y) :
        x, y = y, x

    # Inverse the lists
    x = x[::-1]
    # Add in the 0 values to y
    y = y[::-1]
    y = np.append(y, np.zeros(len(x)-len(y)))

    # Initialize the carry and the final result
    carry = 0
    result = []
    
    # Looping through the list and add index by index
    for i in range(len(x)) :
        sum = x[i] + y[i] + carry
        # Add the sum to result (either 1 or 0)
        result.append(sum % 2) #current bit
        carry = sum // 2 #carry bit

    # if there is a carry left over at the end of the list, add it to the result
    if carry : 
        result.append(carry) 

    # inverse the result to get the correct answer
    return result[::-1]

def AddFractional (x,y) :
    # Put the longer list in first
    if len(x) < len(y) :
        x, y = y, x

    # Inverse the lists
    x = x[::-1]
    # Add in the 0 values to y
    # Since it's fractional, we add the 0s after y
    y = np.append(y, np.zeros(len(x)-len(y)))
    y = y[::-1]

    # Initialize the carry and the final result
    carry = 0
    result = []
    
    # Looping through the list and add index by index
    for i in range(len(x)) :
        sum = x[i] + y[i] + carry
        # Add the sum to result (either 1 or 0)
        result.append(sum % 2) #current bit
        carry = sum // 2 #carry bit

    # inverse the result to get the correct answer
    return carry, result[::-1]

def AddBinary (Ix, Fx, Iy, Fy) :
    # First, we add the fractional parts
    carry, F = AddFractional(Fx, Fy)
    
    # Add the integer parts
    I = AddIntegral(Ix, Iy)
    
    # If there is a carry, add it to the integer part
    if carry:
        I = AddIntegral(I, [carry])
    
    
    return I, F

def main(Fx, Fy):
    # Assuming Integral part = 1 and Exponent = 0
    I = 1
    E = 0
    
    # Left most bit is 1
    # The two numbers are in the form of 1.Fx * 2^E and 1.Fy * 2^E
    # This is 24 bits
    I_x = [1] + Fx
    I_y = [1] + Fy
    
    # ADdding the two numbers
    sum = AddIntegral(I_x, I_y)
    
    # the sum will always have 25 bits and >= 2
    # We will get the bits 1-23 as our fractional part
    F_temp = sum[1:24]
    # Since we will have to shift right with 25 bits, E will always >= 1
    E += 1
    # Get the last bit or the rounding bit
    last_bit = sum[24]
    if last_bit == 1:
    # Edge case
    # If the last bit is 1, we need to round up
        F = AddIntegral(F_temp, [1])
    else:
        F = F_temp
    
    return I, F, E


# ===========================
# Example test cases:
# 1. Test AddIntegral
x = [1, 0, 0, 1, 1, 1]
y = [1, 1, 1, 1]
print("AddIntegral(x, y) =", AddIntegral(x, y))
# Expected output: [1, 1, 0, 1, 1, 0]

# 2. Test AddFractional
x_frac = [1, 1, 1, 1]
y_frac = [1, 1, 1]
I_frac, F_frac = AddFractional(x_frac, y_frac)
print("AddFractional(x_frac, y_frac) => I =", I_frac, "F =", F_frac)
# Expected output: I = [1] and F = [1, 1, 0, 1]

# 3. Test AddBinary
Ix = [1, 0, 0, 1, 1, 1]
Iy = [1, 1, 1, 1]
Fx = [1, 1, 1, 1]
Fy = [1, 1, 1]
I_bin, F_bin = AddBinary(Ix, Fx, Iy, Fy)
print("AddBinary(Ix, Fx, Iy, Fy) => I =", I_bin, "F =", F_bin)
# Expected output: I = [1, 1, 0, 1, 1, 1] and F = [1, 1, 0, 1]

# 4. Test main (IEEE single precision addition)
# Example inputs for fractional parts (23 bits each)
Fx_ieee = [0]*22 + [1]      # Only the last bit is 1
Fy_ieee = [1]*23            # All ones
I_ieee, F_ieee, E_ieee = main(Fx_ieee, Fy_ieee)
print("main(Fx_ieee, Fy_ieee) => I =", I_ieee, "F =", F_ieee, "E =", E_ieee)
# Expected output: I = [1], F = [1,0,0,...,0] (23 bits), E = [1]
            
# Other test cases
# 1. Test AddIntegral
x = [1, 0, 1]
y = [1, 1] 
print("AddIntegral(x, y) =", AddIntegral(x, y))

# 2. Test AddFractional
x_frac = [1, 0, 1, 0] 
y_frac = [0, 0, 1]
I_frac, F_frac = AddFractional(x_frac, y_frac)
print("AddFractional(x_frac, y_frac) => I =", I_frac, "F =", F_frac)

# 3. Test AddBinany
Ix = [1, 1, 0]
Iy = [1, 0, 1]
Fx = [1, 1, 1] 
Fy = [1, 0, 1]
I_bin, F_bin = AddBinary(Ix, Fx, Iy, Fy)
print("AddBinary(Ix, Fx, Iy, Fy) => I =", I_bin, "F =", F_bin)

# 4. Test main (IEEE single precision addition)
Fx_ieee = [0] * 22 + [1]
Fy_ieee = [0] * 23
I_ieee, F_ieee, E_ieee = main(Fx_ieee, Fy_ieee)
print("main(Fx_ieee, Fy_ieee) => I =", I_ieee, "F =", F_ieee, "E =", E_ieee)
    
        
        