# 🏥 Smart Health Monitoring System Using Machine Learning, IoT & Django

A Smart Health Monitoring System that integrates **IoT**, **Machine Learning**, and **Django** to monitor vital health parameters such as **Heart Rate (BPM)**, **Blood Oxygen Saturation (SpO₂)**, and **Body Temperature** in real time.

The system collects health data using sensors connected to an **ESP32** microcontroller, uploads the readings to **ThingSpeak Cloud**, and displays them through a **Django Web Application**. Machine Learning is used to analyze patient health data and identify abnormal health conditions.

---

## 📌 Features

- ❤️ Real-time Heart Rate Monitoring
- 🩸 Blood Oxygen (SpO₂) Monitoring
- 🌡 Body Temperature Monitoring
- ☁ IoT Cloud Integration using ThingSpeak
- 📊 Django Dashboard for Data Visualization
- 🤖 Machine Learning Based Health Analysis
- 📟 LCD Display for Live Sensor Readings
- 📈 Real-time Health Data Monitoring

---

# 📷 Project Demo

> Add your project images here.

| Hardware Setup | Django Dashboard |
|---------------|------------------|

![Uploading image.png…]()

---

# 🏗 System Architecture

```
MAX30102 + MLX90614 Sensors
            │
            ▼
         ESP32
            │
        Wi-Fi Module
            │
            ▼
     ThingSpeak Cloud
            │
            ▼
    Django Web Application
            │
            ▼
 Machine Learning Prediction
            │
            ▼
   Health Status Monitoring
```

---

# ⚙ Hardware Components

- ESP32 Development Board
- MAX30102 Heart Rate & SpO₂ Sensor
- MLX90614 Temperature Sensor
- 16×2 LCD Display
- Jumper Wires
- USB Cable

---

# 💻 Software & Technologies

## Languages

- Python
- C++ (Arduino)

## Framework

- Django

## IoT Platform

- ThingSpeak

## Machine Learning

- Scikit-learn
- Pandas
- NumPy

## Database

- SQLite

## Tools

- Arduino IDE
- VS Code
- Git
- GitHub

---

# 🚀 Working

### Step 1

MAX30102 sensor measures

- Heart Rate
- Blood Oxygen (SpO₂)

### Step 2

MLX90614 measures

- Body Temperature

### Step 3

ESP32 collects all sensor readings.

### Step 4

Sensor data is transmitted to ThingSpeak Cloud through Wi-Fi.

### Step 5

Django retrieves and displays the data.

### Step 6

Machine Learning analyzes patient health data.

### Step 7

The dashboard displays the patient's health status.

---

# 📂 Project Structure

```
Smart-Health-Monitoring-System/
│
├── django_app/
├── templates/
├── static/
├── media/
├── ml_model/
├── Arduino_Code/
├── requirements.txt
├── manage.py
└── README.md
```

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/Apurupa126/Smart-Health-Surveillance-System-Using-Machine-Learning-IoT
```

## Navigate

```bash
cd Smart-Health-Monitoring-System
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Apply Migrations

```bash
python manage.py migrate
```

## Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# 📊 Machine Learning Workflow

- Data Collection
- Data Cleaning
- Feature Extraction
- Model Training
- Prediction
- Result Analysis

---

# 📈 ThingSpeak Integration

- Real-time Sensor Data Upload
- Cloud Storage
- Graph Visualization
- Remote Monitoring

---

# 🎯 Applications

- Smart Healthcare
- Hospitals
- Home Patient Monitoring
- Elderly Care
- Remote Health Monitoring
- Medical Research

---

# ✨ Future Enhancements

- Mobile Application
- Email & SMS Alerts
- AI-Based Disease Prediction
- Doctor Dashboard
- Multi-Patient Monitoring
- Health Report Generation
- Cloud Database Integration

---

# 📸 Output

### LCD Output

- Temperature
- Heart Rate
- SpO₂

### Django Dashboard

- Live Sensor Readings
- Historical Data
- Health Status
- Prediction Results

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| ESP32 | Microcontroller |
| MAX30102 | Heart Rate & SpO₂ |
| MLX90614 | Temperature Sensor |
| ThingSpeak | IoT Cloud |
| Django | Web Application |
| Python | Backend |
| Machine Learning | Health Prediction |
| SQLite | Database |

---

# 👩‍💻 Developer

**Apurupa Karna**

B.Tech – Artificial Intelligence and Machine Learning

Vignan's Nirula Institute of Technology and Science for Women (VNITSW), Guntur

---

# 📜 License

This project is developed for educational and academic purposes.

---

# ⭐ Support

If you found this project useful, don't forget to ⭐ star the repository.
