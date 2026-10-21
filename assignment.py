import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.plot([1, 2, 3], [2, 4, 6], "r--")
ax.plot([1, 2, 3], [3, 2, 1], "g-")
ax.set_title("Example plot")
plt.show()

# 1. Does this code create one plotting panel (Axes object) or two?
# Explain briefly. A panel is a plotting area, not an individual x-axis or y-axis.
# Your answer: One plotting panel is created because the code uses plt.subplots(1, 1)
#  which creates a single Axes object. The two lines are drawn on the same panel.

# 2. How many data lines are drawn? What are the y-values of the red dashed line?
# Your answer:
# There are two data lines drawn.
# The y-values of the red dashed line are [2, 4, 6].