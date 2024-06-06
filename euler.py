def euler_propagation(dt, max_number_of_steps: int = 5000000):
    print('Euler')

    g = -9.8

    x = [0]
    y = [0]

    vx = 100   # it does not change, so we don't need to recalculate it
    vy = [100]

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