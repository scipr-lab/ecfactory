Complex Mulitiplication
=======================

Overview
--------

This module provides functionality to construct elliptic curves via the _Complex Multiplication (CM) method_. The implementation follows the procedure described in [\[W08\]](/references/Washington%202008%20---%20Elliptic%20Curves%20Number%20Theory%20and%20Cryptography.pdf). This module contains three files:

* `complex_multiplication.py`, which contains the algorithm for the CM method;

* `complex_multiplication_examples.py`, which contains code examples;

* `complex_multiplication_tests.py`, which contains unit tests.

Throughout,
_q_ denotes the prime size of the base field;
_t_ denotes the trace of Frobenius;
_r_ denotes the prime size of the group;
_k_ denotes the embedding degree;
_D_ denotes the (negative) fundamental discriminant.

Methods
-------

Here is an overview of the methods in `complex_multiplication.py`:

```python
make_curve(q, t, r, k, D, debug=False)
```

Runs the CM method and returns an elliptic curve _E_(**F**<sub>_q_</sub>) that has trace _t_, a subgroup of order _r_ with embedding degree _k_, and fundamental discriminant _D_. Setting `debug=True` will output a print statement when the Hilbert class polynomial is computed, since this computation is the bottleneck of the algorithm.

```python
small_A_twist(E)
```

Returns a curve E' that is isogenous to E and has small coefficient _A_ in the curve equation _y_<sup>2</sup> = _x_<sup>3</sup> + _Ax_ + _B_.

```python
small_B_twist(E)
```

Returns a curve E' that is isogenous to E and has small coefficient _B_ in the curve equation _y_<sup>2</sup> = _x_<sup>3</sup> + _Ax_ + _B_.

```python	
test_curve(q, t, r, k, D, E)
```

Tests that *E*(**F**<sub>_q_</sub>) has trace _t_, a subgroup of order _r_ with embedding degree _k_, and fundamental discriminant _D_.

Examples
--------

The code examples in `complex_multiplication_examples.py` show how to run the CM method to construct an elliptic curve.


Tests
-----

The test in `complex_multiplication_.py` runs the CM method many times on random test cases. The test also checks the two edge cases when the _j_-invariant equals 0 and 1728.