from ultralytics import YOLO
import cv2

def main():
    
    model = YOLO("C:\\Users\\Bhargavi\\Documents\\yolov8m.pt")
    
    frame = cv2.imread("D:\\traffic1.jpg")
    print(frame.shape)
    results = model.predict(frame, save=True, imgsz=544,conf=0.25)[0]
    
    lanes = {
    "North": (0, 0, 543, 117),
    "South": (0, 272, 544, 400),
    "East":  (279, 108, 544, 276),
    "West":  (0, 107, 279, 277)}
    
    lane_counts = {
    lane: {"light":0, "heavy":0, "two":0}
    for lane in lanes}
    
    for box in results.boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        
        if cls_name in ["car", "truck"]:
            vehicle_type = "light"
        elif cls_name == "bus":
            vehicle_type = "heavy"
        elif cls_name == "motorcycle":
            vehicle_type = "two"
        else:
            continue

        for lane, (lx1, ly1, lx2, ly2) in lanes.items():
            if lx1 < cx < lx2 and ly1 < cy < ly2:
                lane_counts[lane][vehicle_type] += 1
    
            
    print(lane_counts)
    
    
if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    main()
