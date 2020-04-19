import xml.etree.ElementTree as ET
import cv2

def read_context(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    list_with_all_boxes = []
    list_with_all_names = []

    for boxes in root.iter('object'):
        filename = root.find('filename').text

        xmin, ymin, xmax, ymax = None, None, None, None

        for box in boxes.findall('bndbox'):
            xmin = int(box.find('xmin').text)
            ymin = int(box.find('ymin').text)
            xmax = int(box.find('xmax').text)
            ymax = int(box.find('ymax').text)

        list_with_single_boxes = [xmin, ymin, xmax, ymax]
        list_with_all_boxes.append(list_with_single_boxes)

        list_with_all_names.append(boxes.find('name').text)

    return filename, list_with_all_boxes, list_with_all_names

def write_bounding_boxes(img, boxes: list, names: list):
    count = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    for box in boxes:
        cv2.rectangle(img, (box[0],box[1]), (box[2],box[3]), (0,255,0), 2)
        cv2.putText(img, names[count], (box[0],box[1]), font, 0.75, (0,255,0), 2)
        count += 1
    return img

img_name = str(input('Input name of a image file (file_name.jpg) : '))
img = cv2.imread(img_name)

xml_file_name = str(input('Input name of the xml file (file_name.xml) : '))

# img_name = 'C228 (17)_frame_152.jpg'
# img = cv2.imread('C228 (17)_frame_152.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# name, boxes, names = read_context('C228 (17)_frame_152.xml')
name, boxes, names = read_context(xml_file_name)
img = write_bounding_boxes(img, boxes, names)
# cv2.imwrite(img_name, img)

cv2.imshow('img', img)

while True:
    key = cv2.waitKey(1)
    if key == 27: #ESC key to break
        break

cv2.destroyAllWindows()