import numpy as np
from scipy.integrate import odeint
import math

def simple_pendulum(theta_thetadot, t):
    theta, theta_dot = theta_thetadot
    return [theta_dot, - np.sin(theta)]

def forced_pendulum_equations(y, t, q, acc, omega):
    theta, theta_dot = y
    return [theta_dot, acc * np.sin(omega * t) - \
                       np.sin(theta) - q * theta_dot]

def forced_pendulum(t_end, t_space, theta_init, theta_dot_init=0, q=0.1,
                            acc=1, omega=1):
    """
    Integrate a trajectory for the forced pendulum.

    Parameters
    ----------

    t_end : float
        Final time of the trajectory (initial time is always 0).

    t_space : float
        Time_interval between two points of the trajectories

    theta_init : float
        Initial angular position

    theta_dot_init : float, optional
        Initial angular velocity (default 0)

    q : float, optional
        Damping (default 0.1)

    acc : float, optional
        Amplitude of the forcing (default 1)

    omega : float, optional
        Pulsation of forcing (default 1)

    Returns
    -------
    t: ndarray of floats
        array of times

    theta: ndarray of floats
        angular positions along the trajectory

    theta_dot: ndarray of floats
        angular velocities along the trajectory

    Notes
    -----
    This function integrates the equation
    .. math::

        \ddot{\\theta} + q \dot{\\theta} + \omega^2 \sin\\theta = A \sin
            \omega_D t

    Examples
    --------
    >>> t, theta, theta_dot =  forced_pendulum(100, 0.1, np.pi/3)
    >>> sol = forced_pendulum(100, 0.1, np.pi/3, theta_dot_init=1, acc=1.5)
    """

    t_range = np.arange(0, t_end, t_space)
    sol = odeint(forced_pendulum_equations, [theta_init, theta_dot_init],
                            t_range, args=(q, acc, omega))
    return np.vstack((t_range, sol.T))
