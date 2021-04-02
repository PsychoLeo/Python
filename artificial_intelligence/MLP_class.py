import numpy as np

class MLP:  # multi layer perception

    def __init__(self, num_inputs, num_hidden_layers, num_outputs):
        self.num_inputs = num_inputs
        self.num_hidden_layers = num_hidden_layers
        self.num_outputs = num_outputs
