#!/usr/bin/env python

max_number_of_steps = 5000000


def euler_next(dt):
    print('Euler')

    x = [0]
    y = [0]
    g = -9.8

    vx = 100   # it does not change, so we don't need to recalculate it
    vy = [100]
    # m = 10  # kg

    for i in range(0, max_number_of_steps):
        if y[i] < 0:
            break

        x.append(vx * dt + x[i])
        y.append(vy[i] * dt + y[i])
        vy.append(g * dt + vy[i])

    # Print the time delta
    print("dt =", dt)

    # Print the last five steps
    for i in range(len(x) - 3, len(x)):
        print(x[i], y[i], vy[i])

    # Print all steps
    # for i in range(0, len(x)):
    #     print(x[i], y[i], vy[i])

    # Print number of steps calculated until the object hits the ground
    print("steps = ", len(x))
    print()


def leap_frog_next(dt):
    print('Leap frog')

    g = -9.8

    x = [0]
    y = [0]

    vx = 100  # it does not change, so we don't need to recalculate it

    vy_start = 100                  # i = 0
    vy = [vy_start - g * dt / 2]    # i = -1/2

    for i in range(0, max_number_of_steps):
        if y[i] < 0:
            break

        vy.append(dt * g + vy[i])
        x.append(vx * dt + x[i])
        y.append(vy[i+1] * dt + y[i])

    # Print the last five steps
    for i in range(len(x) - 3, len(x)):
        print(x[i], y[i], vy[i])

    # Print all steps
    # for i in range(0, len(x)):
    #     print(x[i], y[i], vy[i])

    # Print number of steps calculated until the object hits the ground
    print("steps = ", len(x))
    print()


# def runge_kutta(dt):


def main():
    # Calculate trajectory propagation using FDS for different time steps
    # Bigger time step should produce less precise results / more significant error in the calculation
    dt = 1
    for i in range(1, 6):
        euler_next(dt / 10**i)
        leap_frog_next(dt / 10**i)


if __name__ == "__main__":
    main()
