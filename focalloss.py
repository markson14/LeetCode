import torch
import torch.nn as nn
import torch.nn.functional as F


class FocalLoss(nn.Module):
    '''
    softmax = - [ylog(p) + (1-y)log(1-p)], y={0,1}
    Focal Loss = - [y*alpha*(1-p)**gamma * log(p) + (1-y)*(1-alpha)*p**gamma * log(1-p)], y={0,1}
    '''
    def __init__(self, gamma=0.25, alpha=2, size_average=True):
        '''
        gamma[defult]: 2       |   set [0] is CrossEntropy
        alpha[default]: 0.25   |   set [1] is CrossEntropy
        '''
        super(FocalLoss, self).__init__()
        # 难易样本学习的权重
        self.gamma = gamma
        # 调节正负样本的比例
        self.alpha = alpha
        if isinstance(alpha, (float, int, long)):
            self.alpha = torch.Tensor([alpha, 1-alpha])
        if isinstance(alpha, list):
            self.alpha = torch.Tensor(alpha)
        self.size_average = size_average

    def forward(self, input, target):
        if input.dim() > 2:
            # N,C,H,W => N,C,H*W
            input = input.view(input.size(0), input.size(1), -1)
            input = input.transpose(1, 2)    # N,C,H*W => N,H*W,C
            input = input.contiguous().view(-1, input.size(2))   # N,H*W,C => N*H*W,C
        target = target.view(-1, 1)

        logpt = F.log_softmax(input)
        logpt = logpt.gather(1, target)
        logpt = logpt.view(-1)
        pt = torch.Tensor(logpt.data.exp())

        if self.alpha is not None:
            if self.alpha.type() != input.data.type():
                self.alpha = self.alpha.type_as(input.data)
            at = self.alpha.gather(0, target.data.view(-1))
            logpt = logpt * torch.Tensor(at)

        loss = -1 * (1-pt)**self.gamma * logpt
        if self.size_average:
            return loss.mean()
        else:
            return loss.sum()
