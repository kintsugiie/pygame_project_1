import json

def json_create_file():
    data = {
        "Sun": {
            "color": "#ffff00",
            "pos": [408, 275],
            "density": 1.4
        },
        'planets': {
            "Mercury": {
                "orbit_radius": 80,
                "rotation_speed": 0.02,
                "size": 5,
                "density": 5.43
            },
            "Venus": {
                "orbit_radius": 120,
                "rotation_speed": 0.015,
                "size": 9,
                "density": 5.24
            },
            "Earth": {
                "orbit_radius": 160,
                "rotation_speed": 0.01,
                "size": 10,
                "density": 5.51
            },
            "Mars": {
                "orbit_radius": 200,
                "rotation_speed": 0.008,
                "size": 6,
                "density": 3.93
                },
            "Jupiter": {
                "orbit_radius": 280,
                "rotation_speed": 0.025,
                "size": 20,
                "density": 1.33
                },
            "Saturn": {
                "orbit_radius": 340,
                "rotation_speed": 0.022,
                "size": 17,
                "density": 0.69
                },
            "Uranus": {
                "orbit_radius": 380,
                "rotation_speed": 0.018,
                "size": 12,
                "density": 1.27
                },
            "Neptune": {
                "orbit_radius": 420,
                "rotation_speed": 0.016,
                "size": 11,
                "density": 1.64
                }
        }
    }

    # Сохраняем в JSON файл
    with open('solar_system_planets.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print("Файл 'solar_system_planets.json' успешно создан!")
    return data

