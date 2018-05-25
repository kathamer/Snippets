"""
GenerateHash
Generate a sha256 hash
By Dylan Hamer
"""

import hashlib  # Hashing library

def generateHash(data):
    encodedData = data.encode()  # Encode data as raw binary data
    hashObject = hashlib.sha256(encodedData)  # Generate a hashlib hash object of the data
    hashText = hashObject.hexdigest()  # Get hash data as raw text
    return hashText
  
