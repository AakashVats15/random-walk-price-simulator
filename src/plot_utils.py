import matplotlib.pyplot as plt
import seaborn as sns


def plot_price_path(prices, title="Random Walk Price Path"):
    plt.figure(figsize=(10, 4))
    plt.plot(prices, label="Price")
    plt.title(title)
    plt.xlabel("Time Step")
    plt.ylabel("Price")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_return_distribution(returns, title="Return Distribution"):
    plt.figure(figsize=(8, 4))
    sns.histplot(returns, kde=True, stat="density", bins=40, label="Returns")
    plt.title(title)
    plt.xlabel("Return")
    plt.ylabel("Density")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
