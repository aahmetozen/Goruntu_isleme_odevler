import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('image.jpg', 0) # tek kanal gri görüntü

# Histogram için 256 elemanlı bir liste oluştur (8 BİT FOTOĞRAF)
histogram = [0] * 256

# Görüntünün histogramı hesapla
for row in image:
    for pixel_value in row:
        histogram[pixel_value] += 1

# Histogramı görselleştir
plt.bar(range(256), histogram, color='gray', alpha=0.7)
plt.title('Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
cv2.imshow(" ",image) # resmi gösterir
plt.show()

# GÖRÜNTÜNÜN HİSTOGRAMI

# Bu örnekte, her bir pikselin değerini alarak, histogram adlı 256 elemanlı bir liste içinde ilgili değerin sıklığını arttırıyoruz.
# Daha sonra, Matplotlib kütüphanesini kullanarak bu histogramı görselleştiriyoruz.