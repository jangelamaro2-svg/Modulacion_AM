import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq

# Tiempo
fs = 10000
t = np.arange(0, 1, 1/fs)

# Señal de mensaje
fm = 5
mensaje = np.sin(2*np.pi*fm*t)

# Señal portadora
fc = 100
portadora = np.cos(2*np.pi*fc*t)

# Modulación AM
modulada = (1 + mensaje) * portadora

# Ruido
ruido = 0.3 * np.random.randn(len(t))
modulada_ruido = modulada + ruido

# Atenuación
atenuacion = 0.5 * modulada

# FFT
frecuencias = fftfreq(len(t), 1/fs)
fft_modulada = np.abs(fft(modulada))

# Guardar graficas
plt.figure()
plt.plot(t, mensaje)
plt.title("Señal de mensaje")
plt.savefig("mensaje.png")

plt.figure()
plt.plot(t, portadora)
plt.title("Señal portadora")
plt.savefig("portadora.png")

plt.figure()
plt.plot(t, modulada)
plt.title("Señal modulada AM")
plt.savefig("modulada.png")

plt.figure()
plt.plot(frecuencias, fft_modulada)
plt.title("Dominio de la frecuencia")
plt.savefig("frecuencia.png")

plt.figure()
plt.plot(t, modulada_ruido)
plt.title("Señal modulada con ruido")
plt.savefig("ruido.png")

plt.figure()
plt.plot(t, atenuacion)
plt.title("Señal modulada con atenuación")
plt.savefig("atenuacion.png")

plt.show()