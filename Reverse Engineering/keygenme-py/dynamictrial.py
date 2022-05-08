import hashlib

dynamic_trial = "".join([hashlib.sha256(b"FRASER").hexdigest()[x] for x in [4,5,3,6,2,7,1,8]])

print(dynamic_trial)