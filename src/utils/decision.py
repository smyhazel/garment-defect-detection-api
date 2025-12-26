def decide(score, threshold):
    return{
            "defect_detected" : bool(score > threshold)
    }