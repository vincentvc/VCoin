from ecdsa import SigningKey, VerifyingKey, NIST384p
sk = SigningKey.generate(curve=NIST384p)
vk = sk.get_verifying_key()
vk_string = vk.to_string()
vk2 = VerifyingKey.from_string(vk_string, curve=NIST384p)
# vk and vk2 are the same key


print(type('123'.encode()))
print(type('123'))
print(sk.to_string().hex())