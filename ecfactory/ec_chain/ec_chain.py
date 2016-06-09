import ecfactory.bn_curves as bn
import ecfactory.cocks_pinch as cp
from ecfactory.utils import is_valid_curve

def make_chain(curve, k_vector):
    """
    Description:
    
        Finds an elliptic curve chain
    
    Input:
    
        curve - the first curve (q,t,r,k,D) in the chain
        k_vector - list of embedding degrees
    
    Output:
    
        curves - elliptic curve chain
    
    """
    curves = [curve]
    r = curve[0]
    for i in range(0, len(k_vector)):
        k = k_vector[i]
        r,k,D = cp.gen_params_from_r(r,k)
        curve2 = cp.run(r,k,D)
        j = 0
        while i < len(k_vector) - 1 and (curve2[0] - 1) % k_vector[i+1] != 0 and j < 100:
             curve2 = cp.run(r,k,D)
             j+=1
        curves.append(curve2)
        r = curve2[0]
    return curves
    
def make_chain_from_bn(num_bits, k_vector, n=1):
    """
    Description:
    
        Finds an elliptic curve chain where the first curve is a BN curve
    
    Input:
    
        num_bits - number of bits for BN curve
        k_vector - list of embedding degrees
        n - positive integer
    
    Output:
    
        curves - elliptic curve chain where the first curve is the nth BN curve
    
    """
    curve = bn.make_curve(num_bits,n)[n-1]
    return make_chain(curve, k_vector)
    
def new_chain(p0, k_vector):
    """
    Description:
    
        Finds an elliptic curve chain where the first curve has order r
    
    Input:
    
        r - prime
        k_vector - list of embedding degrees
    
    Output:
    
        curves - elliptic curve chain
    
    """
    curves = make_chain((p0,0,0,0,0), k_vector)
    return curves[1:]
    
def is_chain(curves):
    """
    Description:
    
        Tests if curves is an elliptic curve chain
    
    Input:
    
        curves - a list of elliptic curves (q,t,r,k,D)
    
    Output:
    
        bool - true iff curves is an elliptic curve chain
    
    """
    try:
        for c in curves:
            assert is_valid_curve(c[0],c[1],c[2],c[3],c[4])
        for i in range(1, len(curves)):
            assert curves[i][2] == curves[i-1][0]
    except AssertionError as e:
        return False
    return True