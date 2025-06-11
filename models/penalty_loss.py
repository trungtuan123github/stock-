import torch
import torch.nn as nn

class PenalizedMSELoss(nn.Module):
    def __init__(self, shock_threshold=0.05, penalty_weight=5.0):
        super().__init__()
        self.shock_threshold = shock_threshold
        self.penalty_weight = penalty_weight
        self.mse = nn.MSELoss()

    def forward(self, pred, target):
        loss = self.mse(pred, target)
        shocks = torch.abs(pred[:, 1:] - pred[:, :-1])
        penalties = torch.where(
            shocks > self.shock_threshold,
            self.penalty_weight * shocks,
            torch.zeros_like(shocks)
        )
        return loss + penalties.mean()