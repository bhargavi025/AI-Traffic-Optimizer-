from ultralytics import YOLO


def main():
    """
    model = YOLO("C:\\Users\\Bhargavi\\Documents\\yolov8m.pt")

    results = model.train(data="C:\\Users\\Bhargavi\\Documents\\data.yaml", epochs=50,batch=16,conf=0.2,workers=0,save=True)
    """
    model1 = YOLO("D:\\YOLO\\runs\\detect\\train5\\weights\\best.pt")
    
    result = model1.predict(source="D:\\ambulance2.jpg",conf=0.5,iou=0.4,classes=[0,1],save=True) 
    
if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # For safety on Windows
    main()









