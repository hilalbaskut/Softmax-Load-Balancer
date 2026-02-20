import random
import math

class Server:
    """
    Represents a server with a dynamic response time that changes over time.
    """
    def __init__(self, base_latency):
        self.base_latency = base_latency  # Base latency of the server
        self.current_latency = base_latency  # Current latency (changes over time)

    def get_latency(self):
        """
        Simulate non-stationary latency by adding random noise to the base latency.
        """
        noise = random.uniform(-0.5, 0.5)  # Random noise between -0.5 and 0.5
        drift = random.uniform(-0.1, 0.1)  # Small drift to simulate non-stationary behavior
        self.current_latency += drift
        return max(0.1, self.current_latency + noise)  # Ensure latency is always positive

class SoftmaxLoadBalancer:
    """
    Implements a load balancer using the Softmax Action Selection algorithm.
    """
    def __init__(self, servers, temperature):
        self.servers = servers  # List of Server objects
        self.temperature = temperature  # Temperature parameter for Softmax

    def select_server(self):
        """
        Select a server based on the Softmax probability distribution.
        """
        latencies = [server.get_latency() for server in self.servers]
        max_latency = max(latencies)  # For numerical stability
        exp_values = [math.exp(-(latency - max_latency) / self.temperature) for latency in latencies]
        total = sum(exp_values)
        probabilities = [value / total for value in exp_values]

        # Select a server based on the computed probabilities
        choice = random.choices(range(len(self.servers)), weights=probabilities, k=1)[0]
        return self.servers[choice]

def round_robin(servers, request_count):
    """
    Simulate Round-Robin load balancing.
    """
    total_latency = 0
    server_count = len(servers)
    for i in range(request_count):
        server = servers[i % server_count]  # Select server in a round-robin fashion
        total_latency += server.get_latency()
    return total_latency

def softmax_simulation(servers, request_count, temperature):
    """
    Simulate Softmax load balancing.
    """
    load_balancer = SoftmaxLoadBalancer(servers, temperature)
    total_latency = 0
    for _ in range(request_count):
        server = load_balancer.select_server()
        total_latency += server.get_latency()
    return total_latency

def simulation():
    """
    Run a simulation to compare Round-Robin and Softmax load balancing.
    """
    # Create a cluster of servers with varying base latencies
    servers = [Server(base_latency=random.uniform(1, 10)) for _ in range(5)]

    # Number of requests to simulate
    request_count = 1000

    # Temperature parameter for Softmax
    temperature = 1.0

    # Simulate Round-Robin load balancing
    rr_latency = round_robin(servers, request_count)

    # Simulate Softmax load balancing
    softmax_latency = softmax_simulation(servers, request_count, temperature)

    # Print results
    print("Total Latency (Round-Robin):", rr_latency)
    print("Total Latency (Softmax):", softmax_latency)

# Run the simulation
if __name__ == "__main__":
    simulation()