from televisao import televisao

tv1 = televisao("Samsung", 40)
tv2 = televisao("LG", 50)
tv3 = televisao("TCL", 55)


televisores = [tv1, tv2, tv3]

tv1.ligada = True
tv2.ligada = True

tv1.canal = 10
tv1.volume = 18

tv2.canal = 9
tv2.volume = 47

ligados = 0
maior = None
total_polegadas = 0

for tv in televisores:
    if tv.ligada:
        print(f"{tv.marca} {tv.polegadas}\" | Ligada | Canal {tv.canal} | Volume {tv.volume}")
        ligados += 1
    else:
        print(f"{tv.marca} {tv.polegadas}\" | Desligada")

    total_polegadas += tv.polegadas

    if maior is None or tv.polegadas > maior.polegadas:
        maior = tv

print(f"Televisores ligados: {ligados}")
print(f"Maior televisor: {maior.marca} {maior.polegadas}\"")
print(f"Média de polegadas: {total_polegadas / len(televisores):.2f}")