print(" KarlaMag's Hotel versão 0.1.1 \n ")

disponiveis = {
    1:{'quartos': list(range(91,101)), 'valor':325.5},
    2:{'quartos': list(range(61,91)), 'valor':210},
    3:{'quartos': list(range(31,61)), 'valor':135.2},
    4:{'quartos': list(range(5,31)), 'valor':99.99}
 }

reservados = {}

def obter_quartos_livres(categoria):
    quartos_livres = []

    quartos_disponiveis = disponiveis[categoria]['quartos']
    for quarto in quartos_disponiveis:
        if quarto not in reservados:
            quartos_livres.append(quarto)      
    return quartos_livres


programa_aberto = True 
while programa_aberto == True:
    categoria = int(input('Olá, insira aqui a categoria do quarto:').strip())
    quartos_disponiveis = obter_quartos_livres(categoria)
    if not quartos_disponiveis:
        outra_categoria = input(
            'Não temos quartos disponiveis nessa categoria,' 
            'gostaria de selecionar outra categoria?'
        )
        if outra_categoria.strip().lower() == 'sim': 
            continue
        else: 
            break
        #(;;;;;;;;;;;;;;;;;;;)

    quarto_escolhido = int(input(f'Escolha entre os quartos disponíveis: {quartos_disponiveis}'))
    while quarto_escolhido not in quartos_disponiveis:
        quarto_escolhido = int(
            input(
                'O quarto não está disponível, informe outro quarto: \n'
                f'Os quartos disponíveis são: {quartos_disponiveis}'
            ).strip()
        )
        
    hospede = input('A reserva estará em nome de quem?')
    diarias = int(input('Quantas diárias?'))
    while diarias < 3 or diarias > 15:
        diarias = int(input('O Valor não é válido, informe novamente o valor:').strip())
    valor_total_diarias = diarias * disponiveis[categoria]['valor']

    print(f'''Resumo da reserva: 
    Nome do responsável: {hospede}
    Numero do quarto: {quarto_escolhido} 
    Diárias: {diarias}
    Valor total: {valor_total_diarias}    
    ''')

    confirma = input('Gostaria de confirmar a reserva?')
    if confirma.strip().lower() != 'sim':
          continue  
    reservados[quarto_escolhido] = {'hospede':hospede, 'Diarias':diarias }
