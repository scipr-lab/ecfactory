from sage.all import random, power_mod, primitive_root, Integer, random_prime, is_prime, kronecker, squarefree_part, is_square, Mod, fundamental_discriminant, sqrt, log, floor
from ecfactory.utils import is_valid_curve
import ecfactory.utils as utils
import sys


def make_curve(num_bits, num_curves=1):
    """
    Description:

        Finds num_curves Barreto-Lynn-Scott curves with a scalar field order that is at least 2^num_bits.

    Input:

        num_bits - number of bits for the prime subgroup order of the curve
        num_curves - number of curves to find

    Output:

        curves - list of the first num_curves BLS curves each of prime order at least 2^num_bits;
                 each curve is represented as a tuple (q,t,r,k,D)

    """
    def R(y):
        x = Integer(y)
        return pow(x, 4) - pow(x, 2) + 1

    def P(y):
        x = Integer(y)
        r = R(y)
        return Integer(floor((pow(x-1, 2) * r) / 3 + x))

    x = Integer(floor(pow(2, (num_bits)/4.0)))
    q = 0
    r = 0
    t = 0
    curve_num = 0
    curves = []
    while curve_num < num_curves or (log(r).n()/log(2).n() < 2*num_bits and not (utils.is_suitable_q(q) and utils.is_suitable_r(r) and utils.is_suitable_curve(q, t, r, 12, -3, num_bits))):
        r = R(x)
        q = P(x)
        t = Integer(x + 1)

        b = utils.is_suitable_q(q) and utils.is_suitable_r(
            r) and utils.is_suitable_curve(q, t, r, 12, -3, num_bits)
        if b:
            sys.stdout.write(".")
            try:
                assert floor(log(r)/log(2)) + \
                    1 >= num_bits, 'Subgroup not large enough'
                curves.append((q, t, r, 12, -3))
                curve_num += 1
            except AssertionError as e:
                pass
        if curve_num < num_curves or not b:
            q = P(-x)
            t = Integer(-x + 1)
            if (utils.is_suitable_q(q) and utils.is_suitable_r(r) and utils.is_suitable_curve(q, t, r, 12, -3, num_bits)):
                try:
                    assert floor(log(r)/log(2)) + \
                        1 >= num_bits, 'Subgroup not large enough'
                    curves.append((q, t, r, 12, -3))
                    curve_num += 1
                except AssertionError as e:
                    pass
        x += 1
    return curves
