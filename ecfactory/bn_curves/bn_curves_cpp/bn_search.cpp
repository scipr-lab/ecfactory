#include <cstdio>
#include <iostream>
#include <vector>
#include <NTL/ZZ.h>
#include <NTL/tools.h>

using namespace std;
using namespace NTL;

#define REPORT_INTERVAL	100000
#define MAX_Q_BITS 255

/*
  This code modifies [Algorithm 1, BN06] to search for candidate parameters of
  Barreto-Naehrig curves with high 2-adicity. (The curve itself can be explicitly
  constructed by following the second half of [Algorithm 1, BN06].)

  This code was used to find the BN curve in [BCTV13].

  [BCTV13] = "Succinct Non-Interactive Arguments for a von Neumann Architecture"
  [BN06]   = "Pairing-Friendly Elliptic Curves of Prime Order"
*/

int main(int argc, char **argv)
{
    if (argc != 4)
    {
        cout << "usage: " << argv[0] << " [rand_seed even_offset wanted_two_adicity]\n";
        return 0;
    }

    /* Collect inputs */
    ZZ seed;
    conv(seed, atoi(argv[1]));
    long even_offset = atoi(argv[2]);
    long wanted_two_adicity = atoi(argv[3]);

    /* |x| ~ 64 bits so that |q| = 4 * |x| ~ 256 bits */
    long num_x_bits = 63;

    long num_iters = 0;
    long num_found = 0;

    SetSeed(seed);
    while (1)
    {
        ++num_iters;

        /* Sample x */
        ZZ x = RandomLen_ZZ(num_x_bits);

        /**
         * Make x even and divisible by a large power of 2 to improve two adicity.
         * The resulting q is s.t. -1 is a square in Fq.
         */
        x = ((x >> even_offset) << even_offset);

        /* Uncomment to make x odd and ensure that -1 is a nonsquare in Fq. */
        // SetBit(x, 0);

        /**
         * Compute candidate BN parameters using the formulas:
         * t = 6*x^2 + 1,
         * q = 36*x^4 + 36*x^3 + 24*x^2 + 6*x + 1
         * r = q - t + 1
         * (see [BN06])
         */
        ZZ x2 = x * x;
        ZZ x3 = x2 * x;
        ZZ x4 = x3 * x;
        ZZ t = 6 * x2 + 1;
        ZZ q = 36 * x4 + 36 * x3 + 24 * x2 + 6 * x + 1;
        ZZ r = q - t + 1;

        long num_q_bits = NumBits(q);
        long two_adicity = NumTwos(r-1);

        if (num_q_bits > MAX_Q_BITS)
        {
            continue;
        }

        if (ProbPrime(r) && ProbPrime(q) && (two_adicity >= wanted_two_adicity))
        {
            cout << "x = " << x << "\n";
            cout << "q = " << q << "\n";
            cout << "r = " << r << "\n";
            cout << "log2(q) =" << num_q_bits << "\n";
            cout << "ord_2(r-1) = " << two_adicity << "\n";
            cout.flush();
            ++num_found;
        }

        if (num_iters % REPORT_INTERVAL == 0)
        {
            printf("[ num_iters = %ld , num_found = %0.2f per %d ]\n", num_iters, 1.*REPORT_INTERVAL*num_found/num_iters, REPORT_INTERVAL);
            fflush(stdout);
        }
    }
}
