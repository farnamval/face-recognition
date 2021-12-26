import cv2


def resize_image(original_image, max_width=1366, max_height=768, save_scaling=True):
    image = original_image

    if not save_scaling:
        resolution = (max_width, max_height)

        if image.shape[1] > max_width:
            interpolation = cv2.INTER_AREA
        else:
            interpolation = cv2.INTER_CUBIC

        image = cv2.resize(image, resolution, interpolation=interpolation)

        return image

    if image.shape[1] / max_width > image.shape[0] / max_height:
        scale = float(max_width) / image.shape[1]
        resolution = (max_width, int(image.shape[0] * scale))

        if image.shape[1] > max_width:
            interpolation = cv2.INTER_AREA
        else:
            interpolation = cv2.INTER_CUBIC

        image = cv2.resize(image, resolution, interpolation=interpolation)
    else:
        scale = float(max_height) / image.shape[0]
        resolution = (int(image.shape[1] * scale), max_height)

        if image.shape[0] > max_height:
            interpolation = cv2.INTER_AREA
        else:
            interpolation = cv2.INTER_CUBIC

        image = cv2.resize(image, resolution, interpolation=interpolation)

    return image
