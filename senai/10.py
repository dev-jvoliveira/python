def classificar_participacao(respostas_positivas):
    if respostas_positivas == 2:
        return "Suspeita"
    elif 3 <= respostas_positivas <= 4:
        return "Cúmplice"
    elif respostas_positivas == 5:
        return "Assassino"
    else:
        return "Inocente"


perguntas = [
    "Telefonou para a vítima? (s/n)",
    "Esteve no local do crime? (s/n)",
    "Mora perto da vítima? (s/n)",
    "Devia para a vítima? (s/n)",
    "Já trabalhou com a vítima? (s/n)"
]


respostas_positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta).strip().lower()
    if resposta == 's':
        respostas_positivas += 1

classificacao = classificar_participacao(respostas_positivas)

print(f"A pessoa é classificada como: {classificacao}")
