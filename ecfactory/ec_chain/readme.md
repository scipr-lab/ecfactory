Elliptic Curve Chains
=====================

Overview
--------

This module provides functionality to construct elliptic curve chains using the Cocks-Pinch method. An elliptic curve chain is a sequence of _n_ elliptic curves *E*<sub>1</sub>, *E*<sub>2</sub>, ... , *E*<sub>n</sub> satisfying #*E*<sub>i</sub>(**F**<sub>i<sub></sub></sub>) = *p*<sub>i-1</sub>, for i = 1, 2, ..., n. The module contains three files:

* `ec_chain.py`, which contains the algorithm to construct elliptic curve chains

* `ec_chain_examples.py`, which contains code examples;

* `ec_chain_tests.py`, which contains unit tests.

Throughout,
_q_ denotes the prime size of the base field;
_t_ denotes the trace of Frobenius;
_r_ denotes the prime size of the group;
_k_ denotes the embedding degree;
_D_ denotes the (negative) fundamental discriminant.

Methods
-------
Here is an overview of the methods in `ec_chain.py`:

```python
make_chain(curve, k_vector)
```

Outputs an elliptic curve chain where the first curve is _curve_, and the ith constructed curve has embedding degree k\_vector[i]; each curve is represented as a tuple (_q_,_t_,_r_,_k_,_D_).

```python
make_chain_from_bn(num_bits, k_vector, n=1)
```
	
Outputs an elliptic curve chain where the first curve is the nth BN curve with subgroup of order at least 2<sup>num\_bits</sup>, and the ith constructed curve has embedding degree k\_vector[i]; each curve is represented as a tuple (_q_,_t_,_r_,_k_,_D_).

```python
new_chain(p0, k_vector)
```

Outputs an elliptic curve chain where _p_<sub>0</sub> = p0, and the ith constructed curve has embedding degree k\_vector[i]; each curve is represented as a tuple (_q_,_t_,_r_,_k_,_D_).

```python
is_chain(curves)
```

Checks that *curves* is a valid elliptic curve chain.

Examples
--------

The code examples in `ec_chain_examples.py` shows how to find elliptic curve chains using each of the 3 methods.

Tests
-----

The test in `ec_chain_tests.py` runs the algorithm on random inputs and checks validity of the output.