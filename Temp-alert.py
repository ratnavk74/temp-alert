import sys

if len(sys.argv) == 2:
    temperature = float(sys.argv[1])
    print("User provided temperature:")
else:
    temperature = 25   
    print("No input provided — using default temperature:")

if temperature < 15:
    status = "Cold"
elif 15 <= temperature <= 30:
    status = "Normal"
else:
    status = "Hot"

print("\n----- TEMPERATURE ALERT -----")
print("Temperature (°C):", temperature)
print("Status:", status)
