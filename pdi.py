# Importação das bibliotecas
import cv2
import numpy as np
import hashlib
import os


# Caminho da imagem a ser processada
imagem = 'imgs\/folhas\/001.jpg'

img = cv2.imread(imagem)


# Carregar a imagem em tons de cinza
gray  = cv2.imread(imagem, cv2.IMREAD_GRAYSCALE)

# Aplicar filtro de desfoque (blur)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)


# Binarização global
_, binary_image = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Aplicar filtro de detecção de bordas (Canny)
edges = cv2.Canny(blurred, 50, 150)

# Aplicar filtro de realce (sharpening)
kernel_sharpening = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpened = cv2.filter2D(img, -1, kernel_sharpening)



# Função para calcular o hash MD5 de uma imagem
def calculate_hash(image):
    md5 = hashlib.md5()
    md5.update(image)
    return md5.hexdigest()

# Calcular os hashes
hash_binary = calculate_hash(binary_image.tobytes())
hash_gray = calculate_hash(gray.tobytes())
hash_blurred = calculate_hash(blurred.tobytes())
hash_sharpened = calculate_hash(sharpened.tobytes())

# Salvar as imagens com os nomes baseados nos hashes
cv2.imwrite(f'image_{hash_binary}.jpg', gray)
cv2.imwrite(f'image_{hash_gray}.jpg', gray)
cv2.imwrite(f'image_{hash_blurred}.jpg', blurred)
cv2.imwrite(f'image_{hash_sharpened}.jpg', sharpened)



# # Exibir a imagem binarizada
# cv2.imshow('Imagem Binarizada', binary_image)

# # Aguardar uma tecla ser pressionada (0 indica espera indefinida)
# cv2.waitKey(0)

# # Fechar todas as janelas abertas
# cv2.destroyAllWindows()

