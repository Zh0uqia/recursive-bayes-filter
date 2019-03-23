import matplotlib.pyplot as plt
import numpy as np

def plot_bayes_filter(true_x, eps_list, mean_list):
    t = np.arange(0., 50., 1.)

    plt.hlines(true_x, 0, 50, colors = "b", label='true state value of x')
    plt.plot(t, eps_list, 'bo', ms=5, label='noisy observations')

    plt.plot(t, mean_list, 'r^', t, mean_list, 'k', color='r', label='mean value of posterior')
    plt.xlabel('times')
    plt.ylabel('mean of posterior')
    plt.title('Mean mu of Posterior Distribution')
    plt.show()

def plot_kalman_filter(x0, eps_list, mean_list):
    t = np.arange(0., 50., 1.)

    plt.plot(t, t+x0, 'k', color='b')
    plt.plot(t, eps_list, 'bo', ms=5, label='noisy observations')

    plt.plot(t, mean_list, 'r^', t, mean_list, 'k', color='r', label='mean value of posterior')
    plt.xlabel('times')
    plt.ylabel('mean of posterior')
    plt.title('Mean mu of Posterior Distribution')
    plt.show()
