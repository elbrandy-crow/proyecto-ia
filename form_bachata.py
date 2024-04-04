import tkinter as tk
from tkinter import filedialog
from tkinter import font
import librosa
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense, Input
import pygame
pygame.init()
# Función para extraer características del audio (en este caso, usaremos el tempo)
def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    tempo = librosa.beat.tempo(y=y, sr=sr)
    return tempo[0]

canciones = ["E/corazon sin cara.mp3","E/imitadora.mp3",
            "E/Propuesta Indecente CD 1 TRACK 1 (320).mp3","E/Romeo Santos - Sobredosis (feat. Ozuna).mp3"]
bpm = [127,126,123,128]
# Extraer características de cada canción
X = []
y = []
for cancion, bpm_valor in zip(canciones, bpm):
    tempo = extract_features(cancion)
    X.append(tempo)
    y.append(bpm_valor)

# Convertir a arrays numpy
X = np.array(X)
y = np.array(y)

# Dividir datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Construir modelo simple en TensorFlow
model = tf.keras.Sequential([
    Input(shape=(1,)),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(1)
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mse')

# Entrenar el modelo
model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=2)

root = tk.Tk()
root.title("What is the BPM")
root.configure(bg="black") 
root.geometry("500x600+350+20")
# Etiqueta de título
fuente_personalizada = font.Font(family="Helvetica", size=20, weight="bold")
titulo_label = tk.Label(root, text="What is the BPM", font=fuente_personalizada, fg="white", bg="black")
titulo_label.pack()

# Etiqueta para mostrar el resultado de la predicción
resultado_label = tk.Label(root, text="", font=("Helvetica", 16), fg="white", bg="black")
resultado_label.pack()

ruta_gif = "onda.gif"

gif_image = tk.PhotoImage(file=ruta_gif)

gif_label = tk.Label(root, image=gif_image, bg="black")
gif_label.pack()
# Evaluar el modelo
loss = model.evaluate(X_test, y_test, verbose=2)
print("Loss del modelo en conjunto de prueba:", loss)

def predecir_bpm():
    nueva_cancion = filedialog.askopenfilename()
    tempo_nueva_cancion = extract_features(nueva_cancion)
    predicted_bpm = model.predict(np.array([[tempo_nueva_cancion]]))
    resultado_label.config(text="BPM predicho para la nueva canción: {:.2f}".format(predicted_bpm[0][0]))
    pygame.mixer.music.load(nueva_cancion)
    pygame.mixer.music.play()
# Botón para seleccionar una nueva canción
boton_seleccionar = tk.Button(root, text="Seleccionar nueva canción",font=("Helvetica", 14), command=predecir_bpm)
boton_seleccionar.pack()


root.mainloop()