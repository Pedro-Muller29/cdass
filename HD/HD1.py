with open('input.txt') as f:
    data = [[int(y) for y in x.split(",")] for x in f.readlines()]

data = data[0]


lista = [x for x in range(256)]


def inverter_Sublista(idx, comp):
    global lista
    sub_inicio = []
    sub_fim = []

    if idx+comp >= len(lista):
        if comp >= len(lista):
            idx_inicio = idx
            idx_fim = len(lista)
        else:
            idx_inicio = (idx + comp) % len(lista)
            idx_fim = len(lista)
    else:
        idx_fim = idx+comp
        idx_inicio = 0

    sub_fim = lista[idx:idx_fim]
    sub_inicio = lista[0:idx_inicio]
    
    aux = sub_fim + sub_inicio
    aux.reverse()
    novo_subFim = aux[:len(sub_fim)]
    novo_subinicio = aux[len(sub_fim):]
    lista = novo_subinicio + lista[idx_inicio: idx]+ novo_subFim + lista[idx_fim:]
        

idx = 0
salto = 0

for i in data:
    inverter_Sublista(idx, i)
    if i+salto == len(lista):
        pass
    else:
        idx = (idx+i+salto) % len(lista)
    salto += 1

print(lista[0] * lista[1])