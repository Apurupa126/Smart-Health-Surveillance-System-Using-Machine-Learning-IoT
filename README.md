Smart Health Monitoring System Using Machine Learning, IoT, and Django
Overview

The Smart Health Monitoring System is an IoT-based healthcare solution designed to monitor a patient's vital signs in real time. The system collects heart rate (BPM), blood oxygen saturation (SpO₂), and body temperature using sensors connected to an ESP32 microcontroller. The collected data is transmitted to ThingSpeak Cloud through Wi-Fi for remote monitoring and visualization.

A Django web application provides an interactive dashboard for viewing patient health data, while Machine Learning is used to analyze sensor readings and identify normal or abnormal health conditions.

Features
Real-time Heart Rate (BPM) Monitoring
Blood Oxygen (SpO₂) Monitoring
Body Temperature Monitoring
IoT-Based Cloud Monitoring using ThingSpeak
Django Web Dashboard
Machine Learning Based Health Analysis
LCD Display for Live Sensor Readings
Real-Time Data Visualization
Technologies Used
Programming Languages
Python
C/C++ (Arduino)
Framework
Django
Machine Learning
Scikit-learn
Pandas
NumPy
IoT Platform
ThingSpeak
Hardware
ESP32
MAX30102 Sensor
MLX90614 Temperature Sensor
16×2 LCD Display
Database
SQLite (Default Django Database)
System Architecture
MAX30102 + MLX90614
          │
          ▼
        ESP32
          │
      Wi-Fi Network
          │
          ▼
    ThingSpeak Cloud
          │
          ▼
    Django Web Server
          │
          ▼
 Machine Learning Model
          │
          ▼
 Health Status Prediction
Working
The MAX30102 sensor measures:
Heart Rate
Blood Oxygen (SpO₂)
The MLX90614 sensor measures:
Body Temperature
ESP32 reads all sensor values.
ESP32 uploads data to ThingSpeak via Wi-Fi.
Django fetches and displays the latest readings.
Machine Learning analyzes the collected data.
The dashboard displays the patient's health information.
Project Modules
IoT Module
Sensor Data Collection
Wi-Fi Communication
ThingSpeak Integration
Django Module
User Interface
Dashboard
Patient Data Display
Database Management
Machine Learning Module
Data Preprocessing
Prediction Model
Health Condition Analysis
Hardware Components
Component	Purpose
ESP32	Main Controller
MAX30102	Heart Rate & SpO₂ Sensor
MLX90614	Temperature Sensor
LCD Display	Live Data Display
Jumper Wires	Connections
USB Cable	Power Supply
Software Requirements
Python 3.x
Django
Arduino IDE
ThingSpeak Account
VS Code
Git
Installation

Clone the repository:

git clone https://github.com/yourusername/Smart-Health-Monitoring-System.git

Navigate to the project:

cd Smart-Health-Monitoring-System

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start the Django server:

python manage.py runserver
Machine Learning Workflow
Data Collection
Data Cleaning
Feature Selection
Model Training
Prediction
Result Analysis
Future Enhancements
Email/SMS Health Alerts
Doctor Dashboard
Mobile Application
AI-Based Disease Prediction
Multi-Patient Monitoring
Health Report Generation (PDF)
Advantages
Real-Time Monitoring
Remote Access
Low Cost
Easy to Use
Accurate Sensor Readings
Cloud-Based Storage
Scalable Architecture
Applications
Hospitals
Home Healthcare
Rural Health Monitoring
Elderly Patient Care
Remote Patient Monitoring
Health Research
Project Outcome

This project demonstrates the integration of IoT, Machine Learning, and Django to create a smart healthcare monitoring solution. It enables real-time collection, cloud storage, web-based visualization, and intelligent analysis of patient health data.

Team

Apurupa Karna

B.Tech – Artificial Intelligence and Machine Learning

VNITSW, Guntur

License

This project is developed for educational and research purposes.
