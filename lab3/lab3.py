import itertools
from math import sqrt


class Warehouse:
    def __init__(self, total_units, monthly_storage_cost, batch_production_cost, planning_period_days):
        self.total_units = total_units
        self.monthly_storage_cost = monthly_storage_cost
        self.batch_production_cost = batch_production_cost
        self.planning_period_days = planning_period_days

    @property
    def daily_norm(self):
        return self.total_units / self.planning_period_days

    @property
    def daily_storage_cost(self):
        return self.monthly_storage_cost * 12 / 365

    def initial_batch_size(self):
        return sqrt(2 * self.daily_norm * self.batch_production_cost / self.daily_storage_cost)

    def batch_size(self, n):
        return self.daily_norm * self.total_units / n

    def mean_cost(self, q):
        return (self.daily_norm * self.batch_production_cost / q) + (self.daily_storage_cost * q / 2)

    def optimize(self):
        initial_batch_size = self.initial_batch_size()

        optimal_batch_size = initial_batch_size
        for n in itertools.count(1):
            batch_size_upper = self.batch_size(n)
            batch_size_lower = self.batch_size(n + 1)

            if batch_size_lower <= initial_batch_size < batch_size_upper:
                lower_mean_cost = self.mean_cost(batch_size_lower)
                upper_mean_cost = self.mean_cost(batch_size_upper)
                optimal_batch_size = batch_size_lower if lower_mean_cost < upper_mean_cost else batch_size_upper
                break

        optimal_batch_interval = self.planning_period_days / (self.total_units / optimal_batch_size)
        return optimal_batch_size, optimal_batch_interval


def main():
    warehouse = Warehouse(
        total_units=24000,
        monthly_storage_cost=0.1,
        batch_production_cost=350,
        planning_period_days=365,
    )
    optimal_batch_size, optimal_batch_interval = warehouse.optimize()
    print(f'Optimal batch size: {optimal_batch_size}')
    print(f'Optimal batch interval: {optimal_batch_interval}')


if __name__ == '__main__':
    main()
