Barreto-Lynn-Scott Curves
======================

Overview
--------

This module provides functionality to construct _Barreto-Lynn-Scott (BLS) curves_, following the procedure described in [\[BLS02\]](/references/Barreto%20Lynn%20Scott%202002%20---%20Constructing%20Elliptic%20Curves%20with%20Prescribed%20Embedding%20Degrees.pdf). The module contains three files:

* `bls_curves.py`, which contains the algorithm to construct Barreto-Lynn-Scott curves;

* `bls_curves_examples.py`, which contains code examples;

* `bls_curves_tests.py`, which contains unit tests.

Throughout,
_q_ denotes the prime size of the base field;
_t_ denotes the trace of Frobenius;
_r_ denotes the prime size of the group;
_k_ denotes the embedding degree;
_D_ denotes the (negative) fundamental discriminant.

Methods
-------

The main method in `bls_curves.py` is

```python
make_curve(num_bits, num_curves=1)
```

It outputs a list of the first *num\_curves* BLS curves of prime order at least 2<sup>*num\_bits*</sup>.

Examples
--------

The code example in `bls_curves_examples.py` shows how to find 10 BLS curves with a prime order that is at least 2<sup>100</sup>.

Tests
-----

The test in `bls_curves_tests.py` runs the algorithm on random bit-sizes and checks validity of the output.
