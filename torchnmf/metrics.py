import torch
import numpy as np


def KL_divergence(V, V_tilde):
    """
    The generalized Kullback-Leibler divergence.

    :param V: Target matrix.
    :param V_tilde: Reconstructed matrix.
    :return: Distance.
    """

    V2 = V.clone()
    id1, *id2 = (V2 == 0).nonzero().t()
    idx = [id1] + id2
    V2[idx] = 1

    return torch.sum(V2 * torch.log(V2 / V_tilde) - V + V_tilde)


def Euclidean(V, V_tilde):
    """
    Squared Frobenius norm.

    :param V: Target matrix.
    :param V_tilde: Reconstructed matrix.
    :return: Distance.
    """
    return (V - V_tilde).pow(2).sum() / 2


def IS_divergence(V, V_tilde):
    """
    The Itakura-Saito divergence:

    :param V: Target matrix.
    :param V_tilde: Reconstructed matrix.
    :return: Distance.
    """
    V2 = V.clone()
    id1, *id2 = (V2 == 0).nonzero().t()
    idx = [id1] + id2
    V2[idx] = 1
    return torch.sum(V2 / V_tilde - torch.log(V2 / V_tilde) - 1)
