from project.datasets import Simple, Split, Xor

N = 100

def classify_simple(pt):
    "Classify based on x position"
    # x axis
    x = pt[0]

    if x < 0.5:
        return 1.0
    else:
        return 0.0


def classify_split(pt):
    # x axis
    x = pt[0]

    if x > 0.2 and x < 0.8:
        return 0.0
    else:
        return 1.0


def classify_xor(pt):
    # x axis and y axis
    x = pt[0]
    y = pt[1]

    if x < 0.5 and y < 0.5:
        return 0.0
    elif x <= 0.5 and y >= 0.5:
        return 1.0
    elif x >= 0.5 and y <= 0.5:
        return 1.0
    elif x > 0.5 and y > 0.5:
        return 0.0


Simple(N, vis=True).graph("Simple", model=classify_simple)
# Split(N, vis=True).graph("Split", model=classify_split)
# Xor(N, vis=True).graph("Xor", model=classify_xor)