from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario('Gui')
yuri = Usuario('Yuri')

leilao = Leilao('Celular')

lance_do_gui = Lance(gui, 150)
lance_do_yuri = Lance(yuri, 100)

leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_yuri)

for lance in leilao.lances:
    print(f'O lance do {lance.usuario.nome} foi de {lance.valor}')

avaliador = Avaliador()

avaliador.avalia(leilao)

print(f'O menor lance foi {avaliador.menor_lance} e o maior lance foi {avaliador.maior_lance}')