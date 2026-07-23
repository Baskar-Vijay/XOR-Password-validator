# XOR-Password-validator 
## Inherent dangers of using XOR to validate password or username
1. The system is prone to timing attack.The attacker can determine which bits  are correct by evaluating the time taken for response, given the passwords are compared directly in plaintext.
## How to leverage SHA-256 to make the password checking a tad bit secure
## benefits of SHA-256 
1. It makes use of a one way hashing method.The hash cannot be simply reversed.
2. A small change in the plaintext can cause a hugh variablilty in the ouput hash.This means the hacker cannot reliably get the password from the system
## disadvantages of SHA-256 in this system
1.  malicious actor can still make use of the timing attack to discover the hash value.
  1. with the hash value,the hacker will compare against hash values of common passwords to discover the plaintext
  2. or the hacker may harvest now; decrypt later when the computing catches up.
## Implementation
1. classxor.py and classxor.py uses classes to call the logic or function
2. importingfunction.py and passwordvalidator.py uses calling function.

## Too many security mechanisms can ruin the total security of the system
1. This XOR introduces a risk of exposing password hash of any given user.
## Alternatives
1. A simple hash comparison method 
``` hash == hash2 ```  will be effective and more secure
2. Force the system to use time to return  response after the set time has elapsed from start of validation.



