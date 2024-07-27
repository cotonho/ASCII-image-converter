from PIL import Image

def get_pixel_matrix(img, height):
    img.thumbnail((height, 200))
    pixels = list(img.getdata())
    return [pixels[i:i + img.width] for i in range(0, len(pixels), img.width)]
# retorna um array com todas as informações de cores de cada pixel



im = Image.open("ascii-pineapple.jpg")
print(f'X: {im.size[0]}; Y: {im.size[1]}')
# Printa o tamanho real da imagem

pixels = get_pixel_matrix(im, 1000)


# print(pixels)