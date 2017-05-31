from django.forms import widgets


class PrettyJSONWidget(widgets.Textarea):

    DEFAULT_START_AS = 'raw'
    DEFAULT_BUTTONS_VISIBLE = True

    def render(self, name, value, attrs=None):
        html = super(PrettyJSONWidget, self).render(name, value, attrs)

        start_as = self.attrs.get("initial", self.DEFAULT_START_AS)

        if (start_as not in self._allowed_attrs()):
            start_as = self.DEFAULT_START_AS

        visible = bool(self.attrs.get("visible", self.DEFAULT_BUTTONS_VISIBLE))

        return ('<div class="jsonwidget" data-initial="' + start_as + '" data-visible="'
                + str(visible) + '"><p><button class="parseraw" '
                'type="button">Show parsed</button> <button class="parsed" '
                'type="button">Collapse all</button> <button class="parsed" '
                'type="button">Expand all</button></p>' + html + '<div '
                'class="parsed"></div></div>')

    @staticmethod
    def _allowed_attrs():
        return (PrettyJSONWidget.DEFAULT_START_AS, 'parsed')

    class Media:
        # http://stackoverflow.com/questions/7188563/django-admin-jquery-namespace
        js = ('prettyjson/prettyjson.js', )
        # https://docs.djangoproject.com/en/1.9/topics/forms/media/#css
        css = {
            'all': ('prettyjson/prettyjson.css', )
        }
