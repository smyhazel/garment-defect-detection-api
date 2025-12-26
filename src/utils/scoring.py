import cv2
import numpy as np

def compute_edge_score(gray_image):
    edge = cv2.Canny(gray_image,100,200)
    total_pixels = gray_image.size
    edge_pixels = np.sum(edge != 0)
    score = edge_pixels/total_pixels
    return float(score)
