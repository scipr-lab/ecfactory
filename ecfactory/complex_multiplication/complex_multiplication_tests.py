from sage.all import randint
import time
import ecfactory.cocks_pinch as cp
import ecfactory.complex_multiplication as cm
from ecfactory.utils import is_valid_curve

def test_cm(num_tests,num_bits, debug=False): 
    # runs CM method num_tests times;
    # each test uses a random output from the CP method with a num_bits bit prime
    print('testing CM...')
    fail = 0
    for i in range(0, num_tests):
        try:
            k = randint(5,50)
            r,k,D = cp.gen_params_from_bits(num_bits,k)
            q,t,r,k,D = cp.run(r,k,D)
            E = cm.make_curve(q,t,r,k,D)
            assert E
            assert cm.test_curve(q,t,r,k,D,E)
        except AssertionError as e:
            fail += 1
    if fail == 0:
        print('test passed')
        return True
    else:
        print("failed %.2f" %(100*fail/num_tests) + "% of tests!")
        return False

test_cm(20,50)

print('testing CM edge cases j=0 and j=1728')

# test CM method when j = 1728
E = cm.make_curve(17232027701054521159192750959745535948822138513276994230516636357, 129372487574083575172689106885388, 522378919834231359250965924449, 8, -4)
assert cm.test_curve(17232027701054521159192750959745535948822138513276994230516636357, 129372487574083575172689106885388, 522378919834231359250965924449, 8, -4, E), 'failed to find curve when j=1728'

# test CM method when j = 0
E = cm.make_curve(390834320061394909739901536101003424862215016583546821757802719, 17745279994431356955516821466193, 169356448305103304697688858051, 10, -3)
assert cm.test_curve(390834320061394909739901536101003424862215016583546821757802719, 17745279994431356955516821466193, 169356448305103304697688858051, 10, -3, E), 'failed to find curve when j=0'
print('test passed')