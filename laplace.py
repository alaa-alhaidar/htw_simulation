import numpy as np
import matplotlib.pyplot as plt

# Frequenzbereich
omega = np.linspace(0, np.pi, 500)

# H(e^jw) berechnen
numerator = 3 + 4*np.exp(-1j*omega) + 4*np.exp(-2j*omega) + 3*np.exp(-3j*omega)
denominator = 1 + 0.5*np.exp(-1j*omega)
H = numerator / denominator

# Betrag und Phase
magnitude = np.abs(H)
phase = np.angle(H)

# Plot
plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.plot(omega, magnitude, color='blue')
plt.title("Betrags- und Phasengang von H(e^{jω})")
plt.ylabel("|H(e^{jω})|")
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(omega, np.degrees(phase), color='red')
plt.ylabel("∠H(e^{jω}) [°]")
plt.xlabel("ω [rad]")
plt.grid(True)

plt.tight_layout()
path = "/Users/alaa/Documents/code/modulation/"
plt.savefig(path)
plt.close()

path
