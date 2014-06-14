def ObservedPmf(pmf, speed, label=None):
    """takes in a pmf, an observer speed and an optional label
        returns a modified pmf of speeds from the perspective of
        a person traveling the input speed
    """
    new = pmf.Copy(label=label)
    for val, prob in new.Items():
        diff = abs(val - speed)
        new.Mult(val, diff)
    new.Normalize()
    return new