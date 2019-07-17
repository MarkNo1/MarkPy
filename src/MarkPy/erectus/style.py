# License
TM = u"\u2122"


# All Colors Range
_COLORS_ = [ dict(a=a,b=b,c=c)
            for a in range(8)
            for b in range(38)
            for c in range(48)]


# Create Color Code
Colorizer = lambda a, b, c : f'{a};{b};{c}'

# Get the Color from the Color Table
ColorizeFromTable = lambda color : Colorizer(**color)

# Get Text with Added Color
ColorizeInternal = lambda color_id, text : f'\x1b[%sm{text}\x1b[0m' % (color_id)

# Get Style with human code
Colorize = lambda color_id, text: ColorizeInternal(_COLOR_TABLE_[color_id], text)

# COLORS TABLE
_COLOR_TABLE_ = dict( (idx,code_id) for idx, code_id in enumerate(list(map(ColorizeFromTable, _COLORS_))))

# Print all avaible styles
ShowAllStyles = lambda : print('STYLES TABLES\n\n' + '\t'.join([ColorizeInternal(style_code,human_code)
                                                                for human_code, style_code in _COLOR_TABLE_.items()]))


## Commons idioms for logging:
Success = lambda text: Colorize(13088, text)    #Green
Error = lambda text: Colorize(13087, text)      #Red
Warning = lambda text: Colorize(13137, text)    #Orange
Higlight = lambda text: Colorize(1679, text)    #Blue


# Emojify
Emoji = lambda unicode : unicode.decode('utf-8')

# Commons utf-8 idioms
_fail_ = u'\U00002705'.encode('utf-8')
_success_ = u'\U00002705'.encode('utf-8')

Mark = lambda result : Emoji(_success_) if result else Emoji(_fail_)
