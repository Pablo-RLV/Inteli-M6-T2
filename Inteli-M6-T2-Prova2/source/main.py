import cv2
import argparse
# constrói o analisador de argumentos e analisa os argumentos
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", type=str,
	default="haarcascade.xml")
args = vars(ap.parse_args())
# Carrega o detector de faces
print("[INFO] loading face detector...")
detector = cv2.CascadeClassifier(args["cascade"])
# Abre o arquivo de video
input_video = cv2.VideoCapture('../assets/arsene.mp4')
# Checa se foi possivel abrir o arquivo
if not input_video.isOpened():
    print("Error opening video file")
    exit(1)
# Como foi possível abrir o video de entrada, vamos agora utilizar 
# essa captura para definir o tamanho do video de saida
width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Cria a estrutura do video de saida
# Com formato e local do arquivo de saida
# Codec utilizado
# FPS do video e
# Tamanho do video
output_video = cv2.VideoWriter( './output/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))
# Loop de leitura frame por frame
while True:
    # Le um frame do video e, guarda o resultado da leitura
    # Se nao houver mais frames disponiveis, ret sera falso
    ret, frame = input_video.read()
    # Se nao conseguiu ler o frame, para o laco
    if not ret:
        break
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# realiza a detecção de faces
    rects = detector.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=40, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    # varre as faces encontradas
    for (x, y, w, h) in rects:
		# desenha os retângulos nas faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 128, 0), 2)
    # Exibe o frame
    cv2.imshow('Rolandinho', frame)
    # Escreve o frame no output
    output_video.write(frame)
    # Se o usuario apertar q, encerra o playback
    # O valor utilizado no waiKey define o fps do playback
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
# Fecha tudo
output_video.release()
input_video.release()
cv2.destroyAllWindows()