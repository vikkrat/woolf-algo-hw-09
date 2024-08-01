import time
from tabulate import tabulate
from termcolor import colored
from greedy_algorithm import find_coins_greedy
from dynamic_programming import find_min_coins

def main():
    coins = [50, 25, 10, 5, 2, 1]
    test_amounts = [10, 50, 100, 150, 200, 250, 300, 350, 400, 450]
    results = []

    for amount in test_amounts:
        start_greedy = time.perf_counter()
        result_greedy = find_coins_greedy(amount, coins)
        time_greedy = time.perf_counter() - start_greedy

        start_dp = time.perf_counter()
        result_dp = find_min_coins(amount, coins)
        time_dp = time.perf_counter() - start_dp

        results.append([amount, result_greedy, time_greedy, result_dp, time_dp])

    headers = ["Amount", "Greedy Result", "Greedy Time (s)", "DP Result", "DP Time (s)"]
    table = tabulate(results, headers, tablefmt="fancy_grid")
    print(colored(table, 'cyan'))

if __name__ == "__main__":
    main()
