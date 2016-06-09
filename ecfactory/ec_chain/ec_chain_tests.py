from sage.all import randint, random_prime, is_prime
import ecfactory.ec_chain as ec
import time

def test_ec(num_tests,num_bits, debug=False):
    print('testing EC chain...')
    func_start = time.time()
    fail = 0
    for i in range(0, num_tests):
        try:
            k = randint(5,20)
            r = 0
            while not (r % k == 1 and is_prime(r)):
                r = random_prime(2**(num_bits-1), 2**num_bits)
            k_vector = [k]
            k_vector.append(randint(5,20))
            k_vector.append(randint(5,20))
            curves = ec.new_chain(r, k_vector)
            assert ec.is_chain(curves)
        except AssertionError as e:
            fail += 1
    if fail == 0:
        print('test passed')
        return True
    else:
        print("failed %.2f" %(100*fail/num_tests) + "% of tests!")
        return False



test_ec(20,30)


