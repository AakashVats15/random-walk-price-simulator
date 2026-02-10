from random_walk import RandomWalkSimulator
from plot_utils import plot_price_path, plot_return_distribution


def run_random_walk(
    steps=1000,
    S0=100.0,
    mu=0.0,
    sigma=0.01,
    seed=42
):
    model = RandomWalkSimulator(mu=mu, sigma=sigma, seed=seed)
    prices, returns = model.simulate_path(steps=steps, S0=S0)

    plot_price_path(prices, title="Random Walk Price Simulation")
    plot_return_distribution(returns, title="Random Walk Return Distribution")


if __name__ == "__main__":
    run_random_walk()