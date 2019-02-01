# barrel-detection
## Discription
barrel_detector.py: Main function '\n'
hand_label.py: Handlabel color class using roipoly function. You can create as many classes as you like. Here I only choose three classes:'blue', 'not_blue' and 'not_barrel_blue'. Save them as .png '\n'
training.py: Create training samples with hand-labeled images. Extract all pixels and convert to hsv values. Stored as .txt
gaussian.py: Gaussian model.'\n'
color_seg.py: Color segmentation part. '\n'
find_box.py: Get bounding boxes of detected rectangles(barrels).'\n'
barrel.py: Show bounding boxes results'\n'
