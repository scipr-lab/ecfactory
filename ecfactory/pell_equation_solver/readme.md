Pell Equation Solver
===================

Overview
--------

This module implements an algorithm to solve generalized Pell equations, following the procedure described in [\[KT07\]](/references/Karabina Teske 2007 --- On prime-order elliptic curves with embedding degrees k = 3,4, and 6.pdf). This module contains two files:

* `pell_equation_solver.py`, which contains the algorithm to solve Pell equations;

* `pell_equation_solver_examples.py`, which contains code examples.

Methods
-------

The main method in `pell_equation_solver.py` is

```python
pell_solve(D, m)
```

It solves the generalized Pell equation _x_<sup>2</sup> - *Dy*<sup>2</sup> = _m_. The algorithm outputs a list where: (a) the first element is the minimal solution (_x_<sub>0</sub>, _y_<sub>0</sub>) to _x_<sup>2</sup> − *Dy*<sup>2</sup> = 1; (2) the second element is a list containing a primitive solution to _x_<sup>2</sup> − _Dy_<sup>2</sup> = _m_ for each solution class.

Examples
--------

The example code in `pell_equation_solver_examples.py` shows how to run the code to solve generalized Pell equations.