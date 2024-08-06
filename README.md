# ATTENTION

this is test project, it could be not secure to use in production

# About Code

Some terms:
- prime q - prime_q or just q
- prime p - prime_p or just p
- private exponent - exp_d or just d
### rsa_gen

Here I generate rsa, from two primes

I choosed the easiest way to generate priv exponent **(d)**, so I use formula. Where **(k)** is random integer that make our **(d)** integer number, not float. So I'm just bruteforce this number. Another way is using Evglid algorithm and Bezout's ratio. But it is algorithm, it harder. So I choosed formula, this was in school, it easy, take formula insert numbers and count

Here the formula to find **(d)**
```math
d=\frac{k*phi(n)+1}{e}
```

The code return tuple - prime_p, prime_q, n_num, phi_from_n_num, exp_d

### prime_numbers
These code generate prime numbers/ I use Miller-Rabbin tests for check primelity of number

Code return list of eight prime numbers

### phrase_to_hash 
These code make hash mnemo phrase and return hex formatted hash

I use Scrypt as hashing algorithm with 128 byte lenth of output string



### PS
main project site - https://github.com/purum-pum-pum/Mnemo-SSH