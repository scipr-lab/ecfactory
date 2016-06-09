Utils
=====

Overview
--------

This module provides functionality to filter the set of elliptic curves found by all algorithms in the library. The methods are designed to be overriden by the user.

Throughout,
_q_ denotes the prime size of the base field;
_t_ denotes the trace of Frobenius;
_r_ denotes the prime size of the group;
_k_ denotes the embedding degree;
_D_ denotes the (negative) fundamental discriminant.

Methods
-------

Here is an overview of the methods in `utils.py`:

```python
is_valid_curve(q, t, r, k, D)
```

Checks that (_q_,_t_,_r_,_k_,_D_) is a valid elliptic curve.

```python
is_suitable_curve(q, t, r, k, D, num_bits)
```

All algorithms that output an elliptic curve call this method to check if the curve found is suitable. If not, then the algorithm will retry to find a new curve. By default, the method returns *true* if (_q_,_t_,_r_,_k_,_D_) is a valid elliptic curve and _r_ has at least *num_bits* bits

```python
is_suitable_q(q)
```

All algorithms that search for _q_ separately from the rest of the parameters call this method to determine if _q_ is suitable. By default, the method returns *true* if _q_ is prime.

```python
is_suitable_r(r)
```
	
All algorithms that search for _r_ separately from the rest of the parameters call this method to determine if _r_ is suitable. By default, the method returns *true* if _r_ is prime.

```python
print_curve(q, t, k, r, D):
```

Prints the curve (_q_,_t_,_r_,_k_,_D_).

```python
curve_to_string(q, t, k, r, D):
```

Returns a string representation of the curve (_q_,_t_,_r_,_k_,_D_).



Examples
--------

All of the methods above are designed to be overriden by the user. The following code shows how to do this for `is_suitable_q`. All other methods can be overriden in the same way. **WARNING** Overriding methods improperly may cause algorithms to loop indefinitely. Take care to check that there are curves that will satisfy the constraints implied by the 3 methods.

Overriding `is_suitable_q`

```python
import ecfactory.utils as utils
utils.is_suitable_q = lambda q: is_prime(q) and q % 6 == 1
```

Now all algorithms that search for _q_ will only find primes congruent to 1 mod 6. Check that this is true with DEM

```python
import ecfactory.dupont_enge_morain as dem
q, t, r, k, D = dem.run(50, 5)
assert q % 6 == 1
```


