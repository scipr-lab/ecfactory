import time
from sage.all import is_prime, is_square, power_mod, fundamental_discriminant, log, floor
    
def is_valid_curve(q,t,r,k,D): 
    """
    Description:
    
        Tests that (q,t,r,k,D) is a valid elliptic curve
    
    Input:
    
        q - size of prime field
        t - trace of Frobenius
        r - size of prime order subgroup
        k - embedding degree
        D - (negative) fundamental discriminant
    
    Output:
    
        bool - true iff there exists an elliptic curve over F_q with trace t, a subgroup of order r with embedding degree k, and fundamental discriminant D
    
    """
    if q == 0 or t == 0 or r == 0 or k == 0 or D == 0:
        return False
    if not is_prime(q):
        return False 
    if not is_prime(r):
        return False
    if not fundamental_discriminant(D) == D:
        return False
    if D % 4 == 0: #check CM equation
        if not is_square(4*(t*t - 4*q)//D):
            return False
    if D % 4 == 1:
        if not is_square((t*t - 4*q)//D):
            return False
    if not (q+1-t) % r == 0: #check r | #E(F_q)
        return False
    if not power_mod(q,k,r) == 1: #check embedding degree is k
        return False
    return True

def filter_decorator(f):
    def helper(*args):
        q,t,r,k,D = f(*args)
        num_bits = _number_of_bits(r)
        while not is_suitable_curve(q,t,r,k,D, num_bits):
            q,t,r,k,D = f(*args)
            num_bits = _number_of_bits(r)
        return q,t,r,k,D
    return helper
    
def _number_of_bits(n):
    """
    Description:
        
        Returns the number of bits in the binary representation of n
    
    Input:
    
        n - integer
    
    Output:
    
        num_bits - number of bits
    
    """    
    if n == 0:
        return 1
    else:
        return floor(log(n).n()/log(2).n()) + 1

def is_suitable_curve(q,t,r,k,D, num_bits):
    """
    Description:
    
        User-defined method that filters the set of curves that are returned. By default checks if (q,t,r,k,D) is a valid curve
    
    Input:
    
        q - size of prime field
        t - trace of Frobenius
        r - size of prime order subgroup
        k - embedding degree
        D - (negative) fundamental discriminant
        num_bits - desired number of bits in r
    
    Output:
    
        bool - true iff (q,t,r,k,D) is suitable
    
    """
    return _number_of_bits(r) >= num_bits and is_valid_curve(q,t,r,k,D)

def is_suitable_q(q):
    """
    Description:
    
        User-defined method that filters the set of primes q that are returned. By default checks if q is prime
    
    Input:
    
        q - integer
    
    Output:
    
        bool - true iff q is suitable
    
    """
    return is_prime(q)

def is_suitable_r(r):
    """
    Description:
    
        User-defined method that filters the set of primes r that are returned. By default checks if r is prime
    
    Input:
    
        r - integer
    
    Output:
    
        bool - true iff r is suitable
    
    """
    return is_prime(r)
    
    
def print_curve(q,t,r,k,D):
    """
    Description:
    
        Prints the curve (q,t,r,k,D)
    
    Input:
    
        q - size of prime field
        t - trace of Frobenius
        r - size of prime order subgroup
        k - embedding degree
        D - (negative) fundamental discriminant
    
    Output:
    
        None
    
    """
    print(curve_to_string(q,t,k,r,D))
    
def curve_to_string(q,t,k,r,D):
    """
    Description:
    
        Returns a string representation of the curve (q,t,r,k,D)
    
    Input:
    
        q - size of prime field
        t - trace of Frobenius
        r - size of prime order subgroup
        k - embedding degree
        D - (negative) fundamental discriminant
    
    Output:
    
        s - string representation of (q,t,r,k,D)
    
    """
    if q == 0 or t == 0 or r == 0 or k == 0 or D == 0:
        return 'Failed to find an elliptic curve'
    else:
        return 'Elliptic curve over a field of size ' + str(q) + ' with trace ' + str(t) + ', a subgroup of order ' + str(r) + ' with embedding degree ' + str(k) + ', and fundamental discriminant ' + str(D)
    
    
    