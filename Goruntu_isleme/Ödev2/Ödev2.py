import cv2
import numpy as np

def find_red_objects(frame):
    # Görüntüyü HSV formatına dönüştürme
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığı (HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    # HSV görüntüsünden kırmızı renk aralığındaki nesneleri belirleme
    red_mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
    red_mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    # Görüntüdeki kırmızı nesneleri belirleme
    red_objects = cv2.bitwise_and(frame, frame, mask=red_mask)

    return red_objects

def main():
    # Kamera başlatma
    cap = cv2.VideoCapture(0)

    while True:
        # Kameradan bir çerçeve alınması
        ret, frame = cap.read()

        if not ret:
            print("Kamera görüntüsü alınamıyor.")
            break

        # Kırmızı nesneleri tespit etme
        red_objects = find_red_objects(frame)

        # Görüntüyü ekrana gösterme
        cv2.imshow('Original Frame', frame)
        cv2.imshow("Red Objects", red_objects)

        # 'q' tuşuna basıldığında döngüyü sonlandırma
        if cv2.waitKey(30) & 0xFF == ord('f'):
            break

    # Kamerayı serbest bırakma ve pencereyi kapatma
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
