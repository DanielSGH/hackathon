# class EnergyReading:
#         def __init__(self, device_id: str, watt_hours: float): ...
#         @property
#         def device_id(self) -> str: ...
#         @property
#         def watt_hours(self) -> float: ...

# def process_reading(self, reading: EnergyReading) -> ReadingResult:
#         # Code to process the reading
#         pass

import sys, math

from EnergyReading import EnergyReading



import SmartEnergyMonitor, random, string

def generate_random_string(N):
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for _ in range(N))


def test_process_reading(anomaly_threshold):
    maxint = 2_147_000_000

    device_id = random.randint(0, maxint)
    watt_hours = random.triangular(0, anomaly_threshold)

    try:
        EnergyReading(str(device_id), watt_hours)
    except:
        print("failure: " + sys.exc_info()[0])

    test_inputs = []

    for i in range(1,200):
        quadrant1 = [[0, device_id], [watt_hours, anomaly_threshold]]
        quadrant2 = [[device_id, maxint], [watt_hours, anomaly_threshold]]
        quadrant3 = [[0, device_id], [0.0, watt_hours]]
        quadrant4 = [[device_id, maxint], [0.0, watt_hours]]

        quadrants = [quadrant1, quadrant2, quadrant3, quadrant4]

        sizes = []
        for quadrant in quadrants:
            sizes.append(abs(quadrant[0][1] - quadrant[0][0]) * (abs(quadrant[1][1] - quadrant[1][0])))

        max = 0
        loc = 0
        for i in range(len(sizes)):
            if sizes[i] > max:
                max = sizes[i]
                loc = i
        
        device_id = random.randint(quadrants[loc][0][0], quadrants[loc][0][1])
        watt_hours = random.triangular(quadrants[loc][1][0], quadrants[loc][1][1])

        try:
            input = EnergyReading(device_id, watt_hours)
            test_inputs.append(input)
        except:
            print("Error: " + sys.exc_info()[0])

        # print(device_id, watt_hours)


if __name__ == '__main__':
    test_process_reading(1000)
    