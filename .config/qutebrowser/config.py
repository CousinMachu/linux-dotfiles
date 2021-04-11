#qutebrowser settings
c.url.start_pages = "https://ozencb.github.io/tilde-enhanced/"
c.editor.command = ["vim", "-f", "{}"]
c.downloads.position = "bottom"
c.downloads.location.directory = "~/Downloads/"
#c.content.user_stylesheets = ["/home/machu/.config/qutebrowser/solarized-all-sites-dark.css"]
c.scrolling.smooth = True
c.completion.height = "30%"
c.tabs.background = True
c.tabs.last_close = "close"
c.hints.chars = "arstdhneio"
#c.fonts.tabs = "12pt PragmataPro"
c.fonts.default_family = "PragmataPro"
c.fonts.default_size = "12pt"
c.url.searchengines = {"DEFAULT": "https://duckduckgo.com/?q={}", "d": "https://duckduckgo.com/?q={}", "y": "https://www.youtube.com/results?search_query={}&search=Search", "g": "https://www.google.com/search?q={}", "r": "https://www.reddit.com/search?q={}", "r/": "https://www.reddit.com/r/{}"}
#c.url.searchengines = {"DEFAULT": "https://www.google.com/search?q={}", "y": "https://www.youtube.com/results?search_query={}&search=Search", "g": "https://www.google.com/search?q={}", "r": "https://www.reddit.com/search?q={}"}
c.content.blocking.adblock.lists =  ["https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"]
c.qt.force_software_rendering = "qt-quick"

#Color
c.colors.tabs.odd.fg = "white"
c.colors.tabs.odd.bg = "black"
c.colors.tabs.even.fg = "white"
c.colors.tabs.even.bg = "black"
c.colors.tabs.selected.odd.fg = "white"
c.colors.tabs.selected.odd.bg = "grey"
c.colors.tabs.selected.even.fg = "white"
c.colors.tabs.selected.even.bg = "grey"

#Keybinds
#Open/Close
config.bind('O', 'set-cmd-text :open {url:pretty}')
config.bind('t', 'set-cmd-text -s :open -t')
config.bind('T', 'set-cmd-text :open -t {url:pretty}')
config.bind('W', 'set-cmd-text -s :open -w')
config.bind('F', 'hint all tab-bg')
config.bind('d', 'tab-close')
config.bind('.', 'tab-close')
config.bind('D', 'tab-close -o')
config.bind(',', 'tab-close -o')

#Tab Motion
config.bind('b', 'set-cmd-text -s :buffer')
config.bind('y', 'tab-next')
config.bind('l', 'tab-prev')

#Direction
config.bind('u', 'scroll up')
config.bind('e', 'scroll down')
config.bind('n', 'scroll left')
config.bind('i', 'scroll right')

config.bind('w', 'scroll up')
config.bind('r', 'scroll down')
config.bind('a', 'scroll left')
config.bind('s', 'scroll right')

#Time Motion
config.bind('N', 'back')
config.bind('I', 'forward')

#Page Motion
config.bind('j', 'scroll-page 0 -0.5')
config.bind('h', 'scroll-page 0 0.5')

#Search
config.bind('k', 'search-next')
config.bind('K', 'search-prev')

#yank
config.bind(';', 'yank')

#password
config.bind('gp', 'spawn --userscript qute-pass')

#spawn youtube link into mpv
config.bind('Y', 'hint links spawn mpv {hint-url}')

#spawn chromium for link
config.bind('C', 'spawn chromium {url}')

#Reload
config.bind('R', 'reload -f')

c.content.blocking.enabled = False

import sys, os

config.set(
    "content.blocking.adblock.lists",
    [
        #"https://easylist.to/easylist/easylist.txt",
        #"https://easylist.to/easylist/easyprivacy.txt",
        "https://easylist.to/easylist/fanboy-annoyance.txt",
        #"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
        #"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
        #"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
        #"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
        #"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
        #"https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",
        #"https://www.malwaredomainlist.com/hostslist/hosts.txt",
        #"https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=1&mimetype=plaintext",
        "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    ],
)

config.load_autoconfig()
