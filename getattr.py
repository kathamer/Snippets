"""
GetAttr
Example of using getattr
By Dylan Hamer
"""

class example:
    def __init__(self):
        self.text = "Hello, World!"  # Set class atribute to be retrieved later
        
def main():
    exampleClass = example()  # Class to get from
    toGet = "text"  # Attribute to get from class
    attribute = getattr(exampleClass, toGet)  # Get attribute from class
    print(attribute)  # Display the attribute (Should output: 'Hello, World!')
    
main()
    
