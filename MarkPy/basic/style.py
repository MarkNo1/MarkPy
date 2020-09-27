import emoji

class ColorTable():
    def __init__(self):
        self._table_ = [ self._colorCode_(a,b,c)
                for a in range(8)
                for b in range(38)
                for c in range(48)]

    def _colorCode_(self, a,b,c):
        return f'{a};{b};{c}'

    def __len__(self):
        return len(self._table_)

    def __call__(self, colorID):
        return self._table_[colorID]

class EmojyTable():
    def __init__(self):
        self._table_ = [emo for name, emo  in emoji.unicode_codes.EMOJI_UNICODE.items()]

    def __call__(self, emojyID):
        return self._table_[emojyID]

    def __len__(self):
        return len(self._table_)


class Style:
    _colors_ = ColorTable()
    _emoji_ = EmojyTable()

    def _colorize_(self, colorCode, text):
        return f'\x1b[%sm{text}\x1b[0m' % (colorCode)

    def color(self, id, text):
        return self._colorize_(self._colors_(id), text)

    def emoji(self, id):
        return  self._emoji_(id)

    def __call__(self, style, text=None):
        if isinstance(style,int):
            if text:
                return self.color(style, text)
            else:
                return self.emoji(style)

    def showAllColors(self):
        styles = ''
        for x in range(len(self._colors_)):
            if x %10 == 0 :
                styles += '\n'
            styles += '  ' + self.color(x, x)
        print(styles)

    def showAllEmoji(self):
        counter = 0
        styles = ''
        for x in range(len(self._emoji_)):
            if x %10 == 0 :
                styles += '\n'
            styles += f'\t{counter}:' + self._emoji_(x)
            counter +=1
        print(styles)

    def green(self, text):
        return self.color(13088, text)

    def red(self, text):
        return self.color(13087, text)

    def orange(self, text):
        return self.color(13137, text)

    def blue(self, text):
        return self.color(1679, text)

    def mark(self):
        return self.emoji(3086)

    def denied(self):
        return self.emoji(2169)
