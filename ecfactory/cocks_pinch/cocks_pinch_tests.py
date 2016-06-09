from sage.all import randint
import time
import ecfactory.cocks_pinch as cp
import ecfactory.utils as utils

def test_cp(num_tests,num_bits, debug=False):
    # runs CP method num_tests times;
    # each test uses a random embedding degree and an n bit prime
    test_cp2(num_tests,num_bits,False,debug)

def test_cp2(num_tests,num_bits,k, debug=False):
    # runs CP method num_tests times;
    # uses the same embedding degree k for every test
    print('testing CP...')
    fail = 0
    k2 = k
    for i in range(0, num_tests):
        if not k2:
            k = randint(5,50)
        try:
            r,k,D = cp.gen_params_from_bits(num_bits, k)
            assert cp.test_promise(r,k,D)
            q,t,r,k,D = cp.run(r,k,D)
            assert utils.is_suitable_curve(q,t,r,k,D,num_bits)
        except AssertionError as e:
            fail += 1
    if fail == 0:
        print('test passed')
        return True
    else:
        print("failed %.2f" %(100*fail/num_tests) + "% of tests!")
        return False
        
        
        
        

test_cp(100,50, False)
test_cp(3,400,False)