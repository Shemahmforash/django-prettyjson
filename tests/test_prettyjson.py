from unittest import TestCase
import mock

from prettyjson import PrettyJSONWidget


class TestPrettyJson(TestCase):
    def test_widget_without_args_renders_raw_view(self):
        widget = PrettyJSONWidget()

        result = widget.render(mock.MagicMock(), mock.MagicMock())

        self.assertIn('data-initial="raw"', result)

    def test_widget_renders_parsed_view_when_requested(self):
        widget = PrettyJSONWidget(attrs={'initial': 'parsed'})

        result = widget.render(mock.MagicMock(), mock.MagicMock())

        self.assertIn('data-initial="parsed"', result)

    def test_widget_renders_raw_view_when_requested(self):
        widget = PrettyJSONWidget(attrs={'initial': 'raw'})

        result = widget.render(mock.MagicMock(), mock.MagicMock())

        self.assertIn('data-initial="raw"', result)

    def test_widget_renders_raw_view_when_invalid_requested(self):
        widget = PrettyJSONWidget(attrs={'initial': 'invalid_view'})

        result = widget.render(mock.MagicMock(), mock.MagicMock())

        self.assertIn('data-initial="raw"', result)

    def test_widget_without_args_renders_buttons_visible(self):
        widget = PrettyJSONWidget()

        result = widget.render(mock.MagicMock(), mock.MagicMock())

        self.assertIn('data-visible="True"', result)

    def test_widget_renders_buttons_visible_when_requested(self):
        widget = PrettyJSONWidget(attrs={'visible': True})

        result = widget.render(mock.MagicMock(), mock.MagicMock())

        self.assertIn('data-visible="True"', result)

    def test_widget_renders_buttons_hidden_when_requested(self):
        widget = PrettyJSONWidget(attrs={'visible': False})

        result = widget.render(mock.MagicMock(), mock.MagicMock())

        self.assertIn('data-visible="False"', result)
