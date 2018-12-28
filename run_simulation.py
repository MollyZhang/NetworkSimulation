import argparse


def main():
    args = parse_args()
    node_states, send_probs = initialize_network(args.num_nodes)
    for slot in range(args.time_steps):
        print(".", end="")



def initialize_network(num_nodes):
    """
    return: states and probabilities of sending packets for each node
    """
    node_states = None
    send_probs = {i:1/num_nodes for i in range(num_nodes)}
    return node_states, send_probs






def parse_args():
    parser = argparse.ArgumentParser(description="network simulation")
    parser.add_argument("-N", "--num_nodes", type=int, default=5, 
                        help="number of nodes in the network")
    parser.add_argument("-T", "--time_steps", type=int, default=100, 
                        help="number of steps (time slots) to run the simulation")
    args = parser.parse_args()
    return args






if __name__ == "__main__":
    main()
