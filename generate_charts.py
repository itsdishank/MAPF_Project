import matplotlib.pyplot as plt

grids = ['5x5', '10x10', '20x20']
times = [0.00011, 0.00039, 0.00177]
lengths = [8, 18, 38]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Grid Size')
ax1.set_ylabel('Execution Time (seconds)', color=color)
ax1.plot(grids, times, marker='o', color=color, linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Path Length (steps)', color=color)  
ax2.plot(grids, lengths, marker='s', color=color, linestyle='dashed')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Baseline A* Performance Scaling')
fig.tight_layout()  
plt.savefig('scaling_chart.png')
print("Chart saved as scaling_chart.png!")