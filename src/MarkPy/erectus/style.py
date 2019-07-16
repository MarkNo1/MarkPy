''' Designed for python 3.7

    Copyright 2019  Marco Treglia

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS;    OR #BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHET ER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.""
'''

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
ColorizeFromTable = lambda code : Colorizer(**code)

# Get Text with Added Color
ColorizeInternal = lambda color, text : f'\x1b[%sm{text}\x1b[0m' % (color)

# Get Style with human code
Colorize = lambda color, text: ColorizeInternal(_COLOR_TABLE_[style], text)

# COLORS TABLE
_COLOR_TABLE_ = dict( (idx,code) for idx, code in enumerate(list(map(ColorizeFromTable, _COLORS_))))

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
