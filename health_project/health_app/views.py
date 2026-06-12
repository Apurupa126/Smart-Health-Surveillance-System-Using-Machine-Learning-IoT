from django.shortcuts import render

def health_check(request):
    result = None
    alerts = []
    input_values = {}

    # 🔹 Demo values (replace later with ML / ESP32)
    temperature = 98.6
    bpm = 75
    spo2 = 97

    input_values = {
        "Temperature (°F)": temperature,
        "Heart Rate (BPM)": bpm,
        "SpO₂ (%)": spo2,
    }

    has_alert = False

    if temperature > 99.5:
        alerts.append("🤒 Fever detected")
        has_alert = True

    if spo2 < 95:
        alerts.append("🛑 Low SpO₂ detected")
        has_alert = True

    if bpm < 60 or bpm > 100:
        alerts.append("⚠️ Abnormal heart rate")
        has_alert = True

    if not has_alert:
        alerts = ["✅ All vitals are normal"]

    result = "✅ Health status checked successfully"

    return render(request, 'health_app/index.html', {
        'result': result,
        'alerts': alerts,
        'input_values': input_values,
    })
