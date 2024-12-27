import uuid

def gerar_uuids(quantidade):
    uuids = [str(uuid.uuid4()) for _ in range(quantidade)]
    return uuids

quantidade = int(input("Quantos UUIDs você quer gerar? "))

uuids = gerar_uuids(quantidade)

with open("UUID_v4.txt", "w") as arquivo:
    for uid in uuids:
        arquivo.write(uid + "\n")

print(f"{quantidade} UUIDs gerados e salvos no arquivo UUID_v4.txt")
