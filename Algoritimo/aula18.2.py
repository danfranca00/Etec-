try:
 ouro = float(input("Total de ouro encontrado: "))
 membros = int(input("Dividir por quantos heróis na equipe? "))

 cada_um = ouro / membros

 print(f"Cada aventureiro recebe {cada_um:.2f} moedas de ouro.")

except ZeroDivisionError:     
 print("X Maldição Matemáticas: Não pode dividir tesouros com o nada (zero pessoas)!")
except ValueError:
 print("X Erro de Escrita: Introduz apenas valores numéricos válidos.")