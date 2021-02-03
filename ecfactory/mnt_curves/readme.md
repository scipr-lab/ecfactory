MNT Curves
==========

Overview
--------

This module provides functionality to construct _Miyaji-Nakabayashi-Takano (MNT) curves_, following the procedure described in [\[KT07\]](/references/Karabina%20Teske%202007%20---%20On%20prime-order%20elliptic%20curves%20with%20embedding%20degrees%20k%20%3D%203%2C4%2C%20and%206.pdf). The module contains two files:

* `mnt_curves.py`, which contains the algorithm to construct MNT curves;

* `mnt_curves_examples.py`, which contains code examples.

Throughout,
_q_ denotes the prime size of the base field;
_t_ denotes the trace of Frobenius;
_r_ denotes the prime size of the group;
_k_ denotes the embedding degree;
_D_ denotes the (negative) fundamental discriminant.


Methods
-------

The main method in `mnt_curves.py` is

```python
make_curve(k, D)
```

It finds all MNT curves with embedding degree _k_ and fundamental discriminant _D_. The method outputs a list of all such curves, with each curve represented as a tuple (_q_,_t_,_r_,_k_,_D_).

Examples
--------

The file `mnt6_enumeration.csv` contains a list of all MNT curves with _k_ = 6 and -_D_ < 200000, ordered by -_D_. The example code in `mnt_curves_examples.py` shows how to generate this file, and how to find an MNT curve with a given embedding degree and fundamental discriminant. 