from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP

# Preparation du generateur
generateur = Random.new().read
cle = RSA.generate(1024, generateur)  # Generation d'un pair de cles publique et prive
cle_publique = cle.publickey() # La cle publique
encryptor = PKCS1_OAEP.new(cle_publique)
# Chiffrement
message_crypte = encryptor.encrypt('la securite des donnes personnel et son future avec RSA ') # Message a crypte
print 'Message chiffre:'
print str(message_crypte)

# Dechiffrement
decryptor = PKCS1_OAEP.new(cle)
message_decrypte = decryptor.decrypt(str(message_crypte))
print 'Message dechiffre'
print message_decrypte
