import json
import matplotlib.colors as mcolors

def create_planets_with_color(data):
    # Извлекаем плотности всех планет
    densities = [data['planets'][planet]['density'] for planet in data['planets']]
    min_density = min(densities)
    max_density = max(densities)
    
    print(f"Минимальная плотность: {min_density} g/cm³")
    print(f"Максимальная плотность: {max_density} g/cm³")
    
    # Создаем цветовую карту от синего (мин) к красному (макс)
    colormap = mcolors.LinearSegmentedColormap.from_list('density_colormap', ['blue', 'red'])
    
    # Добавляем цвет каждой планете
    for planet in data['planets']:
        density = data['planets'][planet]['density']
        
        # Нормализуем плотность от 0 до 1
        normalized_density = (density - min_density) / (max_density - min_density)
        
        # Получаем RGB цвет
        rgb_color = colormap(normalized_density)
        
        # Конвертируем в HEX
        hex_color = mcolors.to_hex(rgb_color)
        
        # Добавляем информацию о цвете
        data['planets'][planet]['color'] = hex_color
    
    with open('solar_system_planets.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    
    