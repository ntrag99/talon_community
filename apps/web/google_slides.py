from talon.voice import Context, Key, press
from talon import ctrl

ctx = Context('google_slides', func=lambda app, win:
              win.title.endswith('- Google Slides') or '- Google Slides -' in win.title)
ctx.keymap({
    'new slide': Key('ctrl+m'),
    'duplicate slide': Key('cmd+d'),
    'undo': Key('cmd+z'),
    'redo': Key('cmd+y'),
    'copy': Key('cmd+c'),
    'cut': Key('cmd+x'),
    'paste': Key('cmd+v'),
    'copy formatting of the selected text or shape': Key('cmd+alt+c'),
    'paste formatting of the selected text or shape': Key('cmd+alt+v'),
    'insert or edit link': Key('cmd+k'),
    'open link': Key('alt+enter'),
    'delete': Key('delete'),
    'select all': Key('cmd+a'),
    'select none': Key('cmd+shift+a'),
    'find': Key('cmd+f'),
    'find and replace': Key('cmd+shift+h'),
    'find again': Key('cmd+g'),
    'find previous': Key('cmd+shift+g'),
    'open...': Key('cmd+o'),
    'print': Key('cmd+p'),
    'save': Key('cmd+s'),
    'show common keyboard shortcuts': Key('cmd+/'),
    'search the menus': Key('alt+/'),
    'hide or show menus ': Key('ctrl+shift+f'),
    'move to previous slide': Key('up'),
    'move to next slide': Key('down'),
    'move focus to first slide': Key('home'),
    'move focus to last slide': Key('end'),
    'move slide up': Key('cmd+up'),
    'move slide down': Key('cmd+down'),
    'move slide to beginning': Key('cmd+shift+up'),
    'move slide to end': Key('cmd+shift+down'),
    'select previous slide': Key('shift+up'),
    'select next slide': Key('shift+down'),
    'select first slide': Key('shift+home'),
    'select last slide': Key('shift+end'),
    'zoom in': Key('cmd+altand +'),
    'zoom out': Key('cmd+altand-'),
    'move to filmstrip': Key('cmd+alt+shift+f'),
    'move to canvas': Key('cmd+alt+shift+c'),
    'open speaker notes panel': Key('cmd+alt+shift+s'),
    'change to html view of presentation': Key('cmd+alt+shift+p'),
    'open animations panel': Key('cmd+alt+shift+b'),
    'continue in animation preview': Key('enter'),
    'open explore tool': Key('cmd+alt+shift+i'),
    'define selected word in explore tool': Key('cmd+shift+y'),
    'go to side panel': Key('cmd+alt+.'),
    'open revision history panel': Key('cmd+alt+shift+h'),
    'open cell border selection ': lambda m: (
        ctrl.key_press('cmd', ctrl=True, cmd=True, down=True),
        press('e'), press('p'),
        ctrl.key_press('cmd', ctrl=True, cmd=True, up=True),
    ),
    'play the selected video': Key('enter'),
    'present slides': Key('cmd+enter'),
    'present slides from beginning': Key('cmd+shift+enter'),
    'exit the current mode': Key('esc'),
    'context menu': Key('cmd+shift+\\'),
    'file menu': Key('ctrl+alt+f'),
    'edit menu': Key('ctrl+alt+e'),
    'view menu': Key('ctrl+alt+v'),
    'insert menu': Key('ctrl+alt+i'),
    'slide menu': Key('ctrl+alt+s'),
    'format menu': Key('ctrl+alt+o'),
    'arrange menu': Key('ctrl+alt+r'),
    'tools menu': Key('ctrl+alt+t'),
    'help menu': Key('ctrl+alt+h'),
    'input tools menu': Key('cmd+alt+shift+k'),
    'toggle input controls': Key('cmd+shift+k'),
    'insert comment': Key('cmd+alt+m'),
    'enter current comment': Key('ctrl+enter'),
    'move to next comment': lambda m: (
        ctrl.key_press('cmd', ctrl=True, cmd=True, down=True),
        press('n'), press('c'),
        ctrl.key_press('cmd', ctrl=True, cmd=True, up=True),
    ),
    'move to previous comment': lambda m: (
        ctrl.key_press('cmd', ctrl=True, cmd=True, down=True),
        press('p'), press('c'),
        ctrl.key_press('cmd', ctrl=True, cmd=True, up=True),
    ),
    ## these are duplicates that only work if you have a comment selected
    # 'move to next comment': Key('j'),
    # 'move to previous comment': Key('k'),
    'reply to comment': Key('r'),
    'resolve comment': Key('e'),
    'open comment discussion thread': Key('cmd+alt+shift+a'),
    'bold': Key('cmd+b'),
    'italic': Key('cmd+i'),
    'underline': Key('cmd+u'),
    'subscript': Key('cmd+,'),
    'superscript': Key('cmd+.'),
    'strikethrough': Key('cmd+shift+x'),
    'clear formatting': Key('cmd+\\'),
    'increase font size': Key('cmd+shift+>'),
    'decrease font size': Key('cmd+shift+<'),
    'left align': Key('cmd+shift+l'),
    'right align': Key('cmd+shift+r'),
    'center align': Key('cmd+shift+e'),
    'justify': Key('cmd+shift+j'),
    'select paragraph above': Key('alt+shift+up'),
    'select paragraph below': Key('alt+shift+down'),
    'increase indent': Key('cmd+]'),
    'decrease indent': Key('cmd+['),
    'bulleted list': Key('cmd+shift+8'),
    'numbered list': Key('cmd+shift+7'),
    'select list item': lambda m: (
        ctrl.key_press('shift', ctrl=True, cmd=True, shift=True, down=True),
        press('e'), press('i'),
        ctrl.key_press('shift', ctrl=True, cmd=True, shift=True, up=True),
    ),
    'select list items at current level': lambda m: (
        ctrl.key_press('shift', ctrl=True, cmd=True, shift=True, down=True),
        press('e'), press('o'),
        ctrl.key_press('shift', ctrl=True, cmd=True, shift=True, up=True),
    ),
    'move to next text formatting change': lambda m: (
        ctrl.key_press('cmd', ctrl=True, cmd=True, down=True),
        press('n'), press('w'),
        ctrl.key_press('cmd', ctrl=True, cmd=True, up=True),
    ),
    'move to previous text formatting change': lambda m: (
        ctrl.key_press('cmd', ctrl=True, cmd=True, down=True),
        press('p'), press('w'),
        ctrl.key_press('cmd', ctrl=True, cmd=True, up=True),
    ),
    'move to next misspelling': Key('cmd+\''),
    'move to previous misspelling': Key('cmd+;'),
    'duplicate': Key('cmd+d'),
    'group': Key('cmd+alt+g'),
    'ungroup': Key('cmd+ alt+shift+g'),
    'send backward': Key('cmd+down'),
    'bring forward': Key('cmd+up'),
    'send to back': Key('cmd+shift+down'),
    'bring to front': Key('cmd+shift+up'),
    'select next shape': Key('tab'),
    'select previous shape': Key('shift+tab'),
    'nudge up, down, left, or right': Key('keys'),
    'nudge one pixel at a time': Key('shift+keys'),
    'rotate counterclockwise by 1 degree': Key('alt+shift+left'),
    'rotate clockwise by 1 degree': Key('alt+shift+right'),
    'rotate counterclockwise by 15 degree': Key('alt+left'),
    'rotate clockwise by 15 degree': Key('alt+right'),
    'resize larger horizontally': Key('cmd+ctrl+b'),
    'resize larger vertically': Key('cmd+ctrl+i'),
    'resize smaller': Key('cmd+ctrl+j'),
    'resize larger': Key('cmd+ctrl+k'),
    'resize smaller horizontally': Key('cmd+ctrl+w'),
    'exit crop mode': Key('enter'),
    'speak selection': Key('ctrl+cmd+x'),
    'enable screen reader support': Key('alt+cmd+z'),
    'speak from cursor location': Key('ctrl+cmd+r'),
    'announce formatting at cursor location': lambda m: (
        ctrl.key_press('cmd', ctrl=True, cmd=True, down=True),
        press('a'), press('f'),
        ctrl.key_press('cmd', ctrl=True, cmd=True, up=True),
    ),
})
