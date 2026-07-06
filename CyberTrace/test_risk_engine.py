from modules.risk_engine import calculate_risk


score, severity, reasons = calculate_risk(
    "File Created",
    "virus.exe",
    "123456789"
)

print("\n==============================")
print("   CyberTrace Risk Analysis")
print("==============================")

print(f"Risk Score : {score}")
print(f"Severity  : {severity}")

print("\nReasons")
print("-------")

for reason in reasons:
    print(f"• {reason}")

print("\n==============================")