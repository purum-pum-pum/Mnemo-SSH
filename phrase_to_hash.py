import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

salt = os.urandom(16)
# derive

def phrase_to_hash(some_wods):
    kdf = Scrypt(

    salt=str.encode("fhdfhd u7r43ujc d e2nh34ru4388 iu jdj23j34r 8"),
    length=128,
    n=2**16,
    r=8,
    p=3,
    )
    key = kdf.derive(str.encode(some_wods))

    kdf = Scrypt(

    salt=str.encode("fhdfhd u7r43ujc d e2nh34ru4388 iu jdj23j34r 8"),
    length=128,
    n=2**16,
    r=8,
    p=3,
    )
    kdf.verify(str.encode(some_wods), key)

    return key.hex()