def classify_risk(port):

    high_risk = [21, 23, 445, 3389]
    medium_risk = [80, 8080]

    if port in high_risk:
        return "High"
    elif port in medium_risk:
        return "Medium"
    else:
        return "Low"
