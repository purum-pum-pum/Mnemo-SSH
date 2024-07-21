import random, os
from prime_numbers import generateLargePrime
from rsa_gen import gen_rsa_key
from english_bip39 import list_of_englishWords
from phrase_to_hash import phrase_to_hash
from NIST_tests.RunTest import RunTest


seed_part1 = input("Input some random data ")
seed_part2 = input("Please input more randomness")


seed_for_random = seed_part1 + "  " + seed_part2 + "  " + str(os.urandom(129))
random.seed(seed_for_random)
Mnemo_phrase = []
test_for_bigest_block_n_number = 0



def create_SSH_keey():
    checks_rsa_key = 0
    for i in range (0, 12):
        Mnemo_phrase.append(random.choice(list_of_englishWords))
        
    hash_Mnemo_phrase = phrase_to_hash(str(Mnemo_phrase))

    print("Hash from Scrypt  ####")
    print(hash_Mnemo_phrase)

    print("##################")
    print("   ")

    random.seed(hash_Mnemo_phrase)

    generated_primes = generateLargePrime(3072)

    print("your secret phrase  ###### ")
    print(Mnemo_phrase)

    print("######")
    print("list of primes  ", generated_primes)


    i=0
    while checks_rsa_key != 2:
    
        RSA_Private_KEY = gen_rsa_key(generated_primes[i], generated_primes[i+1])

        test_for_bigest_block = "True" in str(RunTest.longest_one_block_test(bin(RSA_Private_KEY[2])[:1000000]))

        i=i+1
    
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

    print(RSA_Private_KEY, checks_rsa_key)


def recover_SSH_key (input_MnemoPhrase):
    checks_rsa_key = 0


    hash_Mnemo_phrase = phrase_to_hash(str(input_MnemoPhrase))

    print("Hash from Scrypt  ####")
    print(hash_Mnemo_phrase)

    print("##################")
    print("   ")

    random.seed(hash_Mnemo_phrase)

    generated_primes = generateLargePrime(3072)

    print("######")
    print("list of primes  ", generated_primes)


    i=0
    while checks_rsa_key != 2:
    
        RSA_Private_KEY = gen_rsa_key(generated_primes[i], generated_primes[i+1])

        test_for_bigest_block = "True" in str(RunTest.longest_one_block_test(bin(RSA_Private_KEY[2])[:1000000]))

        i=i+1
    
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

    print(RSA_Private_KEY, checks_rsa_key)



##create_SSH_keey()

recover_SSH_key(input_MnemoPhrase=['extend', 'velvet', 'win', 'diet', 'fix', 'inspire', 'casino', 'stereo', 'trash', 'dinner', 'fish', 'bronze'])
