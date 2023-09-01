# import modules
import matplotlib.pyplot as plt

# Plotting graphs in python

# very basic plot
# x = [1, 3, 5, 10]  # this is what we are plotting
# plt.plot(x)
# plt.show()

# plotting x and y against each other
# y = [7, 12, 21, 22]
# plt.plot(x, y)
# plt.show()


# new plot

# line 1 - points
x = [3, 9, 14]
y = [2, 7, 30]
# plotting x and y
plt.plot(x, y, c='red', linewidth=2, label='line 1')

# line 2 - points
x2 = [1, 15, 18]
y2 = [0, 3, 12]

# plotting x2 and y2
plt.plot(x2, y2, c='green', linewidth=2, label='line 2', linestyle='dashed',
         marker='o', markerfacecolor='orange')  # marker can also be 's' = make marker's squared

# label the axes and give the plot a title
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('two lines')

# limits of the axes
plt.ylim(1, 10)
plt.xlim(0, 30)

# show the legend on the plot
plt.legend()
plt.show()