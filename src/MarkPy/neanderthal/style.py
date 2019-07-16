## COLORS

# All Colors Range
STYLES_ = [ dict(a=a,b=b,c=c)
            for a in range(8)
            for b in range(38)
            for c in range(48)]


# Create Color Code
StyleCode = lambda a, b, c : f'{a};{b};{c}'

# Get the Color from the Color Table
StyleCodeFromTable = lambda code : StyleCode(**code)

# Get Text with Added Color
StyledTextInternal = lambda color, text : f'\x1b[%sm{text}\x1b[0m' % (color)

# Get Style with human code
UseStyle = lambda human_code, text: StyledTextInternal(STYLES_TABLE[human_code], text)

# COLORS TABLE
STYLES_TABLE = dict( (idx,code) for idx, code in enumerate(list(map(StyleCodeFromTable, STYLES_))))

# Print all avaible styles
ShowAllStyles = lambda : print('STYLES TABLES\n\n' + '\t'.join([StyledTextInternal(style_code,human_code)
                        for human_code, style_code in STYLES_TABLE.items()]))


### DEFINE your commons styles:

Success = lambda text: UseStyle(13088, text)
Fail = lambda text: UseStyle(13087, text)
Warning = lambda text: UseStyle(13137, text)
Header = lambda text: UseStyle(1679, text)


#### UNICODE

# License Marco Treglia
TM = u"\u2122"

# Emoji
Decode = lambda unicode : unicode.decode('utf-8')
Emoji = Decode
Encode = lambda unicode : unicode.encode('utf-8')


# Logging
fail_ = u'\U00002705'.encode('utf-8')
success_ = u'\U00002705'.encode('utf-8')

FAIL = lambda : Emoji(fail)
SUCCESS = lambda : Emoji(success_)
Mark = lambda result : SUCCESS() if result else FAIL()
