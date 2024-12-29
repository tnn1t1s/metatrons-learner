import torch
import torch.nn as nn

class MetatronNet(nn.Module):
    def __init__(self):
        super(MetatronNet, self).__init__()
        # Fully connected layers reflecting Metatron's Cube
        self.fc_input_to_inner = nn.Linear(5, 6)  # 5 input nodes to 6 inner hidden nodes
        self.fc_inner_to_center = nn.Linear(6, 1)  # 6 inner hidden nodes to 1 center node
        self.fc_inner_to_output = nn.Linear(6, 1)  # 6 inner hidden nodes to 1 output node
        self.fc_center_to_output = nn.Linear(1, 1)  # Center node to output node
        
        # Activation functions
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # Input to inner hidden nodes
        inner_hidden = self.relu(self.fc_input_to_inner(x))  # Shape: [batch_size, 6]
        
        # Inner hidden to center node
        center_node = self.relu(self.fc_inner_to_center(inner_hidden))  # Shape: [batch_size, 1]
        
        # Inner hidden to output node
        inner_to_output = self.fc_inner_to_output(inner_hidden)  # Shape: [batch_size, 1]
        
        # Combine center and inner-to-output paths
        combined_output = inner_to_output + self.fc_center_to_output(center_node)
        
        # Final activation for binary classification
        output = self.sigmoid(combined_output)
        return output

