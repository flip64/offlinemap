import matplotlib.pyplot as plt

x = [44, 44, 40, 110.2, 125.8, 125.8]
y = [0, 15.9, 75, 135.6, 32.4, 0]

x.append(x[0])
y.append(y[0])

plt.plot(x, y)
plt.grid(True)
plt.xlabel("P (MW)")
plt.ylabel("H (MWth)")
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.savefig("FR.png", format="png", dpi=500, bbox_inches="tight")
plt.show()
