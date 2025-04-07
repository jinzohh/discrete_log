#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Python program calculates the discrete log problem.

import math

def euc(a, b):
    # This function calculates the GCD using recursion method.
    # Find the modulus of a and b.
    r = a % b
    
    # If remainder does not equal 0, call the euc() function again. If remainder equals 0, return b which is the GCD.
    if r != 0:
        result = euc(b, r)
    else:
        result = b

    return result

def zp(num):
    # This function calculates all values mod num relatively prime to num.
    result = []

    for i in range(1, num+1):
        gcd = euc(num, i)
        if gcd == 1:
            result.append(i)
        else:
            continue

    return result

def is_prime(num):
    # This function check whether num is prime.
    if num <= 1:
        result = False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
            else:
                continue

        result = True

    return result

def easy_form(num):
    # This function checks whether p is of the form 2q+1.
    q = (num - 1) / 2

    if q % int(q) == 0:
        is_int = True
    else:
        is_int = False
    
    if is_int == True:
        check = is_prime(q)
        return check
    else:
        return False

def generator(num, zp):
    # This function finds all factors of p-1 and checks each factor whether its a generator.
    check = easy_form(num)
    
    if check:
        factors = []
        generators = []
        p_minus_one = num - 1

        for i in range(1, p_minus_one+1):
            if p_minus_one % i == 0:
                factors.append(i)
            else:
                continue

        print("\nFactors of p-1 are:", factors)

        for i in zp:
            # Excluding factors 1 and p-1. 
            # For factor of 1, k = p-1, and every value raised to the Euler's totient (p-1) is equal to 1, so trivial.
            # For factor of p-1, k = 1, and every value except for 1 does not equal 1, so trivial, again.
            for j in factors[1:len(factors)-1]:
                k = int(p_minus_one / j)
                g_check = pow(i, k, num) != 1
                
                if g_check == False:
                    break

            if g_check:
                generators.append(i)
            else:
                continue

        return generators
        
    else:
        print("\nModulus is not of the form 2q+1.")
        return None

def discrete_log(g, a, num):
    # This function calculates the discrete log of a.
    for i in range(num):
        k = pow(g, i, num)
        
        if k == a % num:
            return i
        else:
            continue
        
    return None

def main():
    # This is the main function.
    try:
        user_input = int(input("Enter modulus value: "))

        # Getting Zp.
        number_set = zp(user_input)
        print("\nZp =", number_set)

        # Getting generators.
        generators = generator(user_input, number_set)
        print("\nGenerators are: ", generators)

        if generators is not None:
            # Getting the Discrete Log.
            g_input = int(input("\nEnter a generator value: "))
            a_input = int(input("Enter an 'a' value from Zp: "))
    
            if a_input not in number_set or g_input not in generators:
                raise ValueError
            else:
                d_log = discrete_log(g_input, a_input, user_input)
                print("\nDiscrete log of", a_input, "is", d_log)
        else:
            print("\nNo discrete log as there are no generators of mod", user_input)
        
    except ValueError:
        print("\nInvalid input.\n")

if __name__ == "__main__":
    main()


# In[ ]:




