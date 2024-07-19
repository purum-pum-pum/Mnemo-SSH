import random, os
from prime_numbers import generateLargePrime
from rsa_gen import gen_rsa_key
from english_bip39 import list_of_englishWords
from phrase_to_hash import phrase_to_hash
from NIST_tests.RunTest import RunTest

seed_for_random = "frefrfrefreerfreerggrerggreerggreerggreerggreergvgfgfar34r32rf32f42 r3223 r323r" + str(os.urandom(129))
random.seed(seed_for_random)
Mnemo_phrase = []
test_for_bigest_block_n_number = 0

for i in range (0, 12):
    Mnemo_phrase.append(random.choice(list_of_englishWords))

hash_Mnemo_phrase = phrase_to_hash(str(Mnemo_phrase))

random.seed(hash_Mnemo_phrase)

generated_primes = generateLargePrime(3072)


print("######")
print("list of primes  ", generated_primes)

RSA_Private_KEY = gen_rsa_key(random.choice(generated_primes), random.choice(generated_primes))
test_for_bigest_block_n_number = RSA_Private_KEY[2]

while checks_rsa_key != 2:
    test_for_bigest_block = "True" in str(RunTest.longest_one_block_test(bin(RSA_Private_KEY[2])[:1000000]))
    
    list_for_distance=[]
    
    if RSA_Private_KEY[0]-RSA_Private_KEY[1] > 0:
        list_for_distance.append(RSA_Private_KEY[0])
        list_for_distance.append(RSA_Private_KEY[1])  
    else:
        list_for_distance.append(RSA_Private_KEY[1])
        list_for_distance.append(RSA_Private_KEY[0])

    if list_for_distance[0]-list_for_distance[1] > 3351951982485649274893506249551461531869841455148098344430890360930441007518386744200468574541725856922507964546621512713438470702986642486608412251521024:
        test_distance_p_and_q = True
    else:
        test_distance_p_and_q = False

    checks_rsa_key = test_distance_p_and_q + test_for_bigest_block