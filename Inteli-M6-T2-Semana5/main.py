from ultralytics import YOLO
import cv2 as cv

video = cv.VideoCapture(0) # indica onde está o vídeo
modelo = YOLO('./best.pt') # importa o modelo treinado

if video.isOpened(): # verifica se a câmera está conectada
    pass
else:
    exit() # caso não esteja, fecha o programa

while True:
    ret, frame = video.read()
    result = modelo.predict(frame, conf=0.6) # aplica o modelo no frame
    if ret:
        frame_resultados = result[0].plot() # plota os resultados
        cv.imshow("Resultados", frame_resultados) # mostra os resultados na tela
        if cv.waitKey(1) == ord(' '): # caso aperte espaço, fecha o programa
            break

video.release()
cv.destroyAllWindows()