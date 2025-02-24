# Importando as bibliotecas
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import customtkinter as ctk
from PIL import Image
import pandas as pd


# Importando arquivo view
from view import *
  


# Variáveis de cores
color_0 = "#f0f3f5"  # Preta
color_1 = "#feffff"  # branca
color_2 = "#F9040B"  # vermelha
color_3 = "#38576b"  # valor
color_4 = "#403d3d"   # letra
color_5 = "#e06636"   # - profit
color_6 = "#0278d9"   # azul
color_7 = "#cf1318"   # + vermelha
color_8 = "#09b341"  # verde
color_9 = "#e9edf5"   # sky blue
color_10 = "#099e0e"   # + verde

# Transformando a variável table, da tabela, numa variável global
global table

# Funções de CRUD e Excel exceto a de mostrar/read, que está mais abaixo no código
# Função do botão cadastrar
def register_btn_function():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    birth_date_iso = date_entry.get_date()  # Obtém a data no formato padrão (datetime.date)
    birth_date = birth_date_iso.strftime("%d/%m/%Y")  # Converte para o formato brasileiro
    age = age_entry.get()
    belt = belt_entry.get()

    info_list = [name, email, phone, birth_date, age, belt]

    if name == '':
        messagebox.showerror("Erro!", "O nome não foi preenchido!")
    else:
        create(info_list)
        messagebox.showinfo("Sucesso!", "Aluno cadastrado com sucesso!")

        # Apagando os dados digitados no entry, após inserir a informação
        name_entry.delete(0, "end")
        email_entry.delete(0, "end")
        phone_entry.delete(0, "end")
        date_entry.delete(0, "end")
        age_entry.delete(0, "end")
        belt_entry.delete(0, "end")
    
    for widget in right_frame.winfo_children():
        widget.destroy()

    show_table()

# Função do botão atualizar
def update_btn_function():
    try:
        table_data = table.focus()
        table_data_dict = table.item(table_data)
        table_data_list = table_data_dict['values']

        id = table_data_list[0]

        name_entry.delete(0, "end")
        email_entry.delete(0, "end")
        phone_entry.delete(0, "end")
        date_entry.delete(0, "end")
        age_entry.delete(0, "end")
        belt_entry.delete(0, "end")

        name_entry.insert(0, table_data_list[1])
        email_entry.insert(0, table_data_list[2])
        phone_entry.insert(0, table_data_list[3])
        date_entry.insert(0, table_data_list[4])
        age_entry.insert(0, table_data_list[5])
        belt_entry.insert(0, table_data_list[6])

        def update_info():
            name = name_entry.get()
            email = email_entry.get()
            phone = phone_entry.get()
            birth_date_iso = date_entry.get_date()  # Obtém a data no formato padrão (datetime.date)
            birth_date = birth_date_iso.strftime("%d/%m/%Y")
            age = age_entry.get()
            belt = belt_entry.get()

            info_list = [name, email, phone, birth_date, age, belt, id]

            if name == '':
                messagebox.showerror("Erro!", "O nome não foi preenchido!")
            else:
                update(info_list)
                messagebox.showinfo("Sucesso!", "Dados atualizados com sucesso!")

                # Apagando os dados digitados no entry, após inserir a informação
                name_entry.delete(0, "end")
                email_entry.delete(0, "end")
                phone_entry.delete(0, "end")
                date_entry.delete(0, "end")
                age_entry.delete(0, "end")
                belt_entry.delete(0, "end")
            
            show_table()

        # Botão para confirmar
        confirm_button = ctk.CTkButton(bottom_frame, 
                                text="Confirmar", 
                                width=40, height=20, 
                                fg_color=color_8, 
                                text_color=color_1, 
                                hover_color=color_10,
                                font=("Ivy", 10, "bold"), 
                                cursor = "hand2",
                                command=update_info
                                )
        confirm_button.place(x=105, y=375)


    except IndexError:
        messagebox.showerror("Erro!", "Selecione um registro da tabela!")

# Função do botão deletar
def delete_btn_function():
    try:
        table_data = table.focus()
        table_data_dict = table.item(table_data)
        table_data_list = table_data_dict['values']

        id = [table_data_list[0]]

        delete(id)

        messagebox.showinfo("Sucesso!", "Aluno deletado com sucesso!")

        show_table()

    except IndexError:
        messagebox.showerror("Erro!", "Selecione um aluno para removê-lo!")


# Função do botão de exportar para arquivo Excel
def export_to_excel():
    table_data = read()

    columns = ["ID", "Nome", "E-mail", "Telefone", "Data de Nascimento", "Idade", "Faixa"]

    df = pd.DataFrame(table_data, columns=columns)

    path = "alunos_cadastrados.xlsx"
    
    df.to_excel(path, index=False)

    messagebox.showinfo("Sucesso!", f"Tabela exportada para {path} com sucesso!")


# Criação da janela e definição de suas propriedades
ctk.set_appearance_mode("Light") # "System" (padrão), "Dark" ou "Light"
ctk.set_default_color_theme("blue") # Temas disponíveis: "blue", "green", "dark-blue"
window = ctk.CTk()
window.title("Raggio BJJ")
window.geometry("1043x453")
window.configure(fg_color=color_9)
window.iconbitmap("assets/raggio_icon.ico")
window.resizable(width=False, height=False)

# Configurando o layout da janela para permitir expansão
window.grid_columnconfigure(0, weight=1) # Coluna da esquerda (top_frame e bottom_frame)
window.grid_columnconfigure(1, weight=3) # Coluna da direita (right_frame)
window.grid_rowconfigure(0, weight=0) # Linha do top_frame
window.grid_rowconfigure(1, weight=1) # Linha do bottom_frame e right_frame

# Dividindo a janela com frames
top_frame = ctk.CTkFrame(window,
                          width=310,
                          height=50,
                          fg_color=color_2,
                          border_width=0, 
                          corner_radius=0
)
top_frame.grid(row=0, column=0, sticky="NSEW")

bottom_frame = ctk.CTkFrame(window,
                          width=310,
                          height=403,
                          fg_color=color_1,
                          border_width=0, 
                          corner_radius=0
                          )
bottom_frame.grid(row=1, column=0, padx=0, pady=1, sticky="NSEW")

right_frame = ctk.CTkFrame(window,
                          fg_color=color_1,
                          border_width=0, 
                          corner_radius=0
                          )
right_frame.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky="NSEW")

# Configurando o layout dentro do right_frame para expandir a tabela
right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_rowconfigure(0, weight=1)


# Label do frame de cima
top_label = ctk.CTkLabel(top_frame, 
                         text="Cadastro de Alunos", 
                         fg_color=color_2,
                         text_color=color_1,
                         font=("Ivy", 15, "bold"),
                         anchor="nw"
                         )
top_label.place(x=10, y=20)

# Configurando frame de baixo

# Nome
name_label = ctk.CTkLabel(bottom_frame,
                          text="Nome *",
                          fg_color=color_1,
                          text_color=color_4,
                          font=("Ivy", 13, "bold"),
                          anchor="nw"
                          )
name_label.place(x=10, y=10)

name_entry = ctk.CTkEntry(bottom_frame, width=280, height=20, font=("Ivy", 13), corner_radius=1)
name_entry.place(x=10, y=40)

# E-mail
email_label = ctk.CTkLabel(bottom_frame,
                          text="E-mail *",
                          fg_color=color_1,
                          text_color=color_4,
                          font=("Ivy", 13, "bold"),
                          anchor="nw"
                          )
email_label.place(x=10, y=70)

email_entry = ctk.CTkEntry(bottom_frame, width=280, height=20, font=("Ivy", 13), corner_radius=1)
email_entry.place(x=10, y=100)

# Telefone
phone_label = ctk.CTkLabel(bottom_frame,
                          text="Telefone *",
                          fg_color=color_1,
                          text_color=color_4,
                          font=("Ivy", 13, "bold"),
                          anchor="nw"
                          )
phone_label.place(x=10, y=130)

phone_entry = ctk.CTkEntry(bottom_frame, width=280, height=20, font=("Ivy", 13), corner_radius=1)
phone_entry.place(x=10, y=160)

# Data da Consulta
date_label = ctk.CTkLabel(bottom_frame,
                          text="Data de Nascimento *",
                          fg_color=color_1,
                          text_color=color_4,
                          font=("Ivy", 13, "bold"),
                          anchor="nw"
                          )
date_label.place(x=10, y=200)

date_entry = DateEntry(bottom_frame, width=12, background=color_2, foreground="white", borderwidth=4, font=("Ivy", 12))
date_entry.place(x=15, y=280)

# Estado da Consulta
age_label = ctk.CTkLabel(bottom_frame,
                            text="Idade *",
                            fg_color=color_1,
                            text_color=color_4,
                            font=("Ivy", 13, "bold"),
                            anchor="nw"
                            )
age_label.place(x=160, y=200)

age_entry = ctk.CTkEntry(bottom_frame,
                            width=132,
                            height=15,
                            font=("Ivy", 13),
                            corner_radius=1
                            )
age_entry.place(x=160, y=225)

# Faixa
belt_label = ctk.CTkLabel(bottom_frame,
                          text="Faixa *",
                          fg_color=color_1,
                          text_color=color_4,
                          font=("Ivy", 13, "bold"),
                          anchor="nw"
                          )
belt_label.place(x=10, y=260)

belt_entry = ctk.CTkEntry(bottom_frame, width=280, height=20, font=("Ivy", 13), corner_radius=1)
belt_entry.place(x=10, y=290)

# Criando os botões

# Cadastrar
register_button = ctk.CTkButton(bottom_frame, 
                                text="Cadastrar", 
                                width=40, height=30, 
                                fg_color=color_6, 
                                text_color=color_1, 
                                hover_color="#0b03fc",
                                font=("Ivy", 13, "bold"), 
                                cursor = "hand2",
                                command=register_btn_function
                                )
register_button.place(x=10, y=340)

# Atualizar
update_button = ctk.CTkButton(bottom_frame, 
                                text="Atualizar", 
                                width=40, height=30, 
                                fg_color=color_8, 
                                text_color=color_1, 
                                hover_color=color_10,
                                font=("Ivy", 13, "bold"), 
                                cursor = "hand2",
                                command=update_btn_function
                                )
update_button.place(x=100, y=340)

# Deletar
delete_button = ctk.CTkButton(bottom_frame, 
                                text="Deletar", 
                                width=40, height=30, 
                                fg_color=color_2, 
                                text_color=color_1, 
                                hover_color=color_7,
                                font=("Ivy", 13, "bold"), 
                                cursor = "hand2",
                                command=delete_btn_function
                                )
delete_button.place(x=190, y=340)

# Carregando a imagem do botão Excel
image = ctk.CTkImage(Image.open("assets/arquivo_excel.png"), size=(30, 30))

# Criando o botão para converter os dados da tabela para um arquivo Excel
excel_button = ctk.CTkButton(bottom_frame,
                          text="",
                          image=image,
                          width=30,
                          height=35,
                          cursor="hand2",
                          fg_color=color_1,
                          hover_color=color_10,
                          command=export_to_excel      
                          )
excel_button.place(x=260, y=335)


# Função para exibir a tabela e configurá-la, além do "READ" do CRUD
def show_table():

    global table

    # Usando a função read do arquivo "view", para adicionar as linhas retornadas pela query SELECT na lista
    info = read()

    # lista para cabeçalho
    table_headers = ['ID','nome',  'e-mail','telefone', 'data de nascimento', 'idade','faixa']


    # criando a tabela
    table = ttk.Treeview(right_frame, selectmode="extended", columns=table_headers, show="headings")

    # vertical scrollbar
    vertical_scroll = ttk.Scrollbar(right_frame, orient="vertical", command=table.yview)

    # horizontal scrollbar
    horizontal_scroll = ttk.Scrollbar(right_frame, orient="horizontal", command=table.xview)

    table.configure(yscrollcommand=vertical_scroll.set, xscrollcommand=horizontal_scroll.set)
    table.grid(column=0, row=0, sticky='nsew')
    vertical_scroll.grid(column=1, row=0, sticky='ns')
    horizontal_scroll.grid(column=0, row=1, sticky='ew')

    right_frame.grid_rowconfigure(0, weight=12)


    header_alignments = ["center","center","center","center","center","center","center"]

    h = [20,170,150,100,120,50,100]
    n = 0
    for col in table_headers:
        table.heading(col, text=col.upper(), anchor=CENTER)

        # Ajusta a largura das colunas
        table.column(col, width=h[n],anchor=header_alignments[n])
        
        n+=1

    for item in info:
        table.insert('', 'end', values=item)

# Chamando a função mostrar tabela
show_table()

window.mainloop()