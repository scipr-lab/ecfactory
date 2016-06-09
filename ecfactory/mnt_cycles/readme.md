MNT Cycles
==========

Overview
--------

This module provides functionality to construct (pairing-friendly) elliptic curve cycles (of length 2) using MNT curves, following the procedure described in [\[KT07\]](/references/Karabina Teske 2007 --- On prime-order elliptic curves with embedding degrees k = 3,4, and 6.pdf) and [\[BCTV14\]](https://eprint.iacr.org/2014/595). The module contains two files:

* `mnt_cycles.py`, which contains the algorithm to construct MNT cycles;

* `mnt_cycles_examples.py`, which contains code examples.

Throughout,
_q_ denotes the prime size of the base field;
_t_ denotes the trace of Frobenius;
_r_ denotes the prime size of the group;
_k_ denotes the embedding degree;
_D_ denotes the (negative) fundamental discriminant.

Methods
-------

The main method in `mnt_cycles.py` is

```python
cycle(D)
```

It finds all MNT cycles with fundamental discriminant _D_. The method outputs a list of cycles, where each cycle is a list of the curves on the cycle; each curve is represented as a tuple (_q_,_t_,_r_,_k_,_D_).

Examples
--------

The example code in `mnt_cycles_examples.py` shows how to find an MNT cycle with a given fundamental discriminant.
