from ultralytics import YOLO
import cv2

# load model
model = YOLO("yolov8m.pt")

# read image
image = cv2.imread("D:\\traffic1.jpg")

# run detection
results = model(image)

car_count = 0
truck_count = 0
bike_count = 0
bus_count = 0

for cls in results[0].boxes.cls:
    cls = int(cls)

    if cls == 2:      # car
        car_count += 1
    elif cls == 7:    # truck
        truck_count += 1
    elif cls == 3:
        bike_count += 1
    elif cls == 5:
        bus_count +=1

total = car_count + truck_count + bike_count +bus_count

print("Cars:", car_count)
print("Trucks:", truck_count)
print("Bikes:", bike_count)
print("Total Vehicles:", total)

