Barreto-Naehrig Curves
======================

Overview
--------

This module provides functionality to construct _Barreto-Naehrig (BN) curves_, following the procedure described in [\[BN05\]](/references/Barreto%20Naehrig%202005%20---%20Pairing-Friendly%20Elliptic%20Curves%20of%20Prime%20Order.pdf). The module contains three files:

* `bn_curves.py`, which contains the algorithm to construct Barreto-Naehrig curves;

* `bn_curves_examples.py`, which contains code examples;

* `bn_curves_tests.py`, which contains unit tests.

Throughout,
_q_ denotes the prime size of the base field;
_t_ denotes the trace of Frobenius;
_r_ denotes the prime size of the group;
_k_ denotes the embedding degree;
_D_ denotes the (negative) fundamental discriminant.

Methods
-------

The main method in `bn_curves.py` is

```python
make_curve(num_bits, num_curves=1)
```

It outputs a list of the first *num\_curves* BN curves of prime order at least 2<sup>*num\_bits*</sup>.

Examples
--------

The code example in `bn_curves_examples.py` shows how to find 10 BN curves with a prime order that is at least 2<sup>100</sup>.

Tests
-----

The test in `bn_curves_tests.py` runs the algorithm on random bit-sizes and checks validity of the output.
