import matplotlib.pyplot as plt

def create_chart():
    labels = ['Standard CBS', 'h-CBS']
    times = [0.0024, 0.0018] # Using the exact data from your terminal run
    colors = ['#e74c3c', '#2ecc71'] # Red for slow, Green for fast

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, times, color=colors, width=0.5)
    
    plt.ylabel('Execution Time (seconds)')
    plt.title('Experiment 4: Impact of h-CBS Heuristic on Execution Time')
    
    # Add exact numbers on top of the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.00005, f'{yval}s', ha='center', va='bottom')

    plt.savefig('heuristic_impact_chart.png')
    print("Saved heuristic_impact_chart.png!")

if __name__ == '__main__':
    create_chart()