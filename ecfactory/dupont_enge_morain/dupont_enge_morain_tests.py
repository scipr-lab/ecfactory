from sage.all import randint
import ecfactory.dupont_enge_morain as dem
import time
import ecfactory.utils as utils

def test_dem(num_tests,num_bits, debug=False):
    # runs dupont enge morain method num_tests times;
    # each test uses a random embedding degree
    test_dem2(num_tests,num_bits,False,debug)

def test_dem2(num_tests,num_bits,k, debug=False):
    # runs dupont enge morain method num_tests times;
    # each test uses a fixed embedding degree k
    print('testing DEM...')
    fail = 0
    k2 = k
    for i in range(0, num_tests):
        if not k2:
            k = randint(5,20)
        try:
            q,t,r,k,D = dem.run(num_bits,k)
            assert utils.is_suitable_curve(q,t,r,k,D,num_bits)
        except AssertionError as e:
            fail += 1
    if fail == 0:
        print('test passed')
        return True
    else:
        print("failed %.2f" %(100*fail/num_tests) + "% of tests!")
        return False

test_dem(20,100)