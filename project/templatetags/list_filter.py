from django import template

register = template.Library()

#@register.filter()
@register.simple_tag
def get_at_index(list, x, y, n, m):
    # if args is None:
    #     return False
    # arg_list = [arg.strip() for arg in args.split(',')]
    
    m = m - n
    y = abs(m-y)
    x = x - 1
    return list[x][y]
