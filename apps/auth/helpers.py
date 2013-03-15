from jingo import register


@register.function
def gravatar(email, size=48):
    import hashlib
    import urllib
    url = '//www.gravatar.com/avatar.php?' + urllib.urlencode({
        'gravatar_id': hashlib.md5(email).hexdigest(),
        #'default': 'http://www.mysite.com/media/images/no-avatar.gif',
        'size': str(size)
    })
    return url
