'''
LEETCODE 1108: Defanging an IP Address 
'''

address = "1.1.1.1"

def defangIPaddr(address: str) -> str: 
    address = address.replace(".", "[.]")
    return address 

print(defangIPaddr(address=address))