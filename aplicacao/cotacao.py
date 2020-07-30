# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# obs este conversor não utiliza a cotação atual. cotação do dia 22/07/2020
# este processo será introduzido em uma versão futura;

import os
import sys
from pathlib import Path
from os.path import join, dirname
import gettext
import locale
import configparser
import logging
import tkinter as tk
from sys import platform
import requests
import json
from tkinter import ttk
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import filedialog as fdlg
from tkinter import messagebox as tkmsg
from tkinter import font


class Projeto:
    def __init__(self, **kw):
        self.root = tk.Tk()
        self.root.title('Conversor de Moedas')
        #self.root.geometry('800x600')
        self.create_menu()
        self.create_canvas_area()


    def create_canvas_area(self):
        moedas = ['USD - Dólar Comercial',
        'USDT - Dólar Turismo',
        'CAD - Dólar Canadense',
        'AUD - Dólar Australiano',
        'EUR - Euro',
        'GBP - Libra Esterlina',
        'ARS - Peso Argentino',
        'JPY - Iene Japonês',
        'CHF - Franco Suíço',
        'CNY - Yuan Chinês',
        'ILS - Novo Shekel Israelense',
        'BTC - Bitcoin',
        'LTC - Litecoin',
        'ETH - Ethereum',
        'XRP - Ripple']

        self.mainframe = ttk.Frame(self.root)
        # label frame 1
        lblframe_1 = tk.LabelFrame(self.mainframe,
                                   text='Moeda',
                                   bd=3,
                                   padx=5,
                                   pady=5,
                                   background='#80b3b3')
        lblframe_1.pack(padx=10, pady=10)

        # combobox 1
        self.combo_1 = ttk.Combobox(lblframe_1, width=25, values=moedas, state='readonly')
        self.combo_1.grid(row=0, column=0, padx=10, pady=10)

        # frame 1
        frame_1 = tk.Frame(self.mainframe, padx=5, pady=5)
        frame_1.pack(padx=5, pady=5)

        # botão 1
        btn_1 = tk.Button(frame_1, text='Cotar', command=self.cotar, padx=5, pady=5, width=10)
        btn_1.grid(row=0, column=0, padx=5, pady=5)

        # botão 2
        btn_2 = tk.Button(frame_1, text='Apagar', command=self.apagar, padx=5, pady=5, width=10)
        btn_2.grid(row=0, column=1, padx=5, pady=5)

        # frame 2
        frame_2 = tk.Frame(self.mainframe, padx=5, pady=5)
        frame_2.pack(padx=5, pady=5)

        self.cotacao = tk.StringVar()
        label_1 = tk.Label(frame_2, textvariable=self.cotacao)
        label_1.pack(padx=5, pady=5)

        self.cotacao2 = tk.StringVar()
        self.label_2 = tk.Label(frame_2, textvariable=self.cotacao2)
        self.label_2.pack(padx=5, pady=5)


        self.mainframe.pack()

    def cotar(self):
        self.req = requests.get('https://economia.awesomeapi.com.br/all')
        self.cot = self.req.json()
        self.mostrar()

    def mostrar(self):
        moeda = self.combo_1.get()
        if moeda == 'USD - Dólar Comercial':
            self.cotacao.set(f'Moeda: {self.cot["USD"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["USD"]["bid"]}')

        elif moeda == 'USDT - Dólar Turismo':
            self.cotacao.set(f'Moeda: {self.cot["USDT"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["USDT"]["bid"]}')

        elif moeda == 'CAD - Dólar Canadense':
            self.cotacao.set(f'Moeda: {self.cot["CAD"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["CAD"]["bid"]}')

        elif moeda == 'EUR - Euro':
            self.cotacao.set(f'Moeda: {self.cot["EUR"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["EUR"]["bid"]}')

        elif moeda == 'GBP - Libra Esterlina':
            self.cotacao.set(f'Moeda: {self.cot["GBP"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["GBP"]["bid"]}')

        elif moeda == 'ARS - Peso Argentino':
            self.cotacao.set(f'Moeda: {self.cot["ARS"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["ARS"]["bid"]}')

        elif moeda == 'BTC - Bitcoin':
            self.cotacao.set(f'Moeda: {self.cot["BTC"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["BTC"]["bid"]}')

        elif moeda == 'LTC - Litecoin':
            self.cotacao.set(f'Moeda: {self.cot["LTC"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["LTC"]["bid"]}')

        elif moeda == 'JPY - Iene Japonês':
            self.cotacao.set(f'Moeda: {self.cot["JPY"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["JPY"]["bid"]}')

        elif moeda == 'CHF - Franco Suíço':
            self.cotacao.set(f'Moeda: {self.cot["CHF"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["CHF"]["bid"]}')

        elif moeda == 'AUD - Dólar Australiano':
            self.cotacao.set(f'Moeda: {self.cot["AUD"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["AUD"]["bid"]}')

        elif moeda == 'CNY - Yuan Chinês':
            self.cotacao.set(f'Moeda: {self.cot["CNY"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["CNY"]["bid"]}')

        elif moeda == 'ILS - Novo Shekel Israelense':
            self.cotacao.set(f'Moeda: {self.cot["ILS"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["ILS"]["bid"]}')

        elif moeda == 'ETH - Ethereum':
            self.cotacao.set(f'Moeda: {self.cot["ETH"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["ETH"]["bid"]}')

        elif moeda == 'XRP - Ripple':
            self.cotacao.set(f'Moeda: {self.cot["XRP"]["name"]}')
            self.cotacao2.set(f'Valor atual: R$ {self.cot["XRP"]["bid"]}')

    def apagar(self):
        self.cotacao.set('')
        self.cotacao2.set('')

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        self.file_menu = tk.Menu(menu_bar, tearoff=0)
        self.file_menu.add_command(label=('Sair'), command=self.exit_software)
        menu_bar.add_cascade(label=('Arquivo'), menu=self.file_menu)


        self.root.config(menu=menu_bar)

    def exit_software(self):
        self.root.quit()

    def execute(self):
        self.root.mainloop()

def main(args):
    app = Projeto()
    app.execute()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))