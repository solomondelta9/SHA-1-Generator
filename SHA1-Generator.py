from Cryptodome.Hash import SHA1
message="secret"
h=SHA1.new()
h.update(message.encode())
print(h.hexdigest())
