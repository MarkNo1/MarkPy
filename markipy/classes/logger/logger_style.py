from dataclasses import dataclass
import emoji

from .logger_meta import LoggerMeta


def colorize(color_code, text):
    return f'\x1b[%sm{text}\x1b[0m' % (color_code)


def colorcode(a, b, c):
    return f'{a};{b};{c}'


def get_color_table():
    return [colorcode(a, b, c)
            for a in range(8)
            for b in range(38)
            for c in range(48)]


@dataclass
class LoggerStyle(LoggerMeta):
    _log_colors = get_color_table()
    _log_colors_len = len(_log_colors)

    _log_emoji = [emo for name, emo in emoji.unicode_codes.EMOJI_UNICODE.items()]
    _log_emoji_len = len(_log_emoji)

    def color(self, color_id, text):
        return colorize(self._log_colors[color_id], text)

    def emoji(self, emoji_id):
        return self._log_emoji[emoji_id]

    def print_all_colors(self):
        colors = ''
        for i in range(self._log_colors_len):
            if i % 10 == 0:
                colors += '\n'
            colors += f' {self.color(i, str(i))}'
        print(colors)

    def print_all_emoji(self):
        emoticon = ''
        for i, e in enumerate(self._log_emoji):
            if i % 5 == 0:
                emoticon += '\n'
            emoticon += f'\t{i}: {e}'
        print(emoticon)

    def red(self, text):
        return self.color(79, text)

    def green(self, text):
        return self.color(80, text)

    def orange(self, text):
        return self.color(33, text)

    def yellow(self, text):
        return self.color(81, text)

    def blue(self, text):
        return self.color(82, text)

    def violet(self, text):
        return self.color(35, text)

    def cyan(self, text):
        return self.color(84, text)

    def light_violet(self, text):
        return self.color(93, text)

    def lightblue(self, text):
        return self.color(36, text)

    def grey(self, text):
        return self.color(4782, text)

    def bred(self, text):
        return self.color(41, text)

    def bold_green(self, text):
        return self.color(42, text)

    def bold_orange(self, text):
        return self.color(43, text)

    def bold_blue(self, text):
        return self.color(44, text)

    def bold_violet(self, text):
        return self.color(45, text)

    def bold_lightblue(self, text):
        return self.color(46, text)

    def underline_grey(self, text):
        return self.color(11954, text)

    def mark(self):
        return self.emoji(3086)

    def denied(self):
        return self.emoji(2169)
