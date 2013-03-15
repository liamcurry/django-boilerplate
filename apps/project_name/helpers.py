import jinja2
from django.conf import settings
from django.utils.encoding import force_bytes, force_text
from jingo import register


@register.function
def thumbnail(file_, geometry_string, **options):
    from sorl.thumbnail.shortcuts import get_thumbnail
    options.setdefault('format', 'PNG')
    try:
        im = get_thumbnail(file_, geometry_string, **options)
    except IOError:
        im = None
    return im


@register.function
def pygmentize(content, *args, **kwargs):
    from pygments import highlight
    from pygments.lexers import (get_lexer_by_name, TextLexer,
                                 get_lexer_for_filename, guess_lexer,
                                 get_lexer_for_mimetype)
    from pygments.formatters import HtmlFormatter
    opts = {'name': None, 'filename': None, 'mimetype': None}
    lexer_opts = {'encoding': 'UTF-8'}
    formatter_opts = {
        'linenos': True,
        'lineanchors': 'blob',
        'anchorlinenos': True
    }

    for key, value in kwargs.items():
        if key in opts:
            opts[key] = value
        elif key in formatter_opts:
            formatter_opts[key] = value
        elif key in lexer_opts:
            lexer_opts[key] = value

    formatter = HtmlFormatter(**formatter_opts)

    try:
        if opts['name']:
            lexer = get_lexer_by_name(opts['name'], **lexer_opts)
        elif opts['filename']:
            lexer = get_lexer_for_filename(opts['filename'], **lexer_opts)
        elif opts['mimetype']:
            lexer = get_lexer_for_mimetype(opts['mimetype'], **lexer_opts)
        else:
            lexer = guess_lexer(content, **lexer_opts)
    except:
        lexer = TextLexer(**lexer_opts)

    return jinja2.Markup(highlight(content, lexer, formatter))


@register.filter
def textile(value):
    import textile
    return jinja2.Markup(force_text(textile.textile(force_bytes(value),
                         encoding='utf-8', output='utf-8')))


@register.filter
def markdown(value, extensions=[]):
    import markdown
    return jinja2.Markup(markdown.markdown(force_text(value), extensions,
                                           safe_mode=False))


@register.filter
def restructuredtext(value):
    from docutils.core import publish_parts
    rst_settings = getattr(settings, 'RESTRUCTUREDTEXT_FILTER_SETTINGS', {})
    parts = publish_parts(source=force_bytes(value), writer_name='html4css1',
                          settings_overrides=rst_settings)
    return jinja2.Markup(force_text(parts["fragment"]))


@register.filter
def timesince(text):
    from django.template.defaultfilters import timesince
    return timesince(text)
