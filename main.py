from dp_algorithms import min_cost_with_stops

def main():
    print("\n--- Smart Travel Cost Optimizer ---")

    n = int(input("Enter number of cities: "))
    m = int(input("Enter number of flights: "))

    flights = []
    print("Enter flights (u v cost):")
    for _ in range(m):
        u, v, cost = map(int, input().split())
        flights.append((u, v, cost))

    src = int(input("Enter source city: "))
    dst = int(input("Enter destination city: "))
    K = int(input("Enter max stops: "))

    result = min_cost_with_stops(n, flights, src, dst, K)

    if result == -1:
        print("No route available within given stops.")
    else:
        print(f"Minimum travel cost: {result}")


if __name__ == "__main__":
    main()