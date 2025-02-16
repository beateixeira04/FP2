ORD_A = ord('A')
ORD_I = ord('I')
ORD_M = ord('M')
ORD_S = ord('S')

#TAD-Interseção-------------------------------------------------------------------------------------

def cria_intersecao(coluna, linha):
    if not isinstance(coluna, str) or len(coluna) != 1 or ord(coluna) < ORD_A or ord(coluna) > ORD_S \
    or not isinstance(linha, int) or isinstance(linha, bool) or linha < 1 or linha > 19: #Validar os argumentos
        raise ValueError('cria_intersecao: argumentos invalidos')
    return (coluna, linha)
        
def obtem_col(intersecao):
    return intersecao[0]

def obtem_lin(intersecao):
    return intersecao[1]

def eh_intersecao(intersecao):
        if (
        isinstance(intersecao, tuple) #Tem que ser um tuplo
        and len(intersecao) == 2 #Tem que ter apenas 2 elementos
        and isinstance(intersecao[0], str) #Primeiro elemento é uma string
        and len(intersecao[0]) == 1 #A string tem comprimeiro = 1
        and ord(intersecao[0]) <= ORD_S
        and ord(intersecao[0]) >= ORD_A #Só pode ir de 'A' a 'S'
        and isinstance(intersecao[1], int) #Segundo elemento é um número inteiro
        and not isinstance(intersecao[1], bool)
        and intersecao[1] <= 19
        and intersecao[1] > 0 #Só pode ir de 1 a 99
        ):
            return True
        return False

def intersecao_para_str(intersecao):
    resultado = f"{obtem_col(intersecao)}{obtem_lin(intersecao)}"
    return resultado

def str_para_intersecao(intersecao_str):
    resultado = ()
    for elemento in intersecao_str:
        if ord(elemento) <= ORD_S and ord(elemento) >= ORD_A:
            resultado += (elemento, )
            break
    for elemento in range(len(intersecao_str)):
        if len(intersecao_str) == 3:
            linha = int(intersecao_str[1] + intersecao_str[2])
            resultado += (linha, )
            break
        else:
            resultado += (int(intersecao_str[1]), )
            break
    return resultado

def intersecoes_iguais(intersecao_a, intersecao_b):
    if isinstance(intersecao_a, str):
        a = str_para_intersecao(intersecao_a)
    if isinstance(intersecao_b, str):
        b = str_para_intersecao(intersecao_b)
    return obtem_col(intersecao_a) == obtem_col(intersecao_b) \
    and obtem_lin(intersecao_a) == obtem_lin(intersecao_b)


def obtem_intersecoes_adjacentes(intersecao, limite):
    adjacentes = ()
    if obtem_lin(intersecao) > 1:
        adjacentes += (cria_intersecao(obtem_col(intersecao), obtem_lin(intersecao) - 1), )
    if ord(obtem_col(intersecao)) > ORD_A:
        linha = obtem_lin(intersecao)
        coluna = chr(ord(obtem_col(intersecao)) - 1)
        adjacentes += (cria_intersecao(coluna, linha), )
    if ord(obtem_col(intersecao)) < ord(obtem_col(limite)):
        linha = obtem_lin(intersecao)
        coluna = chr(ord(obtem_col(intersecao)) + 1)
        adjacentes += (cria_intersecao(coluna, linha), )
    if obtem_lin(intersecao) < obtem_lin(limite):
        adjacentes += (cria_intersecao(obtem_col(intersecao), obtem_lin(intersecao) + 1), )
    return adjacentes

def ordena_intersecoes(intersecoes):
    return tuple(sorted(intersecoes, key = lambda x: (x[1], x[0])))

#TAD-PEDRA------------------------------------------------------------------------------------------

def cria_pedra_branca():
    return 'O'

def cria_pedra_preta():
    return 'X'

def cria_pedra_neutra():
    return '.'

def eh_pedra(pedra):
    if pedra == 'O' or pedra == '.' or pedra == 'X':
        return True
    return False

def eh_pedra_branca(pedra):
    if pedra == 'O':
        return True
    return False
    
def eh_pedra_preta(pedra):
    if pedra == 'X':
        return True
    return False
    
def pedras_iguais(pedra_a, pedra_b):
    if eh_pedra_branca(pedra_a) and eh_pedra_branca(pedra_b) or eh_pedra_preta(pedra_a) and \
        eh_pedra_preta(pedra_b) or pedra_a == cria_pedra_neutra() and pedra_b == cria_pedra_neutra():
        return True
    return False

def pedra_para_str(pedra):
    return pedra
    
def eh_pedra_jogador(pedra):
    return eh_pedra_branca(pedra) or eh_pedra_preta(pedra)

#TAD-goban------------------------------------------------------------------------------------------

def cria_goban_vazio(tamanho):
    if tamanho not in (9,13,19):
        raise ValueError('cria_goban_vazio: argumento invalido')
    resultado = {}
    linha = 1
    while linha <= tamanho:
        coluna = ORD_A
        while coluna <= (tamanho + ORD_A) - 1:
            if f"{chr(coluna)}{linha}" not in resultado:
                resultado[f"{chr(coluna)}{linha}"] = '.'
            coluna += 1
        linha += 1
    return resultado

def obtem_ultima_intersecao(goban):
    if len(goban) == 9**2:
        return cria_intersecao('I', 9)
    elif len(goban) == 13**2:
        return cria_intersecao('M', 13)
    elif len(goban) == 19**2:
        return cria_intersecao('S', 19)

def eh_intersecao_valida(goban, intersecao):
    if isinstance(intersecao, str):
        return intersecao in goban
    if isinstance(intersecao, tuple):
        return intersecao_para_str(intersecao) in goban

def cria_goban(tamanho, pedras_brancas, pedras_pretas):
    if len(set(pedras_brancas) & set(pedras_pretas)) != 0 or tamanho not in (9,13,19):
        raise ValueError('cria_goban: argumentos invalidos')
    goban = cria_goban_vazio(tamanho)
    pretas = ()
    brancas = ()
    for intersecao in pedras_brancas:
        if not eh_intersecao_valida(goban, intersecao) or intersecao in brancas:
            raise ValueError('cria_goban: argumentos invalidos')
        brancas += (intersecao, )
        goban[intersecao_para_str(intersecao)] = 'O'
    for intersecao in pedras_pretas:
        if not eh_intersecao_valida(goban, intersecao) or intersecao in pretas:
            raise ValueError('cria_goban: argumentos invalidos')
        pretas += (intersecao, )
        goban[intersecao_para_str(intersecao)] = 'X'
    return goban

def cria_copia_goban(goban):
    brancas = ()
    pretas = ()
    tamanho = (len(goban) ** 0.5)
    for chave, valor in goban.items():
        if valor == 'O':
            brancas += (str_para_intersecao(chave), )
        if valor == 'X':
            pretas += (str_para_intersecao(chave), )
    return cria_goban(tamanho, brancas, pretas)

def obtem_pedra(goban, intersecao):
    intersecao_str = intersecao_para_str(intersecao)
    return goban[intersecao_str]
    
def obtem_cadeia(goban, intersecao):
    resultado = cadeia = (intersecao,)
    cor_pedra = obtem_pedra(goban, intersecao)
    while True:
        cadeia_temporaria = ()
        for intersecao_cadeia in cadeia: #Em cada ciclo vai estar a analisar interseções diferentes (Adjacente das adjacentes)
            adjacentes = obtem_intersecoes_adjacentes(intersecao_cadeia, obtem_ultima_intersecao(goban))
            for adjacente in adjacentes:
                if goban[intersecao_para_str(adjacente)] == cor_pedra and adjacente not in resultado:
                    resultado += (adjacente,)
                    cadeia_temporaria += (adjacente,)
        cadeia = cadeia_temporaria
        if len(cadeia) == 0:
            break
    return ordena_intersecoes(resultado)

def coloca_pedra(goban, intersecao, pedra):
    goban[intersecao_para_str(intersecao)] = pedra_para_str(pedra)
    return goban

def remove_pedra(goban, intersecao):
    goban[intersecao_para_str(intersecao)] = pedra_para_str(cria_pedra_neutra())
    return goban

def remove_cadeia(goban, conjunto_intersecoes):
    for intersecao in conjunto_intersecoes:
        remove_pedra(goban, intersecao)
    return goban

def eh_goban(goban): 
    if not isinstance(goban, dict):
        return False 
    if not eh_intersecao_valida(goban, obtem_ultima_intersecao(goban)):
        return False
    for key, value in goban.items():
        if not eh_intersecao_valida(goban, str_para_intersecao(key)):
            return False
        if value not in ('.', 'O', 'X'):
            return False
    return True

def gobans_iguais(universal_a, universal_b):
    if not eh_goban(universal_b) or not eh_goban(universal_a) or len(universal_a) != len(universal_b):
        return False
    for chave in universal_a.keys():
        if universal_a[chave] != universal_b[chave]:
            return False
    return True
    
def goban_para_str(goban):
    ultima_intersecao = obtem_ultima_intersecao(goban)
    linha_maxima = obtem_lin(ultima_intersecao)
    linha_temporaria = 1

    def lista_letras(): #Função para escrever as letras da string, já que se usa duas vezes.
        letra = ORD_A
        letras_str = ""
        while letra <= ord(obtem_col(ultima_intersecao)):
            letras_str += f" {chr(letra)}"
            letra += 1
        return letras_str

    goban_str = "  " + lista_letras()
    goban_str += "\n"
    while linha_maxima >= 1: #Adiciona o número da linha no início
        if linha_maxima < 10: #Se o número tiver 2 dígitos terá de ter um espaço a menos
            goban_str += " "
        goban_str += f"{linha_maxima}"
        for chave, valor in goban.items():
            if str(linha_maxima) in chave and (len(f"{linha_maxima}") + 1) == len(chave):
                goban_str += f" {valor}"
        if linha_maxima < 10: #Adiciona o número da linha no final
            goban_str += " "
        goban_str += f" {linha_maxima}"
        goban_str += "\n"
        linha_maxima -= 1
    goban_str += "  " + lista_letras()
    return goban_str

def obtem_territorios(goban):
    resultado = ()
    for chave in goban.keys():
        intersecao = str_para_intersecao(chave)
        if not eh_pedra_jogador(goban[chave]):
            valor = False
            for territorio in resultado:
                if intersecao in territorio:
                    valor = True
            if valor == False:
                terr = obtem_cadeia(goban, intersecao)
                resultado += (terr, )
    return resultado

def obtem_adjacentes_diferentes(goban, tuplo_intersecoes):
    valor_pedra = eh_pedra_jogador(obtem_pedra(goban, tuplo_intersecoes[0]))
    resultado = ()
    for intersecao in tuplo_intersecoes:
        adjacentes = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(goban))
        for adjacente in adjacentes:
            if eh_pedra_jogador(obtem_pedra(goban, adjacente)) != valor_pedra and adjacente \
            not in resultado:
                resultado += (adjacente, )
    return ordena_intersecoes(resultado)

def jogada(goban, intersecao, pedra):
    goban = coloca_pedra(goban, intersecao, pedra)
    if eh_pedra_branca(pedra):
        valor = cria_pedra_preta()
    if eh_pedra_preta(pedra):
        valor = cria_pedra_branca()
    adjacentes_jogada = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(goban))
    for adjacente in adjacentes_jogada:
        if goban[intersecao_para_str(adjacente)] == valor:
            cadeia_oposta = obtem_cadeia(goban, adjacente)
            adjacentes_diferentes = obtem_adjacentes_diferentes(goban, cadeia_oposta)
            if len(adjacentes_diferentes) == 0:
                goban = remove_cadeia(goban, cadeia_oposta)
    return goban
    
def obtem_pedras_jogadores(goban):
    brancas = pretas = 0
    for valor in goban.values():
        if eh_pedra_branca(valor):
            brancas += 1
        if eh_pedra_preta(valor):
            pretas += 1
    return (brancas, pretas)

#Funções-adicionais---------------------------------------------------------------------------------

def calcula_pontos(goban):
    brancas = pretas = 0
    for valor in goban.values():
        if eh_pedra_branca(valor):
            brancas += 1
        if eh_pedra_preta(valor):
            pretas += 1
    territorios = obtem_territorios(goban)
    for territorio in territorios:
        fronteira = obtem_adjacentes_diferentes(goban, territorio)
        if len(fronteira) == 0:
            continue
        valor = goban[intersecao_para_str(fronteira[0])]
        fronteira_uniforme = True
        for adjacente in fronteira:
            if goban[intersecao_para_str(adjacente)] != valor:
                fronteira_uniforme = False
                break
        if fronteira_uniforme == True:
            if eh_pedra_branca(valor):
                brancas += len(territorio)
            elif eh_pedra_preta(valor):
                pretas += len(territorio)
    return (brancas, pretas)

def eh_jogada_legal(goban, intersecao, pedra, goban_b):
    copia = cria_copia_goban(goban)
    jogada(copia, intersecao, pedra)
    if copia == goban_b:
        return False
    copia_b = cria_copia_goban(goban)
    copia_b = coloca_pedra(copia_b, intersecao, pedra)
    if eh_pedra_branca(pedra):
        valor = cria_pedra_preta()
    if eh_pedra_preta(pedra):
        valor = cria_pedra_branca()
    adjacentes_jogada = obtem_intersecoes_adjacentes(intersecao, obtem_ultima_intersecao(copia_b))
    for adjacente in adjacentes_jogada:
        if copia_b[intersecao_para_str(adjacente)] == valor:
            cadeia_oposta = obtem_cadeia(copia_b, adjacente)
            adjacentes_diferentes = obtem_adjacentes_diferentes(copia_b, cadeia_oposta)
            if len(adjacentes_diferentes) != 0:
                return False
    else:
        return True
    
def turno_jogador(goban, pedra, goban_b):
    jogada = input(f"Escreva uma intersecao ou 'P' para passar [{pedra}]: ")
    if jogada == 'P':
        return False
    elif not eh_intersecao_valida(goban, str_para_intersecao(jogada)):
        return turno_jogador(goban, pedra, goban_b)
    elif eh_intersecao_valida(goban, str_para_intersecao(jogada)):
        if not eh_jogada_legal(goban, str_para_intersecao(jogada), pedra, goban_b):
            return turno_jogador(goban, pedra, goban_b)
        else:
            goban_b = goban
            goban = coloca_pedra(goban, str_para_intersecao(jogada), pedra)
            return True
        
def go(tamanho, intersecoes_brancas, intersecoes_pretas):
    if tamanho not in (9,13,19) or not isinstance(intersecoes_brancas, tuple) or not \
    isinstance(intersecoes_pretas, tuple):
        raise ValueError("go: argumentos invalidos")
    if len(intersecoes_brancas) == 0:
        for intersecao in intersecoes_brancas:
            if not eh_intersecao_valida(cria_goban_vazio(tamanho), intersecao):
                raise ValueError("go: argumentos invalidos")
    if len(intersecoes_pretas) == 0:
        for intersecao in intersecoes_pretas:
            if not eh_intersecao_valida(cria_goban_vazio(tamanho), intersecao):
                raise ValueError("go: argumentos invalidos")
    goban = cria_goban(tamanho, intersecoes_brancas, intersecoes_pretas)
    goban_b = cria_goban_vazio(tamanho)

    def _print():
        print(f"Branco (O) tem {calcula_pontos(goban)[0]} pontos\nPreto (X) tem {calcula_pontos(goban)[1]} pontos")
        print(goban_para_str(goban))

    _print()
    a = turno_jogador(goban, cria_pedra_preta(), goban_b)
    if a == True:
        for chave, valor in goban.items():
            if valor == cria_pedra_preta() and str_para_intersecao(chave) not in intersecoes_pretas:
                intersecoes_pretas += (str_para_intersecao(chave), )
        _print()
    
    if a == False:
        b = turno_jogador(goban, cria_pedra_branca(), goban_b)
        if b == False:
            return calcula_pontos(goban)[0] > calcula_pontos(goban[1])
        for chave, valor in goban.items():
            if valor == cria_pedra_branca() and str_para_intersecao(chave) not in intersecoes_brancas:
                intersecoes_brancas += (str_para_intersecao(chave), )
        _print()
        return go(tamanho, intersecoes_brancas, intersecoes_pretas)
    else:
        b = turno_jogador(goban, cria_pedra_branca(), goban_b)
        if b == True:
            for chave, valor in goban.items():
                if valor == cria_pedra_branca() and str_para_intersecao(chave) not in intersecoes_brancas:
                    intersecoes_brancas += (str_para_intersecao(chave), )
        return go(tamanho, intersecoes_brancas, intersecoes_pretas)

go(9, (), ())
