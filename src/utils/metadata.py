from .grayscale import is_grayscale

def extract_image_metadata(img):
    h, w = img.shape[:2]
    channels = 1 if len(img.shape) == 2 else img.shape[2] 
    is_gray = is_grayscale(img)
    return {"width" : w,
            "height" : h,
            "channels" : channels,
            "is_grayscale": is_gray} 
