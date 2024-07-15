from rsa_gen import gen_rsa_key
from prime_numbers import generateLargePrime


generated_primes = generateLargePrime(256)

print("########")
print("list of primes  ", generated_primes)

print("")
print("#########")
print(gen_rsa_key(generated_primes[1],generated_primes[2]))

funci=gen_rsa_key(generated_primes[1], generated_primes[2])

print(type(funci))
print(funci[2])