Dupont-Enge-Morain Method
=========================

Overview
--------

This module provides functionality to construct pairing-friendly elliptic curves via the _Dupont-Enge-Morain (DEM) method_; curves constructed via this method have &rho;-value approximately 2. The implementation follows the procedure described in [\[FST10\]](/references/Freeman%20Scott%20Teske%202010%20---%20A%20Taxonomy%20of%20Pairing-Friendly%20Elliptic%20Curves.pdf). This module contains three files:

* `dupont_enge_morain.py`, which contains the algorithm that implements the DEM method. 

* `dupont_enge_morain_examples.py`, which contains code examples;

* `dupont_enge_morain_tests.py`, which contains unit tests.

Throughout,
_q_ denotes the prime size of the base field;
_t_ denotes the trace of Frobenius;
_r_ denotes the prime size of the group;
_k_ denotes the embedding degree;
_D_ denotes the (negative) fundamental discriminant.


Methods
-------

Here is an overview of the methods in `dupont_enge_morain.py`:

```python
method(num_bits, k, D, y, max_trials=10000)
```

Runs the DEM method, and returns a curve (_q_,_t_,_r_,_k_,_D_), where _r_ has at least _num\_bits_ bits. If no curve was found, the method returns (0,0,0,_k_,_D_) if no _r_ was found, and (0,0,_r_,_k_,_D_) if no _q_ was found. In the input, _y_ is the coefficient of _D_ in the CM equation, i.e. *D*_y_<sup>2</sup> = _t_<sup>2</sup> − 4*q*. The optional parameter *max_trials* sets the maximum number of iterations of the while loop that searches for _q_.

```python
run(num_bits, k)
```

Runs `method` multiple times until a valid curve (_q_,_t_,_r_,_k_,_D_) is found. If no curve is found, then the function outputs (0,0,0,_k_,0).

Examples
--------

The code example in `dupont_enge_morain_examples.py` shows how to run the DEM method using a predetermined embedding degree and number of bits for _r_.


Tests
-----

The test in `dupont_enge_morain.py` runs the DEM method many times using random input parameters and checks validity of the output.
