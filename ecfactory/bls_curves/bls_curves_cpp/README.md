# bls_curves_cpp

This module provides a fast C++ implementation for finding Barreto-Lynn-Scott curve parameters.

## Installation

### Ubuntu 14.04

Install GMP and NTL:

```
sudo apt-get install libgmp3-dev liblstl27
```

### macOS

Install Homebrew:

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
```

Install GMP:

```
brew install gmp
```

Install NTL:

```
brew install ntl
```

## Run

Compile with:

```
g++ -o bls_search bls_search.cpp -lntl -lgmp
```

Run with:

```
./bls_search {seed for RNG} {even_shift_of_x} {2-adicity}
```

For example, using the seed 100, and sampling values of x that are multiples of 2^2, looking for a two adicity of 10, would be:

```
./bls_search 100 2 10
```

## Log and analyze

We provide a statistics script to generate a histogram of findings. To use it, log the output of `bls_search` as follows:

```
./bls_search 100 2 10 > log.txt
```

Then use `bls_statistics` on the log as follows:

```
./bls_statistics log.txt
```
