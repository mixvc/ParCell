import random, math

def generateTime(tau):

    r = random.uniform(0.0,1.0)

    tau_bar = - (math.log(1-r)) * tau
    #tau_bar = - (math.log(tau * r)) * tau
    TAU = (0.8 * tau) + (0.2 * tau_bar)

    return TAU
