import json
import matplotlib.colors as mcolors

def create_planets_with_color(data):
    # Извлекаем плотности всех планет
    densities = [data['planets'][planet]['density'] for planet in data['planets']]
    min_density = min(densities)
    max_density = max(densities)

    colormap = mcolors.LinearSegmentedColormap.from_list('density_colormap',
                                                         ['#440154', '#3b528b', '#21918c', '#5ec962', '#daa520'])

    for planet in data['planets']:
        density = data['planets'][planet]['density']
        
        # Нормализуем плотность от 0 до 1
        normalized_density = (density - min_density) / (max_density - min_density)
        rgb_color = [int(c * 255) for c in colormap(normalized_density)]
        data['planets'][planet]['color'] = rgb_color
    
    with open('solar_system_planets.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    