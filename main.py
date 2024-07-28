from PIL import Image

def get_pixel_matrix(img):
    img.thumbnail((2000, 300))
    #é necessário alterar esses valores caso a imagem esteja com alguma proporção estranha
    #eu deixei 300 por conta de não caber muito bem no txt e 2000 por conta de nenhuma image chegar nessa largura quando limitada a 300 pixels
    print(img.size)
    pixels = list(img.getdata())
    return [pixels[i:i + img.width] for i in range(0, len(pixels), img.width)]
# retorna um array com todas as informações de cores de cada pixel


matriz_ascii = ('`^\\",:;Il!i~+_-?][}{1)(|\\\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$')
im = Image.open("ascii-pineapple.jpg")
# Imagem a ser convertida
img = []
brilho = []


print(f'X: {im.size[0]}; Y: {im.size[1]}')
# Printa o tamanho real da imagem

pixels = get_pixel_matrix(im)

for x in range(len(pixels)):
    brilho.append([])
    for y in range(len(pixels[x])):
        pixel = pixels[x][y]
        brilho[x].append((pixels[x][y][0] + pixels[x][y][1] + pixels[x][y][2]) /3)
# Transforma todos as informações de cores de cada pixel em uma média que será o brilho utilizado na imagem


for x in range(len(brilho)):
    img.append([])
    for y in range(len(brilho[x])):
        n = 1
        while (n * 12.75) < brilho[x][y]:
            n+= 1
        img[x].append(matriz_ascii[n-1])

for x in range(len(img)):
    print(*img[x])