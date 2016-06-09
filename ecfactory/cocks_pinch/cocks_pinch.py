from sage.all import random, power_mod, primitive_root, Integer, random_prime, is_prime, kronecker, squarefree_part, is_square, Mod, fundamental_discriminant, randint
import time
from ecfactory.utils import is_valid_curve
import ecfactory.utils as utils

def find_element_of_order(k,r):
    """
    Description:
    
        Finds a random element of order k in Z_r^*
    
    Input:
    
        k - integer such that r % k == 1
        r - prime
    
    Output:
    
        h - element of order k in Z_r^*
    
    """
    assert r % k == 1
    h = 0
    def order(h,k,p):
        bool = True
        g = h
        for i in range(1,k):
            bool = bool and g != 1
            g = Mod(g * h, p)
        bool = bool and g == 1
        return bool
    while not order(h,k,r): # expected number of iterations is k/euler_phi(k)
        h = power_mod(randint(2, r-1), (r-1)//k, r)
    return h


def method(r,k,D,max_trials=10000, g=0): 
    """
    Description:
        
        Run the Cocks-Pinch method to find an elliptic curve
    
    Input:
    
        r - prime
        k - embedding degree, r % k == 1
        D - (negative) fundamental discriminant where D is a square mod r
        max_trials - the number of integers q to test for primality in the CP method
        g - an element of order k in Z_r^*

    Output:
    
        (q,t) - tuple where q is a prime and t is chosen such that there exists
                an elliptic curve E over F_q with trace t, and r | q+1-t;
                if the algorithm fails to find (q,t), it will return (0,0)
    
    """
    assert test_promise(r,k,D), 'Invalid inputs'
    if g != 0:
        assert power_mod(g,k,r) == 1, 'Invalid inputs'
    else:
        g = find_element_of_order(k,r)
    D = Integer(D)
    t = Integer(g) + 1
    root_d = Integer(Mod(D, r).sqrt())
    u = Integer(Mod((t-2)*root_d.inverse_mod(r) ,r))
    q = 1
    j = Integer(0)
    i = Integer(0)
    count = 0
    while (count < max_trials):
           q = Integer( (t+i*r)**2 - D*(u + j*r)**2)
           if q % 4 ==0:
                q = q//4
                if utils.is_suitable_q(q):
                    return (q, t+i*r)
                q = 1
           if random() < 0.5:
                j+=1
           else:
                i+=1
           count+=1
    return (0, 0) # no prime found, so end

@utils.filter_decorator
def run(r,k,D,max_run_time=20):
    """
    Description:
    
        Runs the Cocks-Pinch method multiple times until a valid curve is found
    
    Input:
    
        r - prime
        k - embedding degree, r % k == 1
        D - (negative) fundamental discriminant where D is a square mod r
        max_run_time - maximum runtime of the function, in seconds

    Output:
        
        (q,t,r,k,D) - elliptic curve
    
    """
    assert test_promise(r,k,D), 'Invalid inputs'
    q = 0
    t = 0
    start = time.time()
    while q == 0 and time.time() - start < max_run_time: # run cocks pinch method until successful
        q,t = method(r,k,D)
    assert is_valid_curve(q,t,r,k,D), 'Invalid output'
    return q,t,r,k,D

def gen_params_from_bits(num_bits,k): 
    """
    Description:
    
        Generates a prime r with num_bits bits and a fundamental discriminant D to use as input to the Cocks-Pinch method
    
    Input:
        
        num_bits - number of bits in r
        k - embedding degree
        
    Output:
        
        r - prime such that r % k == 1 and r is num_bits bits long
        k - embedding degree
        D - (negative) fundamental discriminant where D is a square mod r
    
    """
    r = random_prime(2**num_bits, lbound=2**(num_bits-1))
    while not (r % k == 1 and utils.is_suitable_r(r)):
        r = random_prime(2**num_bits, lbound=2**(num_bits-1))
    return gen_params_from_r(r,k)

def gen_params_from_r(r,k):
    """
    Description:
    
        Finds a fundamental discriminant D to use as input to the Cocks-Pinch method
    
    Input:
    
        r - prime such that r % k == 1
        k - embedding degree  
    
    Output:
        
        r - prime such that r % k == 1
        k - embedding degree
        D - (negative) fundamental discriminant where D is a square mod r
    
    """
    D = -Integer(Mod(int(random()*(1000)),r))
    i = 0
    while not kronecker(D,r) == 1: # expected number of iterations of the while loop is 2
        D = -Integer(Mod(int(random()*(1000)),r))
        i+=1
    D = fundamental_discriminant(D)
    if not (kronecker(D,r) == 1):
        return r, k, 0
    return r,k,D


def test_promise(r,k,D):
    """
    Description:
    
        Tests that r,k,D is a valid input to the Cocks-Pinch method
    
    Input:
    
        r - prime
        k - embedding degree    
        D - (negative) funadmental discriminant
    
    Output:
    
        bool - true iff (r,k,D) is a valid input to the Cocks-Pinch method
    
    """
    bool = (kronecker(D,r) == 1) # D is a square mod r
    bool = bool and ( (r-1) % k ==0) # k | r-1
    bool = bool and (D == fundamental_discriminant(D)) # check that D is a fundamental discriminant
    return bool