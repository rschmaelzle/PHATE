import matplotlib.pyplot as plt

def plot_PHATE(data, out_file)
    plt.scatter(Y[:,0],Y[:,1],c=C,cmap='cubehelix')
    y_min = min(Y[:,1]) * 1.1
    y_max = max(Y[:,1]) * 1.1
    plt.ylim(y_min,y_max)
