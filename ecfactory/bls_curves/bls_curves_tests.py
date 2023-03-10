from sage.all import randint
import ecfactory.bls_curves as bls
import ecfactory.utils as utils


def test_bls(num_tests):
    # finds num_tests BLS curves with random bit sizes;
    # checks that each curve found is a suitable curve
    print('testing BLS...')
    fail = 0
    for i in range(0, num_tests):
        num_bits = randint(50, 100)
        num_curves = randint(1, 20)
        try:
            curves = bls.make_curve(num_bits, num_curves)
            assert len(curves) == num_curves
            for q, t, r, k, D in curves:
                assert utils.is_suitable_curve(q, t, r, k, D, num_bits)
        except AssertionError as e:
            fail += 1
    if fail == 0:
        print('test passed')
        return True
    else:
        print("failed %.2f" % (100*fail/num_tests) + "% of tests!")
        return False


test_bls(10)
