import random

SAFE_DISTANCE = 20

def driving_decision(distance, obstacle, traffic_light):
    if obstacle:
        return "STOP - Obstacle detected"

    if traffic_light == "RED":
        return "STOP - Red light"

    if distance < SAFE_DISTANCE:
        return "SLOW DOWN - Vehicle too close"

    return "ACCELERATE - Road clear"


print("Autonomous Driving Decision System\n")

for step in range(5):

    # Simulated sensor inputs
    distance = random.randint(10, 40)
    obstacle = random.choice([True, False])
    traffic_light = random.choice(["GREEN", "RED"])

    print(f"Step {step+1}")
    print(f"Distance to vehicle: {distance} meters")
    print(f"Obstacle detected: {obstacle}")
    print(f"Traffic light: {traffic_light}")

    decision = driving_decision(distance, obstacle, traffic_light)

    print("Decision:", decision)
    print("-" * 30)
