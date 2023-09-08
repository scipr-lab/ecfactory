import ecfactory.bls_curves as bls
from ecfactory.utils import print_curve

# Example
num_bits = 100  # number of bits in r
num_curves = 10  # number of curves to find
curves = bls.make_curve(num_bits, num_curves)
for q, t, r, k, D in curves:
    print_curve(q, t, r, k, D)
