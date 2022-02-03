import torch


def risk_loss(pred, target):
    weights = torch.Tensor([[0., 0.25, 0.5, 1.0],
                            [0.25, 0., 0.25, 0.5],
                            [0.5, 0.25, 0., 0.5],
                            [1.0, 0.5, 0.25, 0.],
                            ]).view(-1, 4)
    results = torch.zeros(pred.size(0))
    ind = 0

    for i,j in zip(pred, target):
        results[ind] = weights[i.int(),j.int()]
        ind +=1

    loss = torch.sum(results)/pred.size(0)
    #print("RISK LOSS{}".format(loss))
    #mult = torch.matmul(tensor1, tensor2)
    #print(mult)
    return loss

def risk_metrics(pred, target):
    weights = torch.Tensor([[0, 1, 1, 1],
                            [1, 0, 1, 1],
                            [1, 1, 0, 1],
                            [1, 1, 1, 0],
                            ]).view(-1, 4)
    risks = torch.tensor((1,2,3,4))
    c_metric = torch.zeros(4)
    ind = 0

    for i,j in zip(pred, target):
        diff = torch.abs(i-j)
        c_metric[diff]+=1

    print("counters {}". format(c_metric))
    #mult = torch.matmul(tensor1, tensor2)
    #print(mult)


if __name__=='__main__':
    tensor1 = torch.randint(0,3,(3,))
    tensor2 = torch.randint(0,4,(3,))
    print(tensor1,tensor2)
    risk_loss(tensor1,tensor2)
    risk_metrics(tensor1,tensor2)
