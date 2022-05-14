
import os
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen


color_active = "ab82ff"
color_inactive = "d5coff"
fg = "333333"
bg = color_inactive

#Set padding of Sep widget

sep_pad = 5

class MyBar:
    
    def widgets_bar(self):

        widgets_list = [
            widget.GroupBox(
                font = "Hack",
                fontsize = 14,
                margin = 3,
                padding_y = 5,
                padding_x = 3,
                borderwidth = 3,
                active = color_active,
                inactvie = color_inactive,
                rounded = false,
                foreground = fg
                ),

            widget.Sep(
                foreground = fg,
                background= bg,
                linewidth = 1,
                size_percent = 100,
                padding = sep_pad,
                ),

            widget.windowName(
                foreground = fg,
                background = bg,
                ),

            widget.Sep(
                foreground = fg,
                background = bg,
                linewidth = 1,
                size_percent = 100,
                padding = sep_pad,
                ),

            widget.Cmus(
                foreground = fg,
                background = bg,
                noplay_color = bg,
                play_color = fg,
                ),

            widget.Spacer(
                background = bg,
                length = STRETCH,
                ),

            widget.Chord(
                foreground = fg,
                background = bg,
                ),

            widget.Clock(
                foreground = fg,
                background = bg,
                format = '%m/%d/%y %H:%M',
                ),

            widget.Sep(
                foreground = fg,
                background = bg,
                linewidth = 1,
                size_percent = 100,
                padding = sep_pad
                ),

           widget.NetGraph(
                fill_color = fg,
                background = bg,
                type = line,
                line_width = 2,
                ),

           widget.Sep(
                foreground = fg,
                background = bg,
                linewidth = 1, 
                size_percent = 100,
                padding = sep_pad,
                ),

           widget.Memory(
                foreground = fg,
                background = bg,
                measure_mem = G,
                ),

           widget.Sep(
                foreground = fg, 
                background = bg,
                linewidth = 1,
                size_percent = 100,
                padding = sep_pad,
                ),

           widget.CPU(
                foreground = fg,
                background = bg,
                ),

           widget.Sep(
                   foreground = fg,
                   background = bg,
                   linewidth = 1, 
                   size_percent = 100,
                   padding = sep_pad,
                   ),
           widget.Volume(
                   foreground = fg,
                   background = bg,
                   fmt = 'Vol: {}',
                   step = 5,
                   ),
           ]
        return widget_list

    def screen:
        widgets_screen = self.widgets_bar()
        return widgets_screen

    def bar
        return Screen(top = bar.Bar(widgets=self.screen(), opacity = .7, size 20, background = bg))

