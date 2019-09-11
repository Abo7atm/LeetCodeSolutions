# https://leetcode.com/problems/defanging-an-ip-address/
# Passed: 16ms, 11.5MB

def defangIPaddr(self, address: str) -> str:
    return address.replace('.', '[.]')
