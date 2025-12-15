# Endpoint USB Lock Control

## Control Objective
Prevent unauthorized endpoint access and mitigate insider threat or device theft
by enforcing hardware-presence authentication using a trusted USB device.

## Threat Model
Endpoints are vulnerable when:
- Devices are stolen or lost
- Unauthorized users gain physical access
- Insider threats attempt data exfiltration
- Endpoints remain unlocked after user absence

This control assumes the attacker has physical access to the endpoint.

## Control Description
A trusted USB device is registered as a physical authentication factor.
If the USB device is removed, the endpoint immediately enforces a security action
(lock or shutdown).

This creates a hardware-backed enforcement mechanism that does not rely on
user behavior or application-level security.

## Enforcement Mechanism
- Kernel-level hardware event monitoring
- Rule-based enforcement on device removal
- Immediate endpoint shutdown or session lock
- No user interaction required

## Security Benefits
- Prevents unauthorized access to active endpoints
- Reduces insider threat window
- Protects against lost or stolen laptop scenarios
- Enforces zero-trust physical presence

## Incident Response Alignment
This control supports IR by:
- Automatically containing endpoint access
- Reducing attacker dwell time
- Preserving system state for forensic analysis

## Limitations
- USB device cloning risk
- Requires physical possession of the key
- Device naming must be stable (UUID recommended)

## Hardening Recommendations
- Bind enforcement to USB UUID
- Encrypt USB key material
- Combine with login-based authentication
- Integrate with endpoint logging and alerts

## SOC Relevance
This control demonstrates endpoint hardening,
insider threat mitigation, and proactive containment strategy.
