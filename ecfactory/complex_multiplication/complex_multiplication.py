from sage.all import power_mod, primitive_root, is_square, hilbert_class_polynomial, is_prime,GF, EllipticCurve, kronecker, randint, Integer, Mod
from ecfactory.utils import is_valid_curve
import ecfactory.utils as utils

def make_curve(q,t,r,k,D,debug=False):
    """
    Description:
    
        Finds the curve equation for the elliptic curve (q,t,r,k,D) using the Complex Multiplication method
    
    Input:
    
        q - size of prime field
        t - trace of Frobenius
        r - size of prime order subgroup
        k - embedding degree
        D - (negative) fundamental discriminant
    
    Output:
    
        E - elliptic curve over F_q with trace t,
            a subgroup of order r with embedding degree k,
            and fundamental discriminant D
    
    """
    assert is_valid_curve(q,t,r,k,D), 'Invalid input. No curve exists.' # check inputs
    if debug:
        print('Tested input')
    poly = hilbert_class_polynomial(D) # compute hilbert class polynomial
    if debug:
        print('Computed Hilbert class polynomial')
    check = False
    j_inv = poly.any_root(GF(q)) # find j-invariant    
    orig_curve = EllipticCurve(GF(q), j=j_inv) # make a curve
    E = orig_curve
    check = test_curve(q,t,r,k,D,E) # see if this is the right curve
    twist = False
    if not check: # not the right curve, use quadratic twist
        E = E.quadratic_twist()
        check = test_curve(q,t,r,k,D,E)
        if check:
            twist = True
        else: # twist didnt work => j = 0 or 1728
            if j_inv == 0: # for j = 0, use sextic twists
                prim = primitive_root(q)
                i = 1
                while t != E.trace_of_frobenius() and i < 6:
                    E = orig_curve.sextic_twist(power_mod(prim,i,q))
                    i+=1
            elif j_inv == 1728: # for j = 1728, use quartic twists
                prim = primitive_root(q)
                i = 1
                while t != E.trace_of_frobenius() and i < 4:
                    E = orig_curve.quartic_twist(power_mod(prim,i,q))
                    i+=1
            else: # twist didnt work and j != 0, 1728. this should never happen, so write input to a file for debugging
                print('Error. Quadratic twist failed to find the correct curve with j != 0, 1728. Logging output to debug.txt') # this line should never be reached'
                f = open('debug.txt', 'w')
                f.write('Twist: ' + str(twist) + '\n')
                f.write('q: ' + str(q) + '\n')
                f.write('t: ' + str(t) + '\n')
                f.write('r: ' + str(r) + '\n')
                f.write('k: ' + str(k) + '\n')
                f.write('D: ' + str(D) + '\n')
                f.write('E: ' + str(E) + '\n')
                f.write('orig_curve: ' + str(orig_curve))
                f.close()
                return False
            check = test_curve(q,t,r,k,D,E)
            twist = True
    if not check: # didnt find a curve. this should never happen, so write input to a file for debugging
        print('Error. Failed to find curve. Logging output to debug.txt')
        f = open('debug.txt', 'w')
        f.write('Twist: ' + str(twist) + '\n')
        f.write('q: ' + str(q) + '\n')
        f.write('t: ' + str(t) + '\n')
        f.write('r: ' + str(r) + '\n')
        f.write('k: ' + str(k) + '\n')
        f.write('D: ' + str(D) + '\n')
        f.write('E: ' + str(E) + '\n')
        f.write('orig_curve: ' + str(orig_curve))
        f.close()
        return False
    return E

def small_A_twist(E):
    """
    Description:
        
        Finds a curve isogenous to E that has small A in the curve equation y^2 = x^3 + A*x + B
    
    Input:
    
        E - elliptic curve
    
    Output:
    
        E' - elliptic curve isogenous to E that has small A in the curve equation y^2 = x^3 + A*x + B
    
    """
    a = E.ainvs()[3]
    q = E.base_field().order()
    a = power_mod(Integer(a), -1, q)
    if kronecker(a,q) == -1:
        b = 2
        while 1:
            b += 1
            if kronecker(b, q) == 1:
                continue
            tmp = a * b % q
            d = Mod(tmp, q).sqrt()
            if kronecker(d, q) != 1:
                continue
            break
    ainvs = [i for i in E.ainvs()]
    ainvs[3]*= d**2
    ainvs[4] *= d**3
    return EllipticCurve(E.base_field(), ainvs)
    
def small_B_twist(E):
    """
    Description:
        
        Finds a curve isogenous to E that has small B in the curve equation y^2 = x^3 + A*x + B
    
    Input:
    
        E - elliptic curve
    
    Output:
    
        E' - elliptic curve isogenous to E that has small B in the curve equation y^2 = x^3 + A*x + B
    
    """
    b = E.ainvs()[4]
    q = E.base_field().order()
    b = power_mod(Integer(b), -1, q)
    d = 0
    s = Mod(1,q)
    bool = True
    while bool:
        try:
            d = (s*b)
            d = d.nth_root(3)
            d = Integer(d)
            bool = False
        except ValueError as e:
            s+=1 
            pass
    ainvs = [i for i in E.ainvs()]
    ainvs[3] *= d**2
    ainvs[4] *= d**3
    return EllipticCurve(E.base_field(), ainvs)

def test_curve(q,t,r,k,D,E): 
    """
    Description:
    
       Tests that E is an elliptic curve over F_q with trace t, a subgroup of order r with embedding degree k, and fundamental discriminant D
    
    Input:
    
        q - size of prime field
        t - trace of Frobenius
        r - size of prime order subgroup
        k - embedding degree
        D - (negative) fundamental discriminant
    
    Output:
    
        bool - true iff E is an elliptic curve over F_q with trace t, a subgroup of order r with embedding degree k, and fundamental discriminant D
    
    """    
    bool = True
    bool = bool and (power_mod(q, k, r) == 1) #q^k -1 ==0 mod r
    bool = bool and (E.trace_of_frobenius() == t)
    bool = bool and (kronecker((t*t-4*q) * Integer(D).inverse_mod(q),q) == 1)
    bool = bool and (E.cardinality() == q+1-t)
    bool = bool and (E.cardinality() % r ==0)
    return bool
