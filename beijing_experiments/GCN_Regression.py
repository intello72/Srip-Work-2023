import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv


class GCN_RegressionModel(nn.Module):
    """
    A simple regression model using a GCN.

    Args:
        input_dim (int): The dimensionality of the input features.

    """

    def __init__(self, input_dim):
        super().__init__()
        self.conv1 = GCNConv(input_dim, 8)
        self.conv2 = GCNConv(8, 256)
        self.linear1 = nn.Linear(256, 256)
        self.linear2 = nn.Linear(256, 1)

    def forward(self, x, edge_index):
        """
        Forward pass.

        Args:
            x (torch.Tensor): The input features.
            edge_index (torch.Tensor): The edge indices.

        Returns:
            torch.Tensor: The output predictions.

        """
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.conv2(x, edge_index)
        x = self.linear1(x)
        x = F.relu(x)
        x = self.linear2(x)
        return x


class GCN_RegressionModel2(nn.Module):
    """
    A simple regression model using a GCN.

    Args:
        input_dim (int): The dimensionality of the input features.

    """

    def __init__(self, input_dim):
        super().__init__()
        self.conv1 = GCNConv(input_dim, 512)
#         self.conv2 = GCNConv(16, 10)
        self.linear1 = nn.Linear(512, 64)
        self.linear2 = nn.Linear(64, 1)

    def forward(self, x, edge_index):
        """
        Forward pass.

        Args:
            x (torch.Tensor): The input features.
            edge_index (torch.Tensor): The edge indices.

        Returns:
            torch.Tensor: The output predictions.

        """
        x = self.conv1(x, edge_index)
        x = F.relu(x)
#         x = self.conv2(x, edge_index)
        x = self.linear1(x)
        x = F.relu(x)
        x = self.linear2(x)
        return x


