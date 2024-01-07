# Importação das bibliotecas
import cv2

# Caminho da imagem a ser processada
imagem = 'imgs\imagem_processamento.png'

# Carregar a imagem em tons de cinza
img = cv2.imread(imagem, cv2.IMREAD_GRAYSCALE)

# Binarização global
_, binary_image = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Salvar a imagem binarizada em um arquivo
cv2.imwrite('image_binarizada.jpg', binary_image)

# Exibir a imagem binarizada
cv2.imshow('Imagem Binarizada', binary_image)

# Aguardar uma tecla ser pressionada (0 indica espera indefinida)
cv2.waitKey(0)

# Fechar todas as janelas abertas
cv2.destroyAllWindows()

