#   layoutpy by lujs.dev | MIT
#   Gerador de interfaces baseadas em texto

# configurações da interface
_width = 60
_heigth = 25
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

rows = len(_arrglobal)
cols = len(_arrglobal[0]) if rows else 0

# ----------------------------------------
def limit(x, y, v):
    """Calcula os limites."""
    if 0 <= x < rows and 0 <= y < cols:
        _arrglobal[x][y] = v

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
    for c in range(x, x + w + 1):
        limit(y, c, 2)
        limit(y + h, c, 2)
  
      # bordas verticais (laterais)
    for r in range(y + 1, y + h):
        limit(r, x, 1)
        limit(r, x + w, 1)

def text(x,y, t):
    """Desenha um texto"""
    x, y, t, lenTex = int(x), int(y), str(t), len(t)
    for a in range(lenTex):
        _arrglobal[y][x+a-lenTex] = t[a]

def line(x1,y1,x2,y2):
    """Desenha uma uma linha, (x1, y1) ponto de início, (x2, y2) ponto final."""
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    for i in range(y1, y2):
        t = i / (rows - 1)          # 0 -> 1
        x = round(x1 + (x2 + x1) * t) # interpolação linear
        limit(i,x, 4)

# Exemplo
# X Y W H
rect(0, 0, 2, 59)
text(23,1, "Iniciar")
text(32,1, "Projetos")
text(42,1, "Contatos")
text(52,1, "Sobre")

rect(2, centerY-5, 10, 55)
text(centerX+3,centerY, "lujs.dev")

line(3, 3, 40, 7)
line(30, 3, 40, 7)

# Renderizar
render()