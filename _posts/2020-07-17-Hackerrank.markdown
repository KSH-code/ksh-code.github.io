---
title: Nearest Neighboring City
tags:
- algorithm
category: blog
---

### Description
Every city has an integral coordinate location like (x, y) and it is denoted on Euclidean plain.
#### How to find out the nearest city?
First, if cities shares either an x or y, it can be in queried list.

Second, a distance beween cities is calculated Pythagorean theorem. (e.g. (x1 - x2)^2 + (y1 - y2)^2)

Finally, if some cities have the same distance, the nearest city is an alphabetically shorter name.
### Input
c = [] Array of strings which is a name of city. for construction a map.

x = [] Array of integers for construction a map.

y = [] Array of integers for construction a map.

q = []  Array of strings which is a name of city. for querying.

### Output
print each line with a name of the nearest city.

However, what if any city does not share x or y?

Just print `'NONE'`. that's it.
### Code
```
def closestStraightCity(c, x, y, q)
  cities_by_x = {}
  cities_by_y = {}
  index = 0
  city_map = {}
  x.zip(y).each do |location_x, location_y|
    cities_by_x[location_x] ||= []
    cities_by_y[location_y] ||= []
    cities_by_x[location_x] << [c[index], location_y]
    cities_by_y[location_y] << [c[index], location_x]
    city_map[c[index]] = [location_x, location_y]
    index += 1
  end

  cities_by_x.values.each { |arr| arr.sort_by!(&:last) }
  cities_by_y.values.each { |arr| arr.sort_by!(&:last) }

  q.map do |city|
    location_x, location_y = city_map[city]
    near_cities_by_x = cities_by_x[location_x]
    near_cities_by_y = cities_by_y[location_y]

    x_lower_index = lower_bound(near_cities_by_x, 0, near_cities_by_x.size - 1, location_y)
    x_upper_index = upper_bound(near_cities_by_x, 0, near_cities_by_x.size - 1, location_y)
    y_lower_index = lower_bound(near_cities_by_y, 0, near_cities_by_y.size - 1, location_x)
    y_upper_index = upper_bound(near_cities_by_y, 0, near_cities_by_y.size - 1, location_x)
    get_result([
                 {
                   city: near_cities_by_x[x_lower_index].first,
                   distance: (near_cities_by_x[x_lower_index].last - location_y).abs
                 },
                 {
                   city: near_cities_by_x[x_upper_index].first,
                   distance: (near_cities_by_x[x_upper_index].last - location_y).abs
                 },
                 {
                   city: near_cities_by_y[y_lower_index].first,
                   distance: (near_cities_by_y[y_lower_index].last - location_x).abs
                 },
                 {
                   city: near_cities_by_y[y_upper_index].first,
                   distance: (near_cities_by_y[y_upper_index].last - location_x).abs
                 }
               ])
  end
end

def lower_bound(arr, low, high, value)
  while low < high
    mid = (low + high) / 2
    if arr[mid].last < value && arr[mid + 1].last < value
      low = mid + 1
    else
      high = mid
    end
  end
  low
end

def upper_bound(arr, low, high, value)
  while low < high
    mid = (low + high) / 2
    if arr[mid].last > value
      high = mid
    else
      low = mid + 1
    end
  end
  low
end

def get_result(values)
  values
    .sort_by { |value| value[:city] }
    .reject { |value| value[:distance].zero? }
    .min_by { |value| value[:distance] }&.[](:city) || 'NONE'
end
```
