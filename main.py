import os
import shutil
import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandasgui import show
from tkinter import filedialog, ttk, Label, PhotoImage
import tkinter as tk
from utilities import create_custom_button
from PIL import Image, ImageTk

class FileUploader:
    def __init__(self, master):
        self.master = master
        ######################################################
        self.upload_frame = tk.Frame(self.master, bg='#ebebeb')
        self.upload_frame.grid(row=0, column=0, columnspan=2,padx=10, pady=10)
        ######################################################
        # giecar logo handling
        self.img = Image.open("./img/giecar.png")
        or_width, or_height = self.img.size
        self.img = self.img.resize((or_width//3, or_height//3))
        self.photo_img = ImageTk.PhotoImage(self.img)
        img_giecar = Label(self.upload_frame, image=self.photo_img, bg='#ebebeb')
        img_giecar.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.fname = tk.StringVar(self.master)
        self.fname.set("Selecione um arquivo")
        self.selected_file = tk.StringVar(self.master)

        # Texto inicial
        texto_inicial = "Importe e digite as informações do poço nos campos abaixo."
        self.label = tk.Label(self.upload_frame, text=texto_inicial, bg='#ebebeb')
        self.label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


        # Botão para carregar arquivo
        self.upload_button = create_custom_button(self.upload_frame,
                                           text="Carregar arquivo",
                                           command=self.upload_file,)
        # then the grid within the frame
        self.upload_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Label to display messages
        self.message_label = tk.Label(self.upload_frame, text="", bg='#ebebeb')
        self.message_label.grid(row=3, column=0, columnspan=2)

        # Dropdown menu to select file
        files = os.listdir("./uploads")
        if not files:
            files = ["Nenhum arquivo encontrado"]

        self.dropdown = tk.OptionMenu(self.upload_frame, self.fname, *files)
        self.dropdown.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = create_custom_button(self.upload_frame,
                                                "Visualizar arquivo",
                                                self.view_file)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.fname.trace_add('write', self.update_selected_file)

    def view_file(self):
        filename = self.selected_file.get()
        if os.path.exists(filename):
            df = pd.read_csv(filename, sep=";")
            show(df)
        else:
            self.messagebox.showerror("Error", "Arquivo não encontrado!")

    def upload_file(self):
        filename = filedialog.askopenfilename()
        print(filename)
        if not os.path.exists("./uploads"):
            os.makedirs("./uploads")
        shutil.copy(filename, "./uploads")
        self.message_label.config(text="Arquivo carregado com sucesso!")

    def update_selected_file(self, *args):
        self.selected_file.set(os.path.join("./uploads", self.fname.get()))

class WellInfoInput:
    def __init__(self, master, file_uploader):
        self.master = master
        self.file_uploader = file_uploader
        ######################################################
        self.well_info_frame = tk.Frame(self.master, bg='#ebebeb')
        self.well_info_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        ######################################################

        # Input do nome do poço
        tk.Label(self.well_info_frame, text="Digite o nome do poço: ", bg='#ebebeb') \
            .grid(row=0, columnspan=2, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.well_info_frame,
                                   borderwidth=1,
                                   width=45,
                                   justify="center",
                                   relief="solid")
        self.nome_entry.grid(row=1, columnspan=2, padx=10, pady=10)

        # Depth inputs
        tk.Label(self.well_info_frame, text="Prof. Inicial", bg='#ebebeb') \
            .grid(row=2, column=0, padx=10, pady=10)
        self.prof_min = tk.Entry(self.well_info_frame,
                                 borderwidth=1,
                                 width=18,
                                 justify="center",
                                 relief="solid")
        self.prof_min.grid(row=3, column=0, padx=10, pady=10)

        tk.Label(self.well_info_frame, text="Prof. Final", bg='#ebebeb') \
            .grid(row=4, column=0, padx=10, pady=10)
        self.prof_max = tk.Entry(self.well_info_frame,
                                 borderwidth=1,
                                 width=18,
                                 justify="center",
                                 relief="solid")
        self.prof_max.grid(row=5, column=0, padx=10, pady=10)

        # Other options
        tk.Label(self.well_info_frame, text="Mesa Rotativa*", bg='#ebebeb') \
            .grid(row=2, column=1, padx=10, pady=10)
        self.mesa_rot = tk.Entry(self.well_info_frame,
                                 borderwidth=1,
                                 width=18,
                                 justify="center",
                                 relief="solid")
        self.mesa_rot.grid(row=3, column=1, padx=10, pady=10)

        # Error message
        self.error_message = tk.StringVar(self.well_info_frame)
        self.error_label = tk.Label(self.well_info_frame,
                                    textvariable=self.error_message,
                                    fg="red")
        self.error_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        create_custom_button(root=self.well_info_frame,
                            text="Plotar",
                            command=self.plot_pressure)\
            .grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def plot_pressao(self, x, y, title, xlabel, ylabel, pressao_df, prof_min, prof_max, mesa_rot):
        """
        Função que plota a pressão de formação em função da profundidade (cota)
        """
        ymin = int(prof_min.get()) if prof_min.get() else min(pressao_df['Prof./Intv.(m)'])
        ymax = int(prof_max.get()) if prof_max.get() else max(pressao_df['Prof./Intv.(m)'])

        ymin = int(mesa_rot.get()) - ymin
        ymax = int(mesa_rot.get()) - ymax

        plt.plot(x, y, 'o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.ylim(ymin, ymax)
        plt.gca().invert_yaxis()
        plt.grid()
        plt.show()

    def plot_pressure(self):
        """
        Plota os dados de pressão em relação à profundidade.

        Esta função lê um arquivo CSV contendo dados de pressão e os plota em relação
        aos valores de profundidade (em cota) correspondentes.
        Elimina quaisquer linhas com valores NaN.
        Os valores de profundidade em cota são calculados subtraindo
        os valores de 'Prof./Intv.(m)' do valor de 'mesa_rot'.
        """
        try:
            filename = self.file_uploader.selected_file.get()
            pressao_df = pd.read_csv(filename, delimiter=';')
            pressao_df = pressao_df.dropna(subset=['Prof./Intv.(m)', 'Pressão de Formação (Kgf/cm2)'])
            prof_cota = int(self.mesa_rot.get()) - pressao_df['Prof./Intv.(m)']

            self.plot_pressao(x=pressao_df['Pressão de Formação (Kgf/cm2)'],
                        y=prof_cota,
                        title=self.nome_entry.get(),
                        xlabel='Pressão de Formação (Kgf/cm2)',
                        ylabel='Profundidade (m)',
                        pressao_df=pressao_df,
                        prof_min=self.prof_min,
                        prof_max=self.prof_max,
                        mesa_rot=self.mesa_rot)
        except Exception as e:
            self.error_message.set(str(e))

class Footer:
    def __init__(self, master):
        import webbrowser
        self.master = master
        self.footer_frame = tk.Frame(self.master, bg='#ebebeb')
        # Se eu quiser adicionar mais alguma coisa antes do footer
        # alterar o argumento row abaixo.
        self.footer_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        giecar_link = create_custom_button(self.footer_frame,
                                           text="GIECAR",
                                           command=lambda: \
                                           webbrowser.open("http://gcr.sites.uff.br/"),
                                           width=100)
        giecar_link.grid(row=0, column=0, padx=10, pady=10)

        github_link = create_custom_button(self.footer_frame,
                                           text="GitHub",
                                           command=lambda: \
                                           webbrowser.open("https://github.com/albano-a/GradPress"),
                                           width=100)
        github_link.grid(row=0, column=1, padx=10, pady=10)

        exit_button = create_custom_button(self.footer_frame,
                                           text="Sair",
                                           command=self.master.quit,
                                           width=100)
        exit_button.grid(row=0, column=2, padx=10, pady=10)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        self.geometry("600x720")
        self.minsize(600, 830)
        self.title("GradPress")
        self.iconbitmap(default="./icon.ico")  # icone
        self.option_add("*Label.font", "Helvetica 15")  # for the font

        # Determinação de um frame para centralizar o conteúdo da página
        self.main_frame = tk.Frame(self, bg='#ebebeb')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.file_uploader = FileUploader(self.main_frame)
        self.well_info_input = WellInfoInput(self.main_frame, self.file_uploader)
        self.footer = Footer(self.main_frame)




if __name__ == "__main__":
    app = App()
    app.mainloop()