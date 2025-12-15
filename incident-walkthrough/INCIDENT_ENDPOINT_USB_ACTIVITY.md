# Incident Walkthrough — Suspicious Endpoint USB Activity

## Incident Summary
A workstation generated multiple USB-related alerts within a short time window,
indicating potential insider threat activity or unauthorized endpoint interaction.

The incident was detected through endpoint monitoring and escalated
for SOC review.

## Detection
The following alerts were observed:
- Repeated USB insertion and removal events
- Correlated endpoint activity within a short time frame

These alerts triggered SOC triage due to abnormal frequency.

## Triage Analysis
SOC analysis identified:
- USB activity exceeding normal user behavior
- Potential attempts to bypass endpoint controls
- No authorized maintenance window recorded

Severity was classified as MEDIUM due to:
- Physical access implications
- Potential data exfiltration risk

## Containment Actions
The endpoint enforcement control automatically:
- Detected USB removal
- Triggered system shutdown
- Prevented further endpoint access

No manual analyst intervention was required.

## Impact Assessment
- No data exfiltration confirmed
- Endpoint state preserved for review
- User access temporarily disrupted

Impact was limited due to rapid containment.

## Lessons Learned
- Hardware-backed controls significantly reduce dwell time
- Automated enforcement lowers SOC response burden
- USB activity should be correlated with user context

## Recommendations
- Enforce USB-based endpoint controls on high-risk systems
- Correlate physical events with authentication logs
- Alert on abnormal peripheral behavior patterns

## SOC Value
This incident demonstrates effective detection, triage,
and automated containment of a physical access threat.
