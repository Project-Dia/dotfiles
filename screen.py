
import os
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen


color_alert = "AB82FF"
color_quiet = "D5C0FF"
fg = "105253"
bg = "f0e5fa55"

#Set paddng of Sep widget

sep_pad = 2

class MyBear:
    


    def widgets_bar(self):

        widgets_list = [
            widget.GroupBox(
                #font = "Hack",
                #fontsize = 14,
                #margin = 3,
                #padding_y = 5,
                #padding_x = 3,
                #borderwidth = 3,
                #active = color_alert,
                #inactive = color_quiet,
                #rounded = "false",
                #foreground = fg
                ),
            widget.Sep(
                #foreground = fg,
                #background= bg,
                #linewidth = 1,
                #size_percent = 100,
                #padding = sep_pad,
                ),
            widget.windowName(
                #foreground = fg,
                background = bg,
                ),
            widget.Sep(
                #foreground = fg,
                #background = bg,
                #linewidth = 1,
                #size_percent = 100,
                #padding = sep_pad,
                ),
           # widget.Cmus(
               # foreground = fg,
               # background = bg,
               # noplay_color = bg,
               # play_color = fg,
               # ),
            widget.Spacer(
                ),
            widget.Chord(
                #foreground = fg,
                #background = bg,
                ),
            widget.Clock(
                #foreground = fg,
                background = bg,
                format = '%m/%d/%y %H:%M',
                ),
            widget.Sep(
                #foreground = fg,
                #background = bg,
                #linewidth = 1,
                #size_percent = 100,
                #padding = sep_pad
                ),
           widget.NetGraph(
                #fill_color = fg,
                #background = bg,
                #type = line,
                #line_width = 2,
                ),
           widget.Sep(
                #foreground = fg,
                #background = bg,
                #linewidth = 1, 
                #size_percent = 100,
                #padding = sep_pad,
                ),
           widget.Memory(
                #foreground = fg,
                #background = bg,
                #measure_mem = G,
                ),
           widget.Sep(
                #foreground = fg, 
                #background = bg,
                #linewidth = 1,
                #size_percent = 100,
                #padding = sep_pad,
                ),
           widget.CPU(
                #foreground = fg,
                #background = bg,
                ),
           widget.Sep(
                #foreground = fg,
                #background = bg,
                #linewidth = 1, 
                #size_percent = 100,
                #padding = sep_pad,
                ),
           widget.Volume(
                #foreground = fg,
                #background = bg,
                #fmt = 'Vol: {}',
                #step = 5,
                ),
           ]
        return widgets_list

    def scream(self):
        widgets_screen = self.widgets_bar()
        return widgets_screen

    def bear(self):
        return [Screen(top=bar.Bar([
            widget.GroupBox(
                font = "Hack",
                fontsize = 14,
                margin = 3,
                padding_y = 5,
                padding_x = 3,
                borderwidth = 3,
                active = color_alert,
                inactive = color_quiet,
                rounded = "false",
                foreground = fg,
                background = bg,
                ),
            widget.Sep(
                foreground = fg,
                #background= bg,
                linewidth = 1,
                size_percent = 100,
                padding = sep_pad,
                ),
            widget.WindowName(
                foreground = fg,
                background = bg,
                padding = 3,
                ),
           # widget.Sep(
           #     foreground = fg,
           #     #background = bg,
           #     linewidth = 1,
           #     size_percent = 100,
           #     padding = sep_pad,
           #     ),
            widget.Cmus(
                foreground = fg,
                #background = bg,
                noplay_color = bg,
                play_color = fg,
                ),
            widget.Spacer(
                background = bg,
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
                #background = bg,
                linewidth = 1,
                size_percent = 100,
                padding = sep_pad
                ),
           widget.NetGraph(
                fill_color = fg,
                background = bg,
                type = "line",
                line_width = 2,
                ),
           widget.Sep(
                foreground = fg,
                #background = bg,
                linewidth = 1, 
                size_percent = 100,
                padding = sep_pad,
                ),
           widget.Memory(
                foreground = fg,
                background = bg,
                measure_mem = "G",
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
                #background = bg,
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
	],size = 24, background = ["5151dc33","7b7be433"]))]
       # return [Screen(top=bar.Bar([widget.CurrentLayout(), widget.GroupBox()],24,),),]

