import json

def json_create_file():
    data = {
        "Sun": {
            "color": "#ffff00",
            "pos": [
                500,
                400
            ],
            "density": 1.4
        },
        "planets": {
            "Mercury": {
                "orbit_radius": 80,
                "rotation_speed": 4.0,
                "size": 8,
                "density": 7.1,
                "color": [
                    218,
                    165,
                    32,
                    255
                  ]
            },
            "Venus": {
                "orbit_radius": 110,
                "rotation_speed": 3.0,
                "size": 11,
                "density": 5.04,
                "color": [
                    80,
                    188,
                    107,
                    255
                ]
            },
            "Earth": {
                "orbit_radius": 160,
                "rotation_speed": 2.5,
                "size": 9,
                "density": 5.91,
                "color": [
                    140,
                    209,
                    80,
                    255
                ]
            },
            "Mars": {
                "orbit_radius": 190,
                "rotation_speed": 2.0,
                "size": 7,
                "density": 3.93,
                "color": [
                    40,
                    151,
                    135,
                    255
                ]
            },
            "Jupiter": {
                "orbit_radius": 230,
                "rotation_speed": 1.2,
                "size": 18,
                "density": 2.5,
                "color": [
                    52,
                    98,
                    139,
                    255
                ]
            },
            "Saturn": {
                "orbit_radius": 290,
                "rotation_speed": 0.9,
                "size": 23,
                "density": 0.39,
                "color": [
                    68,
                    1,
                    84,
                    255
                ]
            },
            "Uranus": {
                "orbit_radius": 340,
                "rotation_speed": 0.7,
                "size": 14,
                "density": 1.07,
                "color": [
                    64,
                    32,
                    105,
                    255
                ]
            },
            "Neptune": {
                "orbit_radius": 380,
                "rotation_speed": 0.5,
                "size": 13,
                "density": 1.64,
                "color": [
                    61,
                    60,
                    124,
                    255
                ]
            }
        }
    }

    with open('solar_system_planets.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print('made it')
    return data
