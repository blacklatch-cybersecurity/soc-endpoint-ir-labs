# SOC Alert Triage Automation
# Purpose: Reduce alert noise and prioritise incidents

alerts = [
    {"id": 1, "type": "Failed Login", "count": 3, "source": "Endpoint"},
    {"id": 2, "type": "Failed Login", "count": 25, "source": "Endpoint"},
    {"id": 3, "type": "Malware Detection", "count": 1, "source": "EDR"},
    {"id": 4, "type": "USB Device Inserted", "count": 1, "source": "Endpoint"},
    {"id": 5, "type": "Multiple USB Removals", "count": 5, "source": "Endpoint"},
]

def classify_severity(alert):
    if alert["type"] == "Malware Detection":
        return "HIGH"
    if alert["type"] == "Failed Login" and alert["count"] > 10:
        return "MEDIUM"
    if alert["type"] == "Multiple USB Removals":
        return "MEDIUM"
    return "LOW"

print("SOC ALERT TRIAGE REPORT\n")

for alert in alerts:
    severity = classify_severity(alert)
    print(f"Alert ID: {alert['id']}")
    print(f"Type: {alert['type']}")
    print(f"Source: {alert['source']}")
    print(f"Count: {alert['count']}")
    print(f"Severity: {severity}")
    print("-" * 30)
