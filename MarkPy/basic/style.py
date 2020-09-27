from .atom import Atom

import emoji


class ColorTable():

    _common_ = list(range(79, 84))
    _sequence_ = -1

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

    def get_sequential_color(self):
        if self._sequence_ > len(self._common_) - 1:
            self._sequence_ = -1
        return self._common_[self._sequence_]

    def increase_sequence(self):
        self._sequence_ +=1



class EmojyTable():
    def __init__(self):
        self._table_ = [emo for name, emo  in emoji.unicode_codes.EMOJI_UNICODE.items()]

    def __call__(self, emojyID):
        return self._table_[emojyID]

    def __len__(self):
        return len(self._table_)


class Style(Atom):

    __style_version__ = 3
    _colors_ = ColorTable()
    _emoji_ = EmojyTable()


    def __init__(self):
        Atom.__init__(self)
        self.newAtom(self.sequential('Style'), self.sequential(self.__style_version__))
        self.next_sequential()

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

    def next_sequential(self):
        self._colors_.increase_sequence()

    def sequential(self, text):
        return self.color(self._colors_.get_sequential_color(), text)

    def auto_sequential(self, text):
        self.next_sequential()
        return self.color(self._colors_.get_sequential_color(), text)

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

    def lightviolet(self, text):
        return self.color(93, text)

    def lightblue(self, text):
        return self.color(36, text)

    def bred(self, text):
        return self.color(41, text)

    def bgreen(self, text):
        return self.color(42, text)

    def borange(self, text):
        return self.color(43, text)

    def bblue(self, text):
        return self.color(44, text)

    def bviolet(self, text):
        return self.color(45, text)

    def blightblue(self, text):
        return self.color(46, text)

    def mark(self):
        return self.emoji(3086)

    def denied(self):
        return self.emoji(2169)

def test_style():
    s = Style()
    s.showAllColors()
    s.showAllEmoji()

    print(s.green('Green') + s.red('Red') + s.orange('Orange') + s.blue('Blue') + s.violet('Violet') + s.lightblue('Lightblue'))
    print(s.mark() + s.denied())
