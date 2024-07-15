import random, os
from prime_numbers import generateLargePrime

seed_for_random = "frefrfrefreerfreerggrerggreerggreerggreerggreergvgfgfar34r32rf32f42 r3223 r323r" + str(os.urandom(129))
random.seed(seed_for_random)

generated_primes = generateLargePrime(3072)

print(generated_primes)


