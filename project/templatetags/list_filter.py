from django import template

register = template.Library()

#@register.filter()
@register.simple_tag
def get_at_index(list, x, y, n, m):
    #list=> Name = [[0 for y in range(1,ymax+1)] for x in range(1,xmax+1)]
    #x = 1.....xmax+1, y = ymax+1......1
    #n = length(x), m = length(y)
    m = m + 1
    y = abs(m - y) - 1
    x = x - 1
    return list[x][y]
