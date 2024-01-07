# Importação das bibliotecas
import cv2
import numpy as np
# from matplotlib import pyplot as plt

# Caminho da imagem a ser processada
imagem = 'imgs\imagem_processamento.png'

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



# Salvar a imagem gray em um arquivo
cv2.imwrite('image_gray.jpg', gray)

# Salvar a imagem binarizada em um arquivo
cv2.imwrite('image_binarizada.jpg', binary_image)

# Salvar a imagem blurred em um arquivo
cv2.imwrite('image_blurred.jpg', blurred)

# Aplicar filtro de realce (sharpening)
cv2.imwrite('image_sharpened.jpg', sharpened)


# # Exibir a imagem binarizada
# cv2.imshow('Imagem Binarizada', binary_image)

# # Aguardar uma tecla ser pressionada (0 indica espera indefinida)
# cv2.waitKey(0)

# # Fechar todas as janelas abertas
# cv2.destroyAllWindows()

