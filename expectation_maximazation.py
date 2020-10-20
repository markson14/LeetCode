import numpy as np
from scipy import stats


def em(pirors, observations):
    counts = {'A': {'H': 0, 'T': 0}, 'B': {'H': 0, 'T': 0}}
    theta_a = pirors[0]
    theta_b = pirors[1]
    # E step
    for observation in observations:
        len_ob = len(observation)
        num_heads = observation.sum()
        num_tails = len_ob - num_heads
        contribution_a = stats.binom.pmf(num_heads, len_ob, theta_a)
        contribution_b = stats.binom.pmf(num_heads, len_ob, theta_b)
        weight_a = contribution_a / (contribution_a+contribution_b)
        weight_b = contribution_b / (contribution_a+contribution_b)
        # update flip
        counts['A']['H'] += weight_a * num_heads
        counts['A']['T'] += weight_a * num_tails
        counts['B']['H'] += weight_b * num_heads
        counts['B']['T'] += weight_b * num_tails

    # M step
    new_theta_a = counts['A']['H'] / (counts['A']['H'] + counts['A']['T'])
    new_theta_b = counts['B']['H'] / (counts['B']['H'] + counts['B']['T'])
    return [new_theta_a, new_theta_b]


def main(observations, prior, tol=1e-6, iters=1e4):
    iter = 0
    while iter < iters:
        new_piror = em(prior, observations)
        delta_change = np.abs(prior[0] - new_piror[0])
        if delta_change < tol:
            break
        else:
            prior = new_piror
            iter += 1
            print(new_piror)
    print(new_piror, iter)


if __name__ == "__main__":
    observations = np.array([[1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                             [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                             [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                             [1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                             [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]])
    main(observations, [0.6, 0.5])
