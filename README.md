# barrel-detection
## Description
barrel_detector.py: Main function 

hand_label.py: Handlabel color class using roipoly function. You can create as many classes as you like. Here I only choose three classes:'blue', 'not_blue' and 'not_barrel_blue'. Save them as .png 

training.py: Create training samples with hand-labeled images. Extract all pixels and convert to hsv values. Stored as .txt

gaussian.py: Gaussian model

color_seg.py: Color segmentation part

find_box.py: Get bounding boxes of detected rectangles(barrels)

barrel.py: Show bounding boxes results
