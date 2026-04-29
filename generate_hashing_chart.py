import matplotlib.pyplot as plt

def create_hashing_chart():
    labels = ['Without Hashing', 'With Hashing']
    times = [0.0033, 0.0031] # Exact data from your terminal run
    colors = ['#f39c12', '#3498db'] # Orange and Blue for contrast

    plt.figure(figsize=(8, 5))
    bars = plt.bar(labels, times, color=colors, width=0.5)
    
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Experiment 5: Impact of State Hashing (10 Runs)')
    
    # Add exact numbers on top of the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.00005, f'{yval}s', ha='center', va='bottom')

    plt.savefig('hashing_impact_chart.png')
    print("Saved hashing_impact_chart.png!")

if __name__ == '__main__':
    create_hashing_chart()