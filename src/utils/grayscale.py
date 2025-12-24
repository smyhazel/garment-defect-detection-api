def is_grayscale(img):
    if (len(img.shape) == 2) or (len(img.shape) == 3 and img.shape[2] == 1):
        return True
    else:
        return False