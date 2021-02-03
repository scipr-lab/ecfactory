Cocks-Pinch Method
==================

Overview
--------

This module provides functionality to construct pairing-friendly elliptic curves via the _Cocks-Pinch (CP) method_; curves constructed via this method have &rho;-value approximately 2. The implementation follows the procedure described in [\[FST10\]](/references/Freeman%20Scott%20Teske%202010%20---%20A%20Taxonomy%20of%20Pairing-Friendly%20Elliptic%20Curves.pdf). This module contains three files:

* `cocks_pinch.py`, which contains the algorithm for the CP method. 

* `cocks_pinch_examples.py`, which contains code examples;

* `cocks_pinch_tests.py`, which contains unit tests.

Throughout,
_q_ denotes the prime size of the base field;
_t_ denotes the trace of Frobenius;
_r_ denotes the prime size of the group;
_k_ denotes the embedding degree;
_D_ denotes the (negative) fundamental discriminant.

Methods
-------

Here is an overview of the methods in `cocks_pinch.py`:

```python
find_element_of_order(k, r)
```

Generates a random element of order _k_ in **Z**<sub>_r_</sub><sup>\*</sup>.

```python
method(r, k, D, max_trials=10000, g=0)
```

Runs the CP method to find a valid pair (_q_,_t_). If a pair is found, the function outputs it, otherwise it outputs (0,0). Above, *max\_trials* is the number of times the algorithm runs the main loop of the CP method, and _g_ is an element of order _k_ in **Z**<sub>_r_</sub><sup>\*</sup>. By default (if _g_ = 0), the method generates _g_ at random, using `find_element_of_order`.

```python
run(r, k, D, max_run_time=20)
```
	
Runs `method` multiple times until a valid pair (_q_,_t_) is found, and then outputs the curve (_q_,_t_,_r_,_k_,_D_). To prevent infinite looping, after running for *max\_run\_time* seconds the function finishes its last call to `method`, and then terminates.

```python
gen_params_from_bits(num_bits, k)
```

Generates a _num\_bits_ bit prime _r_ and a fundamental discriminant _D_ to use in the CP method.

```python
gen_params_from_r(r, k)
```

Finds a random fundamental discriminant _D_ such that _D_ is a square mod _r_.

```python
test_promise(r, k, D)
```

Tests that _r_, _k_, _D_ are valid inputs to the CP method.

Examples
--------

The code examples in `cocks_pinch_examples.py` show how to run the CP method using a predetermined value for _r_, and how to run the CP method by specifying the number of bits for _r_. The example code also shows how to run the CP method only once, using a given element _g_ of order _k_.

Tests
-----
The test in `cocks_pinch_tests.py` runs the CP method many times using random input parameters and checks validity of the output.
