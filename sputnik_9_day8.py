'''
Sputnik 9 🚀
MARCH 9, 2026

Ever heard of the Space Race? It was a Cold War-era competition between the United States and the Soviet Union to best each other in spaceflight capability.

On this day in 1961, the Soviet Union launched the Sputnik 9 spacecraft into the atmosphere. It was the final rehearsal for sending a human into space.

image

Onboard were:

👤 A mannequin cheekily named Ivan Ivanovich (Russian equivalent of "John Doe")
🐕‍🦺 A black dog named Chernushka
🐁 Several mice
🐹 A guinea pig
And before you ask: Yes, all the animals (and Ivan) survived the one full orbit! 😮‍💨

The animals were in their own capsule of the spacecraft, which landed safely in its parachute.

The Earth's atmosphere is divided into five layers:

Exosphere (700–10,000 km): descent rate = 2000 m/s (near vacuum, free fall)
Thermosphere (85–700 km): descent rate = 500 m/s (thin air, minimal drag)
Mesosphere (50–85 km): descent rate = 200 m/s (air thickens, meteors burn here)
Stratosphere (12–50 km): descent rate =  75 m/s (ozone layer, much denser)
Troposphere (0–12 km): descent rate = 20 m/s (densest layer, parachute deploys 🪂)
Sputnik 9's reentry begins from ~200 km. That's in the thermosphere. The atmospheric density increases as the capsule descends... the descent rate slows the lower it gets.

Given a starting altitude (in km), calculate total descent time (in seconds and one decimal).

Examples
Example 1

Input: 200
Output: 1511.7
230.0s (Thermosphere) + 175.0s (Mesosphere) + 506.7s (Stratosphere) + 600.0s (Troposphere)

Example 2

Input: 12
Output: 600.0
600.0s (Troposphere)

In JavaScript, it might just be 600.
'''


def calculate_descent(altitude):
  # Write code below 💖
    time = 0.0
    while altitude > 0: 
        if altitude > 700:
            steps = altitude - 700
            time = time + ((steps * 1000) / 2000)
            altitude = 700 
        
        elif altitude > 85:
            steps = altitude - 85
            time = time + ((steps * 1000) / 500)
            altitude = 85 
        
        elif altitude > 50:
            steps = altitude - 50
            time = time + ((steps * 1000) / 200)
            altitude = 50

        elif altitude > 12:
            steps = altitude - 12
            time = time + ((steps * 1000) / 75)
            altitude = 12
        
        elif altitude > 0:
            steps = altitude 
            time = time + ((steps * 1000) / 20)
            altitude = 0
        
        else:
            raise ValueError(f"Unexpected altitude: {altitude}")
    return round(time, 1) 

altitude = 200
print(calculate_descent(altitude))


    