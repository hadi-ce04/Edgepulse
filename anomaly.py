def analyze_device(device):
    alerts=[]
    if device.temperature>70: alerts.append("High temperature")
    if device.vibration>5: alerts.append("Excessive vibration")
    if device.cpu>85: alerts.append("High CPU utilization")
    if device.memory>90: alerts.append("High memory utilization")
    if device.latency>180: alerts.append("High network latency")
    if device.battery<15: alerts.append("Low battery")
    device.anomaly=bool(alerts)
    device.status="warning" if device.anomaly else "online"
    device.alert=" • ".join(alerts)
