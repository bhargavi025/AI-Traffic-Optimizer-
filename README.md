# AI-Traffic-Optimizer-
AI powered smart traffic control system that detects ambulances in real-time and make a green-corridor for emergency services and dynamically optimizes the trffic signals using lane-wise vehicle density and object tracking

#Problem Statement
Dynamic AI Traffic Flow Optimizer & Emergency Grid: Create an intelligent traffic management system that uses real-time computer vision to dynamically adjust signal timings based on live traffic density. The system must also enable an AI-powered green corridor feature to prioritize and clear routes for emergency vehicles such as ambulances and fire services.

#Project Overview
Traffic congestion is a major problem in Urban Areas. This project uses Computer Vision to identify different types of vehicles in each lane using ROI and counts the number of vehicles in each lane giving us the density of each lane. The traffic signal times are optimized based on the desity that is the total vehicles presnt in each lane. It also specifically detects the ambulance and emergency vehicles and creates a green corridor until it exists the frame of camera.  

#Features of the AI-Traffic-Optimizer
1. It can be used to optimize the traffic in real-time.
2. Counting vehicles in each ROI
3. Vehicle density counting
4. Traffic signal optimization
5. Ambulance and emergency vehicle Detection

#Technologies used
1. Python
2. YOLOv8
3. OpenCV
4. CUDA/GPU Acceleration
5. Spyder

#Real-Time Capabilities
1. Process live video or camera feed.
2. Count vehicles in real-time
3. Optimizes signal timings in real-time.
4. Suitable for smart-traffic signal systems
5. ROI's are self-adjustable according to the scenario.
