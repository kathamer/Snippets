"""
Base64Encode
Encode data in Base64
By Dylan Hamer
"""

import base64  # Base64 library

def main():
    text = "Hello, World!"
    encoded = base64.b64encode(text)
    print(encoded)
    
main()
