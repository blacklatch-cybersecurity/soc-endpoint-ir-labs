# Technical Summary — Endpoint USB Lock

Platform: Linux (Parrot OS)
Mechanism: udev hardware event rules
Trigger: Physical removal of trusted USB device
Action: Immediate system shutdown

Key Components:
- udev rule bound to device identity
- systemctl enforcement action
- No dependency on userland applications

This implementation validates the concept of
hardware-backed endpoint enforcement.
