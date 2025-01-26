import numpy as np
import matplotlib.pyplot as plt

# numpy.arange([start, ]stop, [step, ]
t = np.arange(0., 20., 0.2)

#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

circle1 = plt.Circle((0, 0), 0.2, color='r')
fig, ax = plt.subplots()
ax.add_patch(circle1)
ax.plot(t, t**2)
#ax.plot(
#    t, t**2, "b-",
#    [1,20], [2,200], "r--")

#plt.plot([1,1], [3,3])
#plt.plot([0,3], [3,3])

#[<matplotlib.lines.Line2D object at 0x7fe822d67a20>]
plt.show()
