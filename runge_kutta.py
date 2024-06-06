def runge_kutta_propagation(dt, max_number_of_steps: int = 5000000):
    print('Runge-Kutta')

    g = -9.8

    x = [0]
    y = [0]

    vx = 100  # it does not change, so we don't need to recalculate it
    vy = [100]

    for i in range(0, max_number_of_steps):
        if y[i] < 0:
            break

        kvy = g
        k1y = vy[i]
        k2y = vy[i] + (dt * kvy) / 2
        k3y = vy[i] + (dt * kvy) / 2
        k4y = vy[i] + dt * kvy

        x.append(x[i] + dt * vx)
        y.append(y[i] + dt * (k1y + 2 * k2y + 2 * k3y + k4y) / 6)
        vy.append(vy[i] + dt * g)

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
