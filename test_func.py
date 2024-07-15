import os, random
from rsa_gen import gen_rsa_key
from prime_numbers import generateLargePrime

#random.seed("rfg48efr   r4##$ FFF  f F#$@%T5tggtv4nbui4bg9ubfgu3i  VVVCR#G$%$%T f vr3T$%$%$#$GR$ t5445wggvr44r ff   f53uh45gu4r5g  fr33r4g F$RGgf45gg5445gg  FG$%$%t"+str(os.urandom(128)))

generated_primes = generateLargePrime(256)

print("########")
print("list of primes  ", generated_primes)

print("")
print("#########")
print(gen_rsa_key(generated_primes[1],generated_primes[2]))

funci=gen_rsa_key(generated_primes[1], generated_primes[2])

print(type(funci))
print(funci[2])