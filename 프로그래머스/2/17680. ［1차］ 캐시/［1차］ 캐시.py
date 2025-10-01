import heapq

def solution(cacheSize, cities):
    cache_log = {city.upper():0 for city in set(cities)}
    cache = set()
    result = 0
    
    if cacheSize == 0:
        return 5*len(cities)
    
    for time, city in enumerate(cities):
        city = city.upper()
        if city in cache:
            result += 1
        else:
            result += 5
            if len(cache) == cacheSize:
                min_city, min_time = '', 10000000
                for cache_city in cache:
                    if cache_log[cache_city] < min_time:
                        min_city, min_time = cache_city, cache_log[cache_city]
                cache.remove(min_city)
            cache.add(city)
                
        cache_log[city] = time
    return result