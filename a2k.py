# a2k
# Version: 0.91 beta
# Rename files using Python and regular expressions with ease.
# Originally titled Anime-to-Kodi.

import tkinter as tk
from tkinter import ttk


class PathFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.configure(background='lightgrey')

        path_label = ttk.Label(self, text='Directory Path:',
                               background='lightgrey')
        path_entry = ttk.Entry(self, font=('Arial', 12))
        path_select_button = ttk.Button(self, text='Select', width=8)

        path_label.pack(anchor='w')
        path_entry.pack(side='left', anchor='n', expand=1, fill='x')
        path_select_button.pack(side='right', anchor='n', padx=(5, 0))


class TypeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.configure(background='lightgrey')

        mchkvar = tk.IntVar()
        pchkvar = tk.IntVar()
        vchkvar = tk.IntVar()
        # Why is it necessary to assign value?
        vchkvar = 1

        type_label = ttk.Label(self, text='File Type:', background='lightgrey')
        music_chkbox = tk.Checkbutton(self, text='Music',
                                      background='lightgrey', variable=mchkvar)
        photo_chkbox = tk.Checkbutton(self, text='Photo',
                                      background='lightgrey', variable=pchkvar)
        video_chkbox = tk.Checkbutton(self, text='Video',
                                      background='lightgrey', variable=vchkvar)
        video_chkbox.select()
        custom_label = ttk.Label(self, text='Custom', background='lightgrey')
        custom_entry = ttk.Entry(self, font=('Arial', 10))
        help_type_button = ttk.Button(self, text='?', width=2)

        type_label.grid(row=0, column=0, padx=5)
        music_chkbox.grid(row=0, column=1, padx=5)
        photo_chkbox.grid(row=0, column=2, padx=5)
        video_chkbox.grid(row=0, column=3, padx=5)
        custom_label.grid(row=0, column=4, padx=(15, 5))
        custom_entry.grid(row=0, column=5, padx=5)
        help_type_button.grid(row=0, column=6)


class FilesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.configure(background='lightgrey')

        files_label = ttk.Label(self, text='Current Files',
                                background='lightgrey')
        files_list = tk.Listbox(self, font=('Arial', 12))
        rename_label = ttk.Label(self, text='Renamed Files',
                                 background='lightgrey')
        rename_list = tk.Listbox(self, font=('Arial', 12))

        files_label.grid(row=0, column=0, sticky='n')
        rename_label.grid(row=0, column=1, sticky='n')
        files_list.grid(row=1, column=0, sticky='nesw', padx=(0, 5))
        rename_list.grid(row=1, column=1, sticky='nesw')


class RegexFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.configure(background='lightgrey')

        regex_label = ttk.Label(self, text='Regex:', background='lightgrey',
                                width=8)
        regex_entry = ttk.Entry(self, font=('Arial', 12))
        clear_button = ttk.Button(self, text='Clear', width=8)

        regex_label.pack(side='left', anchor='nw')
        regex_entry.pack(side='left', anchor='n', expand=1, fill='x',
                         padx=(0, 5))
        clear_button.pack()


class RenameFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.configure(background='lightgrey')

        rename_label = ttk.Label(self, text='Rename:', background='lightgrey',
                                 width=8)
        rename_entry = ttk.Entry(self, font=('Arial', 12))
        test_button = ttk.Button(self, text='Test', width=8)

        rename_label.pack(side='left', anchor='sw')
        rename_entry.pack(side='left', anchor='n', expand=1, fill='x',
                          padx=(0, 5))
        test_button.pack()


class RegexCalcFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.configure(background='lightgrey')

        calc_button01 = ttk.Button(self, text='\\b+', width=4)
        calc_button02 = ttk.Button(self, text='\d+', width=4)
        calc_button03 = ttk.Button(self, text='\s+', width=4)
        calc_button04 = ttk.Button(self, text='\w+', width=4)
        calc_button05 = ttk.Button(self, text='.*', width=4)
        calc_button06 = ttk.Button(self, text='\B+', width=4)
        calc_button07 = ttk.Button(self, text='\D+', width=4)
        calc_button08 = ttk.Button(self, text='\S+', width=4)
        calc_button09 = ttk.Button(self, text='\W+', width=4)
        calc_button10 = ttk.Button(self, text='Ep.', width=4)
        calc_button11 = ttk.Button(self, text='C1', width=4)
        calc_button12 = ttk.Button(self, text='C2', width=4)
        calc_button13 = ttk.Button(self, text='C3', width=4)
        calc_button14 = ttk.Button(self, text='C4', width=4)
        calc_button15 = ttk.Button(self, text='C5', width=4)
        # calc_button16 = ttk.Button(self, text='b16', width=4)
        # calc_button17 = ttk.Button(self, text='b17', width=4)
        # calc_button18 = ttk.Button(self, text='b18', width=4)
        # calc_button19 = ttk.Button(self, text='b19', width=4)
        # calc_button20 = ttk.Button(self, text='b20', width=4)
        calc_help_button = ttk.Button(self, text='?', width=2)

        calc_button01.grid(row=0, column=1, padx=2)
        calc_button02.grid(row=0, column=2, padx=2)
        calc_button03.grid(row=0, column=3, padx=2)
        calc_button04.grid(row=0, column=4, padx=2)
        calc_button05.grid(row=0, column=5, padx=2)
        calc_help_button.grid(row=0, column=6, padx=2)

        calc_button06.grid(row=1, column=1, padx=2)
        calc_button07.grid(row=1, column=2, padx=2)
        calc_button08.grid(row=1, column=3, padx=2)
        calc_button09.grid(row=1, column=4, padx=2)
        calc_button10.grid(row=1, column=5, padx=2)

        calc_button11.grid(row=2, column=1, padx=2)
        calc_button12.grid(row=2, column=2, padx=2)
        calc_button13.grid(row=2, column=3, padx=2)
        calc_button14.grid(row=2, column=4, padx=2)
        calc_button15.grid(row=2, column=5, padx=2)

        # calc_button16.grid(row=3, column=1, padx=2)
        # calc_button17.grid(row=3, column=2, padx=2)
        # calc_button18.grid(row=3, column=3, padx=2)
        # calc_button19.grid(row=3, column=4, padx=2)
        # calc_button20.grid(row=3, column=5, padx=2)


class ExecuteFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        execute_button = ttk.Button(self, text='Execute', width=8)
        execute_button.pack(side='right', anchor='w')
        self.configure(background='lightgrey')


class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        frame_section01 = PathFrame(root)
        frame_section02 = TypeFrame(root)
        frame_section03 = FilesFrame(root)
        frame_section04 = RegexFrame(root)
        frame_section05 = RenameFrame(root)
        frame_section06 = RegexCalcFrame(root)
        frame_section07 = ExecuteFrame(root)

        frame_section01.grid(row=0, column=0, sticky='new', padx=5, pady=5)
        frame_section02.grid(row=1, column=0, sticky='new', padx=5, pady=5)
        frame_section03.grid(row=2, column=0, sticky='nesw', padx=5, pady=5)
        frame_section04.grid(row=3, column=0, sticky='new', padx=5,
                             pady=(5, 0))
        frame_section05.grid(row=4, column=0, sticky='new', padx=5,
                             pady=(0, 5))
        frame_section06.grid(row=5, column=0, padx=5, pady=5)
        frame_section07.grid(row=6, column=0, sticky='new', padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('a2k')
    root.geometry('640x480+100+100')
    root.configure(background='lightgrey')
    Main(root).grid(sticky="nsew")
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()
