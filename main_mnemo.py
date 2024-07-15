import random, os
from prime_numbers import generateLargePrime
from rsa_gen import gen_rsa_key

seed_for_random = "frefrfrefreerfreerggrerggreerggreerggreerggreergvgfgfar34r32rf32f42 r3223 r323r" + str(os.urandom(129))
random.seed(seed_for_random)

generated_primes = generateLargePrime(3072)


print("######")
print("list of primes  ", generated_primes)


RSA_Private_KEY = gen_rsa_key(random.choice(generated_primes), random.choice(generated_primes))


