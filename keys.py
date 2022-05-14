
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod =["mod4"]
mod_s = ["mod4", "shift"]
mod_c = ["mod4", "control"]

Browser = "firefox"
Terminal = "alacritty"

Left = "h"
Up = "j"
Down = "k"
Right = "l"

groups = ["1","2","3","4","5","6","7","8","9"]

class Keybindings:
   
    keys = [] 

    def focus_keys(self):

        layout_left = Key(mod, Left, lazy.layout.left())
        layout_up = Key(mod, Up, lazy.layout.up())
        layout_down = Key(mod, Down, lazy.layout.down())
        layout_right = Key(mod, Right, lazy.layout.right())

        self.keys += [layout_left, layout_up, layout_down, layout_right]

    def swap_keys(self):

        left = Key(mod_s, Left, lazy.layout.swap_left())
        up = Key(mod_s, Up, lazy.layout.swap_up())
        down = Key(mod_s, Down, lazy.layout.swap_down())
        right = Key(mod_s, Right, lazy.layout.swap_right())

        self.keys += [left, up, down, right]

    def shutdown_keys(self):

        shutdown = Key(mod_c, "x", lazy.shutdown())
        restart = Key(mod_c, "r", lazy.restart())
        kill = Key(mod, "q", lazy.window.kill())

        self.keys += [shutdown, restart, kill]

    def floating_keys(self):

        floating = Key(mod_s, "space", lazy.window.toggle_floating())
        full = Key(mod_s, "c", lazy.window.toggle_fullscreen())

        self.keys += [floating, full]

    def spawn_keys(self):
        
        Term = Key(mod, "Return", lazy.spawn(Terminal))
        Browse = Key(mod, "i", lazy.spawn(Browser))
        Rofi = Key(mod, "d", lazy.spawn("rofi -show run"))
        Spotify = Key(mod, "p", lazy.spawn("Spotify"))
        Snes9x = Key(mod, "u", lazy.spawn("snes9x-gtk"))
        obs = Key(mod, "o", lazy.spawn("obs"))
        screenshot = Key(mod_s, "s", lazy.spawn("flameshot gui"))
        
        self.keys += [Term, Browse, Rofi, Spotify, Snes9x, obs, screenshot]

    def groups_keys(self):
        
        group_keys = [] 

        for i in groups:
            group_keys += [Key(mod, i, lazy.group[i].toscreen()), Key(mod_s, i, lazy.window.togroup(i, switch_group=True))]

            return group_keys

    def init_keys(self):

        self.focus_keys()
        self.swap_keys()
        self.shutdown_keys()
        self.floating_keys()
        self.spawn_keys()

        return self.keys


