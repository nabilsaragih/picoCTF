import base64

# cat.jpg XMP:License
license = "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"

print(base64.b64decode(license))