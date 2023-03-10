#include <cstdio>
#include <iostream>
#include <vector>
#include <NTL/ZZ.h>
#include <NTL/tools.h>

using namespace std;
using namespace NTL;

#define REPORT_INTERVAL 100000
#define MAX_R_BITS 255

/*
  This code modifies the method of [BLS02] to search for candidate parameters of
  Barreto-Lynn-Scott curves with high 2-adicity. (The curve itself can be explicitly
  constructed by following the method described in [BLS02].)

  [BLS02]   = "Constructing Elliptic Curves with Prescribed Embedding Degrees"
*/

ZZ r_(ZZ x)
{
    ZZ x2 = x * x;
    ZZ x3 = x2 * x;
    ZZ x4 = x3 * x;
    return x4 - x2 + 1;
}

ZZ q_(ZZ x)
{
    ZZ r = r_(x);
    ZZ q = (x - 1) * (x - 1) * r;

    bool q_is_int = q % 3 == 0;
    if (!q_is_int)
    {
        return ZZ(0);
    }

    return q / 3 + x;
}

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

    /* |x| ~ 64 bits so that |r| = 4 * |x| ~ 256 bits */
    long num_x_bits = 64;

    long num_iters = 0;
    long num_found = 0;

    SetSeed(seed);

    /**
     * Compute candidate BLS parameters using the formulas:
     * r = x^4 - x^2 + 1
     * q = ((x-1)^2 * r) / 3 + x
     * (see [BLS02])
     */

    while (1)
    {
        num_iters += 4;

        /* Sample x */
        ZZ x = RandomLen_ZZ(num_x_bits);

        /**
         * Make x even and divisible by a large power of 2 to improve two adicity.
         * The resulting r is s.t. -1 is a square in Fq.
         */

        x = ((x >> even_offset) << even_offset);
        ZZ r = r_(x);
        ZZ q = q_(x);

        long num_q_bits = NumBits(q);
        long num_r_bits = NumBits(r);
        long two_adicity = NumTwos(r - 1);

        if (num_r_bits > MAX_R_BITS)
        {
            continue;
        }

        if (ProbPrime(r) && ProbPrime(q) && (two_adicity >= wanted_two_adicity))
        {
            cout << "x = " << x << "\n";
            cout << "q = " << q << "\n";
            cout << "r = " << r << "\n";
            cout << "log2(q) =" << num_q_bits << "\n";
            cout << "log2(r) =" << num_r_bits << "\n";
            cout << "ord_2(r-1) = " << two_adicity << "\n";
            cout.flush();
            ++num_found;
        }

        /**
         * -x will yield the same r, but a different q.
         */

        q = q_(-x);

        num_q_bits = NumBits(q);
        num_r_bits = NumBits(r);
        two_adicity = NumTwos(r - 1);

        if (num_r_bits > MAX_R_BITS)
        {
            continue;
        }

        if (ProbPrime(r) && ProbPrime(q) && (two_adicity >= wanted_two_adicity))
        {
            cout << "x = " << -x << "\n";
            cout << "q = " << q << "\n";
            cout << "r = " << r << "\n";
            cout << "log2(q) =" << num_q_bits << "\n";
            cout << "log2(r) =" << num_r_bits << "\n";
            cout << "ord_2(r-1) = " << two_adicity << "\n";
            cout.flush();
            ++num_found;
        }

        /**
         * An x of the form k.2^n + 1 also yields a scalar field with high (n+1) two adicity.
         */

        x = x + 1;
        r = r_(x);
        q = q_(x);

        num_q_bits = NumBits(q);
        num_r_bits = NumBits(r);
        two_adicity = NumTwos(r - 1);

        if (num_r_bits > MAX_R_BITS)
        {
            continue;
        }

        if (ProbPrime(r) && ProbPrime(q) && (two_adicity >= wanted_two_adicity))
        {
            cout << "x = " << x << "\n";
            cout << "q = " << q << "\n";
            cout << "r = " << r << "\n";
            cout << "log2(q) =" << num_q_bits << "\n";
            cout << "log2(r) =" << num_r_bits << "\n";
            cout << "ord_2(r-1) = " << two_adicity << "\n";
            cout.flush();
            ++num_found;
        }

        /**
         * -x will yield the same r, but a different q.
         */

        q = q_(-x);

        num_q_bits = NumBits(q);
        num_r_bits = NumBits(r);
        two_adicity = NumTwos(r - 1);

        if (num_r_bits > MAX_R_BITS)
        {
            continue;
        }

        if (ProbPrime(r) && ProbPrime(q) && (two_adicity >= wanted_two_adicity))
        {
            cout << "x = " << -x << "\n";
            cout << "q = " << q << "\n";
            cout << "r = " << r << "\n";
            cout << "log2(q) =" << num_q_bits << "\n";
            cout << "log2(r) =" << num_r_bits << "\n";
            cout << "ord_2(r-1) = " << two_adicity << "\n";
            cout.flush();
            ++num_found;
        }

        if (num_iters % REPORT_INTERVAL == 0)
        {
            printf("[ num_iters = %ld , num_found = %0.2f per %d ]\n", num_iters, 1. * REPORT_INTERVAL * num_found / num_iters, REPORT_INTERVAL);
            fflush(stdout);
        }
    }
}
