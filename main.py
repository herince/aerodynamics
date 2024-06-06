from euler import euler_propagation
from leap_frog import leap_frog_propagation
from runge_kutta import runge_kutta_propagation


def main():
    # Calculate trajectory propagation using FDS for different time steps
    # Bigger time step should produce less precise results / more significant error in the calculation
    dt = 1
    for i in range(1, 6):
        euler_propagation(dt / 10**i)
        leap_frog_propagation(dt / 10**i)
        runge_kutta_propagation(dt / 10**i)


if __name__ == "__main__":
    main()
