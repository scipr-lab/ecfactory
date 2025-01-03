from sage.misc.prandom import random
from sage.arith.misc import power_mod
from sage.arith.misc import primitive_root
from sage.rings.integer import Integer
from sage.arith.misc import random_prime
from sage.arith.misc import is_prime
from sage.arith.misc import kronecker
from sage.misc.functional import squarefree_part
from sage.arith.misc import is_square
from sage.rings.finite_rings.integer_mod import Mod
from sage.arith.misc import fundamental_discriminant
from sage.misc.functional import sqrt
from sage.misc.functional import log
from sage.functions.other import floor
from ecfactory.utils import is_valid_curve
import ecfactory.utils as utils

def make_curve(num_bits, num_curves=1): 
    """
    Description:
    
        Finds num_curves Barreto-Naehrig curves with a prime order that is at least 2^num_bits.
    
    Input:
    
        num_bits - number of bits for the prime order of the curve
        num_curves - number of curves to find
    
    Output:
    
        curves - list of the first num_curves BN curves each of prime order at least 2^num_bits;
                 each curve is represented as a tuple (q,t,r,k,D)
    
    """
    def P(y):
        x = Integer(y)
        return 36*pow(x,4) + 36*pow(x,3) + 24*pow(x,2) + 6*x + 1
    x = Integer(floor(pow(2, (num_bits)/4.0)/(sqrt(6))))
    q = 0
    r = 0
    t = 0
    curve_num = 0
    curves = []
    while curve_num < num_curves or (log(q).n()/log(2).n() < 2*num_bits and not (utils.is_suitable_q(q) and utils.is_suitable_r(r) and utils.is_suitable_curve(q,t,r,12,-3,num_bits))):
        t = Integer(6*pow(x,2) + 1)
        q = P(-x)
        r = q + 1 - t
        b = utils.is_suitable_q(q) and utils.is_suitable_r(r) and utils.is_suitable_curve(q,t,r,12,-3,num_bits)
        if b:
            try:
                assert floor(log(r)/log(2)) + 1 >= num_bits, 'Subgroup not large enough'  
                curves.append((q,t,r,12,-3))
                curve_num += 1
            except AssertionError as e:
                pass
        if curve_num < num_curves or not b:
            q = P(x)
            r = q+1-t
            if (utils.is_suitable_q(q) and utils.is_suitable_r(r) and utils.is_suitable_curve(q,t,r,12,-3,num_bits)):
                try:
                    assert floor(log(r)/log(2)) + 1 >= num_bits, 'Subgroup not large enough'  
                    curves.append((q,t,r,12,-3))
                    curve_num += 1
                except AssertionError as e:
                    pass  
        x += 1
    return curves