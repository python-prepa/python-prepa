import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal

from dyna import forced_pendulum

omega = 2./3

dt = 2*np.pi / omega / 25

tf = 1000

acc_factors = np.linspace(1, 1.5, 100)
acc_factors = acc_factors[[2, 15, 34]]

all_theta_signals = []

for i, acc in enumerate(acc_factors):
    t, theta, theta_dot = forced_pendulum(tf, dt, np.pi/3, 0,
                        q=0.5, acc=acc, omega=omega)
    all_theta_signals.append(theta)

all_theta_signals = np.array(all_theta_signals)

mask = t > 400
theta_signals = all_theta_signals[:, mask]
theta_signals -= theta_signals.mean(axis=1)[:, np.newaxis]

theta_signals /= np.sqrt((theta_signals**2).mean(axis=1))[:, np.newaxis]

hann = signal.hanning(theta_signals.shape[1])
theta_signals *= hann

fft_sig = []
for sig in theta_signals:
    fft_sig.append(fftpack.fft(sig))

plt.figure(figsize=(6, 4))
plt.plot(t, all_theta_signals[0], lw=2, label=u'$A=1$')
plt.plot(t, all_theta_signals[1], lw=2, label=u'$A=1.08$')
plt.plot(t, all_theta_signals[2], lw=2, label=u'$A=1.17$')
plt.xlim(0, 550)
plt.ylim(-22, 22)
plt.legend(loc=3)
plt.xlabel(u'$t$', fontsize=24)
plt.ylabel(u'$\\theta$', fontsize=24)
plt.grid()
plt.gca().tick_params(axis='both', which='major', labelsize=18)

plt.tight_layout()

plt.axes([0.63, 0.65, 0.3, 0.28])
mask = np.logical_and(t > 400, t < 430)
plt.plot(t[mask], all_theta_signals[0][mask], lw=2, label=u'$A=1$')
plt.plot(t[mask], all_theta_signals[1][mask], lw=2, label=u'$A=1.08$')
plt.xticks([])
plt.yticks([])


plt.show()
