import numpy as np


class RandomWalkSimulator:
    """
    Simple random walk on returns, converted into a price path.
    """

    def __init__(self, mu=0.0, sigma=0.01, seed=None):
        self.mu = mu
        self.sigma = sigma
        self.rng = np.random.default_rng(seed)

    def simulate_returns(self, steps=1000):
        """
        Generate i.i.d. normal returns.
        """
        returns = self.rng.normal(loc=self.mu, scale=self.sigma, size=steps)
        return returns

    def returns_to_prices(self, returns, S0=100.0):
        """
        Convert returns to prices using geometric compounding:
        S_t = S_0 * exp(cumsum(returns))
        """
        log_prices = np.log(S0) + np.cumsum(returns)
        prices = np.exp(log_prices)
        return prices

    def simulate_path(self, steps=1000, S0=100.0):
        """
        Full pipeline: simulate returns → convert to prices.
        """
        returns = self.simulate_returns(steps)
        prices = self.returns_to_prices(returns, S0)
        return prices, returns
