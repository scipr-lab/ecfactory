import ecfactory.ec_chain as ec
from ecfactory.utils import curve_to_string

# Example 1: (using a known starting curve)
curve = (30451590496705691, 43783308, 709451, 5, -71)
k_vector = [5, 11]
curves = ec.make_chain(curve, k_vector)
print('Chain 1:')
for c in curves:
    print('\t' + curve_to_string(c[0], c[1], c[2], c[3], c[4]))
    
# Example 2: (using a BN curve)
k_vector = [5, 11]
curves = ec.make_chain_from_bn(20, k_vector)
print('Chain 2:')
for c in curves:
    print('\t' + curve_to_string(c[0], c[1], c[2], c[3], c[4]))
    
# Example 3: (making a chain with no initial curve)
r = 11
k_vector = [5,7,11]
curves = ec.new_chain(r, k_vector)
print('Chain 3:')
for c in curves:
    print('\t' + curve_to_string(c[0], c[1], c[2], c[3], c[4]))