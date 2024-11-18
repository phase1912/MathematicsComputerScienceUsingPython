import cv2 as cv
import numpy as np
import urllib.request
#from google.colab.patches import cv2_imshow as cv_imshow
from cv2imshow.cv2imshow import cv2_imshow_single, cv2_imshow_multi

# Функція для завантаження зображення з URL
def read_image_by_url(url):
    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv.imdecode(arr, -1)
    return img

# URL до зображення
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/June_odd-eyed-cat.jpg/320px-June_odd-eyed-cat.jpg'  # Приклад зображення
img = read_image_by_url(url)

# Виведемо оригінальне зображення
print("Оригінальне зображення:")
cv2_imshow_single(img, "t")

# Розміри зображення
rows, cols = img.shape[:2]

# 1. Масштабування
M1 = np.array([[0.5, 0, 0], [0, 3, 0]], dtype=np.float32)  # Масштабування
scaled_img = cv.warpAffine(img, M1, (cols, rows * 3))  # Збільшення висоти
print("Масштабоване зображення:")
cv2_imshow_single(scaled_img, "t")

# 2. Відображення
M2 = np.array([[-1, 0, cols], [0, -1, rows]], dtype=np.float32)  # Відображення
reflected_img = cv.warpAffine(img, M2, (cols, rows))
print("Відображене зображення:")
cv2_imshow_single(reflected_img, "t")

# 3. Перенесення
M3 = np.array([[1, 0, -50], [0, 1, 30]], dtype=np.float32)  # Перенесення
translated_img = cv.warpAffine(img, M3, (cols, rows))
print("Перенесене зображення:")
cv2_imshow_single(translated_img, "t")

# 4. Обертання на 60°
theta_60 = np.radians(60)
M4 = np.array([
    [np.cos(theta_60), -np.sin(theta_60), 0],
    [np.sin(theta_60), np.cos(theta_60), 0]
], dtype=np.float32)
rotated_60_img = cv.warpAffine(img, M4, (cols, rows))
print("Обертання на 60°:")
cv2_imshow_single(rotated_60_img, "t")

# 5. Обертання на 30°
theta_30 = np.radians(30)
M5 = np.array([
    [np.cos(theta_30), -np.sin(theta_30), 0],
    [np.sin(theta_30), np.cos(theta_30), 0]
], dtype=np.float32)
rotated_30_img = cv.warpAffine(img, M5, (cols, rows))
print("Обертання на 30°:")
cv2_imshow_single(rotated_30_img, "t")

# 6. Об'єднане перетворення
M_combined = M5 @ M4 @ M2[:2, :2] @ M1[:2, :2]  # Об'єднання тільки матриць
combined_img = cv.warpAffine(img, M_combined, (cols, rows))
print("Об'єднане перетворення:")
cv2_imshow_single(combined_img, "t")