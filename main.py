#   layoutpy by lujs.dev | MIT
#   Gerador de interfaces baseadas em texto

# configurações da interface
_width = 60
_heigth = 20
centerX = _width/2
centerY = _heigth/2

_chars = {
    0: ".",
    1: "│",
    2: "─",
    3: "─",
    4: "*",
}

# --------- Gerar array vazia ----------
# Python não consegue manipular valores que não existe em uma array, então criamos uma array 2D

_arrglobal = []
for i in range(_heigth): #
    if i < 1000: 
        _arrglobal.append([])

for _i in range(_heigth):
    for _ in range(_width):
        _arrglobal[_i].append(0)

# ----------------------------------------

# Renderizar
def render():
    """Exibe o conteúdo de um array 2D em formato de tabela."""
    row = ''
    for i in range(len(_arrglobal)):
        for j in range(len(_arrglobal[i])):
            if _arrglobal[i][j] in _chars:
                row += _chars[_arrglobal[i][j]]
            else:
                row += _arrglobal[i][j]
            #print(_arrglobal[i][j])
        print(row)
        row = ''

# Unir tabelas

def unirtabelas1(arr1, arr2):
    """Modifica os valores da tabela 1 com os valores da tabela 2."""
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr2[i][j] != 0:
                arr1[i][j] = arr2[i][j]
    return arr1  # Retorna a tabela modificada

def rect(x, y, h, w):
    """Desenha uma caixa"""
    x, y, h, w = int(x), int(y), int(h), int(w)
    for i in range(len(_arrglobal)):
        if i < len(_arrglobal):
            for a in range(w+1):
                if a < len(_arrglobal[i]) and y < len(_arrglobal):
                    if y < len(_arrglobal) and a+x < len(_arrglobal[i]):
                        _arrglobal[y][a+x] = 2
                    if y+h < len(_arrglobal) and a+x < len(_arrglobal[i]):
                        _arrglobal[y+h][a+x] = 3

            for b in range(h):
                if i > y and i < y+h:
                    if x < len(_arrglobal[i]):
                        _arrglobal[i][x] = 1
                    if x+w < len(_arrglobal[i]):
                        _arrglobal[i][x + w] = 1

def text(x,y, t):
    """Desenha um texto"""
    x, y, t, lenTex = int(x), int(y), str(t), len(t)
    for a in range(lenTex):
        _arrglobal[y][x+a-lenTex] = t[a]

# Exemplo
# X Y W H
rect(0, 0, 2, 59)
text(23,1, "Iniciar")
text(32,1, "Projetos")
text(42,1, "Contatos")
text(52,1, "Sobre")

rect(2, centerY-5, 10, 55)
text(centerX+3,centerY, "lujs.dev")

# Renderizar
render()