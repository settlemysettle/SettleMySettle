from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    ''' Used in templates to check if a user is in the admin group '''
    return user.groups.filter(name=group_name).exists()
