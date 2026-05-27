nome = input("Nome do heroi: ")
xp = int(input("Quanto XP acomulaste? "))

if xp < 1000:
    rank = "aprendiz"
elif xp < 5000:
    rank  = "guerreiro"
else:
    rank = "Lenda"
    print (f"O aventireiro {nome} é um: {rank}!" )