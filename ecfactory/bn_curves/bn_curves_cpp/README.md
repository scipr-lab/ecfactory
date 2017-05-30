# bn_curves_cpp

This module provides a fast C++ implementation for finding Barreto-Naehrig curve parameters.

## Installation

### Ubuntu 14.04

Install GMP and NTL:
```
sudo apt-get install libgmp3-dev libntl27
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
g++ -o bn_search bn_search.cpp -lntl -lgmp
```

Run with:
```
./bn_search {seed for RNG} {even_shift_of_x} {2-adicity}
```

For example, using the seed 100, and sampling values of x that are multiples of 2^2, looking for a two adicity of 10, would be:
```
./bn_search 100 2 10
```

## Log and analyze

We provide a statistics script to generate a histogram of findings. To use it, log the output of `bn_search` as follows:
```
./bn_search 100 2 10 > log.txt
```

Then use `bn_statistics` on the log as follows:
```
./bn_statistics log.txt
```
