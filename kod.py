import pyautogui
import time
import os
import cv2

# Counter-Strike 1.6'yı açın "aklında bulunsun" \common\Counter-Strike\hl.exe
os.startfile("C:\Windows\System32\cmd.exe")

# 10 saniye bekleyin
time.sleep(10)

## kısayol gibi davrana bilir

# Kamerayı açın ve görüntüyü alın
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Görüntüyü kaydedin
cv2.imwrite("cs16.png", frame)

# Kamerayı kapatın
cap.release()
