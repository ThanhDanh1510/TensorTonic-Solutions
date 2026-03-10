def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    x_left = max(box_a[0], box_b[0])
    y_top = max(box_a[1], box_b[1])
    x_right = min(box_a[2], box_b[2])
    y_bottom = min(box_a[3], box_b[3])

    Intersection = max(0, (x_right - x_left)) * max(0, (y_bottom - y_top))

    box1_Area = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    box2_Area = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
    Union = box1_Area + box2_Area - Intersection
    if Union == 0:
        return 0.0

    IoU = Intersection / Union
    return IoU
    pass