import argparse
import numpy as np



def main():
    args = parse_args()
    network = Network(args.num_nodes)
    for i in range(args.time_steps):
        network.slot()
    print(network.get_bandwidth())


class Node(object):
    def __init__(self, init_prob):
        self.history = []
        self.x = init_prob

    def send(self):
        return np.random.choice([0, 1], p=[1-self.x, self.x])

    def add_to_history(self, status):
        self.history.append(status)



class Network(object):
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(1/n) for i in range(n)]
        self.history = []       
 
    def slot(self):
        send_status = [i.send() for i in self.nodes]
        self.decide_outcome(send_status)
            
    def decide_outcome(self, send_status):
        if sum(send_status) == 0:
            self.history.append("E")
            for node in self.nodes:
                node.add_to_history("E")
        elif sum(send_status) > 1:
            self.history.append("C")
            for node in self.nodes:
                node.add_to_history("C")
        elif sum(send_status) == 1:
            self.history.append("Y")
            for i, node in enumerate(self.nodes):
                if send_status[i] == 1:
                    node.add_to_history("Y")
                else:
                    node.add_to_history("O")
    
    def get_bandwidth(self):
        return self.history.count("Y")/len(self.history)




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
