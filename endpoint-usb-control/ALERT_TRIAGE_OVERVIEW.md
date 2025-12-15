# SOC Alert Triage Automation

## Problem Statement
SOC teams receive thousands of alerts daily.
Most alerts are low-value noise, leading to analyst fatigue
and delayed incident response.

## Objective
Automate first-level alert triage by:
- Classifying alert severity
- Reducing false positives
- Highlighting incidents requiring analyst action

## Triage Logic
Alerts are categorised using simple rules:
- Malware detections → High severity
- High-volume failed logins → Medium severity
- Repeated USB activity → Medium severity
- All others → Low severity

## SOC Value
- Reduces alert fatigue
- Improves response prioritisation
- Allows analysts to focus on real incidents
- Demonstrates detection-to-decision workflow

## Incident Response Alignment
High and medium severity alerts
can be escalated for containment,
investigation, and response actions.

## Future Enhancements
- Integration with SIEM logs
- Time-based correlation
- Automated ticket creation
