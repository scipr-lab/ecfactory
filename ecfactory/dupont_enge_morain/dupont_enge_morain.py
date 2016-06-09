from sage.all_cmdline import x
from sage.all import random, power_mod, primitive_root, Integer, random_prime, is_prime, kronecker, squarefree_part, is_square, Mod, PolynomialRing, ZZ, fundamental_discriminant, randint, GF,sqrt, round, floor, ceil, euler_phi, log
import time
from ecfactory.utils import is_valid_curve
import ecfactory.utils as utils

def method(num_bits,k,D,y,max_trials=10000): 
    """
    Description:
    
        Runs the Dupont-Enge-Morain method
    
    Input:
    
        num_bits - number of bits for the prime order r
        k - embedding degree
        D - (negative) fundamental discriminant
        y - coefficient of D in the CM equation
        num_times - number of iterations of the while loop when searching for q
        
    Output:
    
        (q,t,r,k,D) - elliptic curve;
                      returns (0,0,0,k,D) if no r was found, and (0,0,r,k,D) if no q was found
    
    """
    assert fundamental_discriminant(D) == D, 'Invalid discriminant'
    assert k >= 1, 'Invalid embedding degree'
    t,r = _method_pt1(num_bits,k,D,y)
    if r == 0:
        return 0,0,0,k,D
    return _method_pt2(t,r,k,D,y,max_trials)

def _method_pt1(num_bits,k,D,y):
    a = Integer(-D*y**2)
    R = PolynomialRing(ZZ,'x')
    f = R.cyclotomic_polynomial(k)(x-1).polynomial(base_ring = R)
    g = (a+(x-2)**2).polynomial(base_ring = R)
    r = Integer(f.resultant(g))
    if (Mod(r, k) == 1) and r > 2**(num_bits-1) and utils.is_suitable_r(r): # found a valid r, so use it
        F = GF(r)
        f = f.change_ring(F)
        g = g.change_ring(F)
        t = Integer(f.gcd(g).any_root())
        return t,r
    else:
        return 0,0

def _method_pt2(t,r,k,D,y, max_trials=10000):
    a = Integer(-D*y**2)
    j = 0
    r2 = r**2
    t2 = t**2
    m = 2*t*r
    q = t2+a
    while j < max_trials: # iterate until a prime q is found
        # at the beginning of each loop, q = (t+jr)^2 + a
        if q % 4 == 0:
            q2 = q//4
            if utils.is_suitable_q(q2): # found a prime, so output it
                return q2,t+j*r,r,k,D
        q += m + ((2*j + 1)*r2)
        j+=1
    return 0,0,r,k,D # found nothing

@utils.filter_decorator
def run(num_bits,k):
    """
    Description:
    
        Runs the Dupont-Enge-Morain method multiple times until a valid curve is found
    
    Input:
    
        num_bits - number of bits
        k - an embedding degree
    
    Output:
    
        (q,t,r,k,D) - an elliptic curve;
                      if no curve is found, the algorithm returns (0,0,0,k,0)
    
    """
    j,r,q,t = 0,0,0,0
    num_generates = 512
    h = num_bits/(euler_phi(k))
    tried = [(0,0)] # keep track of random values tried for efficiency
    for i in range(0,num_generates):
        D = 0
        y = 0
        while (D,y) in tried: # find a pair that we have not tried
            D = -randint(1, 1024) # pick a small D so that the CM method is fast
            D = fundamental_discriminant(D)
            m = 0.5*(h - log(-D).n()/(2*log(2)).n())
            if m < 1:
                m = 1
            y = randint(floor(2**(m-1)), floor(2**m))
        tried.append((D,y))
        q,t,r,k,D = method(num_bits,k,D,y) # run DEM
        if q != 0 and t != 0 and r != 0 and k != 0 and D != 0: # found an answer, so output it
            assert is_valid_curve(q,t,r,k,D), 'Invalid output'
            return q,t,r,k,D
    return 0,0,0,k,0 # found nothing