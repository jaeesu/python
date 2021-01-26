import hashlib

h = hashlib.sha256()
h.update(b'Kim')
result = h.hexdigest()
print(result)
