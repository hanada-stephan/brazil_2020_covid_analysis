import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf


def barplot(dataset, x, y, xlabel, ylabel, title):
    """Print matplotlib barplot
    
    Args:
        dataset (pandas.DataFrame, numpy.ndarray, mapping, or sequence): dataset containing all the info
        x (vector or key in the dataset): dataset column for x-axis
        y (vector or key in the dataset): dataset column for y-axis
        xlabel (str): label for x-axis
        ylabel (str): label for y-axis
        title (str): graph title
        
    Returns:
        Figure containing the plot
    """
    
    plt.figure(figsize = (20,8))
    fig = plt.bar(dataset[x], dataset[y])
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel(ylabel, fontsize=15, rotation = 90)
    plt.title(title, loc='center', fontsize=20)


def lineplot(dataset, x, y, hue, xlabel, ylabel, title, semilog=None):
    """Print seaborn line plot
    
    Args:
        dataset (pandas.DataFrame, numpy.ndarray, mapping, or sequence): dataset containing all the info
        x (vector or key in the dataset): dataset column for x axis
        y (vector or key in the dataset): dataset column for y axis
        hue - Optional (vector or key in the dataset): variable to generate different line colors
        xlabel (str): a label for x-axis
        ylabel (str): label for the y-axis
        title (str): graph title
        semilog - Optional(str): "x" or "y" - set semilog axis for x and/or y. 
        
    Returns:
        Axis containing the plot
    """
    ax = sns.lineplot(x=x, y=y, hue=hue, data=dataset)
    ax.figure.set_size_inches(18,9)
    ax.set_xlabel(xlabel, fontsize=15)
    ax.set_ylabel(ylabel, fontsize=15, rotation = 90)
    ax.set_title(title, loc='center', fontsize=20)
    if semilog == "x":
        ax.set_xscale("log")
    elif semilog == "y":
        ax.set_yscale("log")
        
    

def plotACF(y1,y2,y3):
    """Plot 3 graphs for original, first differencing and second differencing
    
    Args:
        y1, y2, y3 (pd.series, np.array): Series of data 
        
    Returns:
        Figure containing the plots
    """
    
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(311)
    fig = plot_acf(y1,ax=ax1,title='Original')
    ax2 = fig.add_subplot(312)
    fig = plot_acf(y2,ax=ax2,title='First differencing')
    ax3 = fig.add_subplot(313)
    fig = plot_acf(y3,ax=ax3,title='Second differencing')
    

def plotting(y1, y2, y3, color1, color2, color3, label1, label2, label3, state = None):
    """Plot 3 graphs at once
    
    Args:
        y1, y2, y3 (pd.series, np.array): Series of data 
        color1, color2, color3 (str): Color to be used in the line plot
        label1, label2, label3 (str): Label to be used in the line plot
        state (str): Brazilian state
        
    Returns:
        Figure containing the plot
    """
    
    plt.figure(figsize=(20,7))
    plt.plot(y1,color=color1,label=label1)
    plt.plot(y2,color=color2,label=label2)
    plt.plot(y3,color=color3,label=label3)
    if state:
        plt.title(f"Seasonal decomposition for {state}", fontsize=20)
    plt.legend(fontsize=18)
    