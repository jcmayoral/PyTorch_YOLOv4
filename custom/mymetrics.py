import torch


def risk_metrics(pred, target):
    weights = torch.Tensor([[1, 1, 1, 1],
                            [1, 2, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 1, 7],
                            ]).view(-1, 4)
    print(weights)
    results = torch.zeros(pred.size(0))
    ind = 0

    for i,j in zip(pred, target):
        results[ind] = weights[i,j]
        ind +=1

    metric = torch.sum(results)
    print(metric)
    #mult = torch.matmul(tensor1, tensor2)
    #print(mult)

if __name__=='__main__':
    tensor1 = torch.arange(4)
    tensor2 = torch.arange(4)
    print(tensor1,tensor2)
    risk_metrics(tensor1,tensor2)
