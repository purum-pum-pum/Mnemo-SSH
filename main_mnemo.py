import random, os
from prime_numbers import generateLargePrime
from rsa_gen import gen_rsa_key
from english_bip39 import list_of_englishWords
from phrase_to_hash import phrase_to_hash

seed_for_random = "frefrfrefreerfreerggrerggreerggreerggreerggreergvgfgfar34r32rf32f42 r3223 r323r" + str(os.urandom(129))
random.seed(seed_for_random)
Mnemo_phrase = []

for i in range (0, 12):
    Mnemo_phrase.append(random.choice(list_of_englishWords))

hash_Mnemo_phrase = phrase_to_hash(str(Mnemo_phrase))

random.seed(hash_Mnemo_phrase)

generated_primes = generateLargePrime(3072)


print("######")
print("list of primes  ", generated_primes)


RSA_Private_KEY = gen_rsa_key(random.choice(generated_primes), random.choice(generated_primes))


