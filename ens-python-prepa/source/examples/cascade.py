import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal

from dyna import forced_pendulum

omega = 2./3

dt = 2*np.pi / omega / 25

tf = 1000

acc_factors = np.linspace(1, 1.5, 100)

fft_sig = []

t = np.arange(0, tf, dt)
mask = t > 400
hann = signal.hanning(mask.sum())

for i, acc in enumerate(acc_factors):
    print i
    t, theta, theta_dot = forced_pendulum(tf, dt, np.pi/3, 0,
                        q=0.5, acc=acc, omega=omega)
    theta = theta[mask]
    theta -= theta.mean()
    theta /= np.sqrt((theta**2).mean())
    theta *= hann
    fft_sig.append(fftpack.fft(theta))


fft_sig = np.array(fft_sig)

np.save('fft_sig.npy', fft_sig)
