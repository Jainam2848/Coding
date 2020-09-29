import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Constants
G = 6.67e-11
M = 5.97e24
R = 6.371e6
#T = float(input("Enter the value of time: "))


def main():
    T = np.linspace(0.0, 1.0e5, 1000)
    h = np.empty(1000)
    for i in range(1000):
        h[i] = (G*M*T[i]**2/(4.0*np.pi**4))**(1.0/3) - R
    sns.set_style("dark")
    fig = plt.figure(figsize=(7, 7))
    ax1 = plt.axes()
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Height (m)')
    ax1.set_title('Height vs Time')
    ax1.plot(T, h)
    plt.show()
    ax1.legend()
    fig.savefig('SatelliteHeight.pdf')


if __name__ == "__main__":
    main()
