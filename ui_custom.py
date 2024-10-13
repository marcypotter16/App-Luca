from UI.Abstract import UICanvas
from UI.Button import TextButton
from UI.Containers import HorizContainer, VertContainer
from UI.Entry import Entry, Paragraph
from UI.Label import Label
from Utils.Colors import *


import pygame as p

BUTTON_HEIGHT = 30
BUTTON_WIDTH = 100
BUTTON_CONTAINER_PADDING = (10, 10)

class CellInputInterface:
    def __init__(self, game, rect: p.Rect, on_close = None) -> None:
        self.game = game
        self.rect = rect
        padding = (20, 20)
        self.canvas = UICanvas(game)
        self.canvas.rect = rect
        self.on_close = on_close
        self.visible = True
        self.action = None
        self.hc = HorizContainer(self.canvas, 
                                 font=game.font_small,
                                 width=rect.w, 
                                 height=rect.h - BUTTON_HEIGHT - BUTTON_CONTAINER_PADDING[1] * 2, 
                                 bg_color=DARK_10, 
                                 corner_radius=0, 
                                 pad=padding)
        self.vcr = VertContainer(self.canvas, 
                                 font=game.font_small,
                                 width=rect.w * .5 - padding[0] * 2, 
                                 height=self.hc.height - self.hc.pad[1], 
                                 bg_color=DARK_10,
                                 corner_radius=0, 
                                 pad=(0, 5))
        self.vcl = VertContainer(self.canvas, 
                                 font=game.font_small,
                                 width=rect.w * .5 - padding[0] * 2, 
                                 height=self.hc.height - self.hc.pad[1],
                                 bg_color=DARK_10,
                                 corner_radius=0, 
                                 pad=(0, 5))
        # self.vcl.rect.update(rect.top, rect.left, 
        #                      rect.w * .5, rect.h)
        # self.vcr.rect.update(rect.top + rect.w * .5,
        #                      rect.left, rect.w * .5, self.vcr.height)
        # self.hc.rect.update(rect)

        H = game.font_small.get_height() + 10

        # Labels and entries
        nome_label = Label(self.canvas, height=H, text="Nome",
                           fg_color=WHITE, font=game.font_small, corner_radius=0)

        self.nome_entry = Entry(self.canvas, height=H, bg_color=(
            40, 40, 40), font=game.font_small, fg_color=LIGHT, corner_radius=0)

        tipo_label = Label(self.canvas, height=H, text="Tipo",
                           fg_color=WHITE, font=game.font_small, corner_radius=0)

        self.tipo_entry = Entry(self.canvas, height=H, bg_color=(
            40, 40, 40), font=game.font_small, fg_color=LIGHT, corner_radius=0)

        data_label = Label(self.canvas, height=H, text="Data",
                           fg_color=WHITE, font=game.font_small, corner_radius=0)

        self.data_entry = Entry(self.canvas, height=H, bg_color=(
            40, 40, 40), font=game.font_small, fg_color=LIGHT, corner_radius=0)

        descrizione_label = Label(self.canvas, height=H, text="Descrizione",
                                  fg_color=WHITE, font=game.font_small, corner_radius=0)

        # Button
        ok_button = TextButton(self.canvas, 
                                text="Inserisci", 
                                width=BUTTON_WIDTH,
                                height=BUTTON_HEIGHT,
                                bg_color=DARK_10,
                                fg_color=LIGHT_GREEN, 
                                hover_color=DARK,
                                font=game.font_small, 
                                corner_radius=0, 
                                command=self.close)
        annulla_button = TextButton(self.canvas, 
                                    text="Annulla", 
                                    width=BUTTON_WIDTH,
                                    height=BUTTON_HEIGHT,
                                    bg_color=DARK_10,
                                    fg_color=ACCENT, 
                                    hover_color=DARK,
                                    font=game.font_small, 
                                    corner_radius=0, 
                                    command=self.cancel)

        self.canvas.add_child(self.hc)
        self.hc.x, self.hc.y = self.rect.topleft + p.Vector2(padding) * .5

        # self.hc.add_child(self.vcl)
        self.hc.modify_children_dimensions_to_fit = False
        self.hc.add_child(self.vcl) #!!!!!!!!!! bug
        self.hc.add_child(self.vcr)

        self.vcl.add_child(nome_label)
        self.vcl.add_child(self.nome_entry)
        self.vcl.add_child(tipo_label)
        self.vcl.add_child(self.tipo_entry)
        self.vcl.add_child(data_label)
        self.vcl.add_child(self.data_entry)

        self.vcr.add_child(descrizione_label)
        self.descrizione_entry = Paragraph(self.canvas, 
                                           height=self.data_entry.rect.bottom - self.nome_entry.rect.top,
                                           bg_color=LIGHT, 
                                           fg_color=LIGHT, 
                                           focus_color=WHITE,
                                           font=game.font_small, 
                                           corner_radius=0)
        self.vcr.add_child(self.descrizione_entry)
        

        self.button_container = HorizContainer(self.canvas,
                                            center=(self.rect.centerx, 
                                                    self.rect.bottom - BUTTON_HEIGHT * .5 - BUTTON_CONTAINER_PADDING[1] * .5),
                                            width=2*BUTTON_WIDTH + BUTTON_CONTAINER_PADDING[0],
                                            height=BUTTON_HEIGHT + BUTTON_CONTAINER_PADDING[1],
                                            bg_color="transparent",
                                            corner_radius=0,
                                            pad=BUTTON_CONTAINER_PADDING)
        self.button_container.add_child(ok_button)
        self.button_container.add_child(annulla_button)

        # self.vcl.height = self.vcl.rect.h = rect.h - self.button_container.rect.h
        # self.vcr.height = self.vcr.rect.h = rect.h - self.button_container.rect.h

    def render(self, surf):
        if self.canvas.visible:
            p.draw.rect(surf, DARK, self.rect, width=2)
            self.hc.render(surf)
            self.button_container.render(surf)

    def update(self, dt):
        if self.canvas.visible:
            self.hc.update(dt)
            self.button_container.update(dt)

    def toggle_visibility(self):
        self.canvas.toggle_visibility()
        self.visible = self.canvas.visible

    def reset(self):
        self.nome_entry.text = ""
        self.tipo_entry.text = ""
        self.data_entry.text = ""
        self.descrizione_entry.text = ""

    def close(self):
        if not self.action:
            self.action = "close"
        if self.on_close is not None:
            self.on_close()
        self.toggle_visibility()
        self.reset()

    def cancel(self):
        self.action = "cancel"
        self.close()

        