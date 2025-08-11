import matplotlib.pyplot as plt
import time

xdata = [0]
ydata = [0]

plt.ion()  # Turn on interactive mode
fig, axes = plt.subplots()
line, = axes.plot(xdata, ydata, 'r-')
axes.set_xlim(0, 100)
axes.set_ylim(0, 1)

for i in range(1, 100):
    xdata.append(i)
    ydata.append(i / 2)
    line.set_xdata(xdata)
    line.set_ydata(ydata)
    axes.set_xlim(0, i)  # Update x-axis limit dynamically
    axes.set_ylim(0, max(ydata) if ydata else 1)  # Update y-axis limit dynamically
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)

plt.ioff()  # Turn off interactive mode
plt.show()  # Show plot window
