# Imports
import tkinter as tk
from tkinter import messagebox, ttk

# Cores do Aplicativo
cor_fundo = "#14293D"
cor_fontePrincipal = "#E8F1F3"
cor_fonteSecundaria = "#1C99E0"

# Configurações da Janela Principal
janela = tk.Tk()
janela.title("Identificação de Cobra")
janela.geometry("850x400")
janela.configure(bg=cor_fundo)
janela.resizable(False, False)

# Mostra o Título da janela
titulo = tk.Label(janela, text="Identificação da Cobra", font=("Helvetica", 22, "bold"), bg=cor_fundo, fg=cor_fontePrincipal)
titulo.pack(pady=5, ipadx=5, ipady=5)

# Subtítulo, aviso importante.
instrucoes = tk.Label(janela, text="Preencha o formulário para identificar a possível espécie da cobra.", font=("Helvetica", 13), bg=cor_fundo, fg=cor_fonteSecundaria)
instrucoes.pack(pady=7)

# Rodapé com o nome dos integrantes do grupo.
rodape = tk.Label(janela, text="Grupo Desenvolvedor: Juliene, Diego, Maria Julia, Gabriel Torres, Gabriel da Silva", font=("Helvetica", 8), bg=cor_fundo, fg=cor_fonteSecundaria)
rodape.pack(side="bottom", pady=10)

# Perguntas e opções de resposta com pontuação equivalente
perguntas = [
    
    # Pergunta 1
    ("Onde a mordida ocorreu?", 
     ("Em área rural", 1), 
     ("Em área urbana", 2), 
     ("Próximo a corpos d'água", 3), 
     ("Em uma trilha ou floresta", 4)),
    
    # Pergunta 2
    ("Qual é a localização da mordida no corpo?", 
     ("Perna (superior ou inferior)", 1), 
     ("Braço (superior ou inferior)", 2), 
     ("Mão ou dedo", 3), 
     ("Pé ou tornozelo", 4)),
    
    # Pergunta 3
    ("Como você descreveria a cor e o padrão da cobra?", 
     ("Escura (preto, marrom, etc.)", 1), 
     ("Clara (amarelo, cinza, verde, etc.)", 2), 
     ("Com padrões visíveis (listras, manchas, etc.)", 3), 
     ("Sólida, sem padrões evidentes", 4)),
    
    # Pergunta 4
    ("Qual é o tamanho estimado da cobra?", 
     ("Menos de 50 cm", 1), 
     ("Entre 50 cm e 1 metro", 2), 
     ("Entre 1 metro e 2 metros", 3), 
     ("Mais de 2 metros", 4)),
    
    # Pergunta 5
    ("A cobra tem uma cabeça visivelmente triangular ou distinta?", 
     ("Sim", 1), 
     ("Não", 0)),
    
    # Pergunta 6
    ("A cobra parecia ter presas grandes ou visíveis na boca?", 
     ("Sim", 1), 
     ("Não", 0)),
    
    # Pergunta 7
    ("Qual foi o comportamento da cobra antes da mordida?", 
     ("Se moveu rapidamente e atacou", 1), 
     ("Estava quieta, mas se moveu quando ameaçada", 2), 
     ("Se arrastava lentamente, sem agressividade", 3)),
    
    # Pergunta 8
    ("A mordida foi rápida ou a cobra demorou a se afastar?", 
     ("Mordida rápida, depois afastou-se", 1), 
     ("Permaneceu mais tempo no local da mordida", 2)),
    
    # Pergunta 9
    ("Após a mordida, houve algum sinal visível de inchaço ou mudança de cor na pele?", 
     ("Sim, inchaço significativo", 1), 
     ("Sim, mudança de cor (vermelhidão, roxidão, etc.)", 2), 
     ("Não percebi mudanças visíveis", 0)),
    
    # Pergunta 10
    ("Você sentiu algum sintoma imediato após a mordida?", 
     ("Dor forte no local da mordida", 1), 
     ("Tontura ou náuseas", 2), 
     ("Dificuldade para respirar", 3), 
     ("Visão embaçada ou problemas neurológicos", 4), 
     ("Nenhum sintoma significativo", 0)),
]

# Base de dados com as 32 cobras identificáveis com o sistema.
cobras = [

    # Cobra 1: Jararaca
    {"nome": "Jararaca", "habitat": 1, "local_mordida": [1, 4], "cor_padrao": 1, "tamanho": 2, "cabeca_triangular": 1, 
     "presas_visiveis": 1, "comportamento": [1, 2], "mordida": 1, "sinais_mordida": [1, 2], "sintomas": [1, 2]},
    
    # Cobra 2: Cascavel
    {"nome": "Cascavel", "habitat": 1, "local_mordida": [1, 4], "cor_padrao": 3, "tamanho": 3, "cabeca_triangular": 1, 
     "presas_visiveis": 1, "comportamento": [1], "mordida": 1, "sinais_mordida": [2], "sintomas": [3, 4]},

    # Cobra 3: Jiboia
    {"nome": "Jiboia", "habitat": 3, "local_mordida": [4], "cor_padrao": 4, "tamanho": 4, "cabeca_triangular": 0, 
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 4: Surucucu
    {"nome": "Surucucu", "habitat": 4, "local_mordida": [1, 4], "cor_padrao": 3, "tamanho": 4, "cabeca_triangular": 1, 
     "presas_visiveis": 1, "comportamento": [1, 2], "mordida": 1, "sinais_mordida": [1, 2], "sintomas": [3, 4]},
    
    # Cobra 5: Cobra Verde
    {"nome": "Cobra-verde", "habitat": 3, "local_mordida": [2, 3], "cor_padrao": 2, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [1], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 6: Cobra Cipó
    {"nome": "Cobra-Cipó", "habitat": 4, "local_mordida": [3, 4], "cor_padrao": 2, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 7: Caniana
    {"nome": "Caninana", "habitat": 3, "local_mordida": [1, 2], "cor_padrao": 2, "tamanho": 3, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [1, 2], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 8: Cobra Papagaio
    {"nome": "Cobra Papagaio", "habitat": 3, "local_mordida": [4], "cor_padrao": 2, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 9: Urutu
    {"nome": "Urutu", "habitat": 1, "local_mordida": [1, 4], "cor_padrao": 1, "tamanho": 3, "cabeca_triangular": 1,
     "presas_visiveis": 1, "comportamento": [2], "mordida": 1, "sinais_mordida": [1, 2], "sintomas": [1, 2]},

    # Cobra 10: Cobra Preta
    {"nome": "Cobra-Preta", "habitat": 2, "local_mordida": [1, 3], "cor_padrao": 1, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},

    # Cobra 11: Cobra de Vidro
    {"nome": "Cobra-de-Vidro", "habitat": 3, "local_mordida": [4], "cor_padrao": 2, "tamanho": 1, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 12: Coral Verdadeira
    {"nome": "Coral Verdadeira", "habitat": 4, "local_mordida": [2, 3], "cor_padrao": 3, "tamanho": 2, "cabeca_triangular": 1,
     "presas_visiveis": 1, "comportamento": [1], "mordida": 1, "sinais_mordida": [1, 2], "sintomas": [3, 4]},
    
    # Cobra 13: Sucuri
    {"nome": "Sucuri", "habitat": 3, "local_mordida": [1, 4], "cor_padrao": 1, "tamanho": 4, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},

    # Cobra 14: Cobra de Fogo
    {"nome": "Cobra-de-Fogo", "habitat": 4, "local_mordida": [3, 4], "cor_padrao": 3, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 1, "comportamento": [1, 2], "mordida": 1, "sinais_mordida": [1], "sintomas": [1, 3]},
    
    # Cobra 15: Cobra de Duas Cabeças
    {"nome": "Cobra de duas cabeças", "habitat": 3, "local_mordida": [4], "cor_padrao": 2, "tamanho": 1, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 16: Cobra Dormideira
    {"nome": "Cobra-dormideira", "habitat": 2, "local_mordida": [3, 4], "cor_padrao": 2, "tamanho": 1, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},

    # Cobra 17: Cobra Tigre
    {"nome": "Cobra-tigre", "habitat": 1, "local_mordida": [1, 4], "cor_padrao": 1, "tamanho": 3, "cabeca_triangular": 1,
     "presas_visiveis": 1, "comportamento": [1], "mordida": 1, "sinais_mordida": [1], "sintomas": [2, 3]},

    # Cobra 18: Cobra Café
    {"nome": "Cobra-café", "habitat": 1, "local_mordida": [1, 2], "cor_padrao": 1, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},

    # Cobra 19: Cobra Falsa Coral
    {"nome": "Falsa Coral", "habitat": 3, "local_mordida": [2, 3], "cor_padrao": 3, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},

    # Cobra 20: Cobra da Terra
    {"nome": "Cobra-da-terra", "habitat": 1, "local_mordida": [1, 4], "cor_padrao": 1, "tamanho": 1, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},

    # Cobra 21: Cobra da água
    {"nome": "Cobra-d'água", "habitat": 3, "local_mordida": [4], "cor_padrao": 2, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},

    # Cobra 22: Cobra Jararaca-Dormideira
    {"nome": "Jararaca-dormideira", "habitat": 3, "local_mordida": [3, 4], "cor_padrao": 2, "tamanho": 1, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 23: Cobra Jaracuçu do Brejo
    {"nome": "Cobra-jaracuçu-do-brejo", "habitat": 1, "local_mordida": [1, 4], "cor_padrao": 1, "tamanho": 3, "cabeca_triangular": 1,
     "presas_visiveis": 1, "comportamento": [2], "mordida": 1, "sinais_mordida": [1], "sintomas": [1, 2]},
    
    # Cobra 24: Cobra do Campo
    {"nome": "Cobra-do-campo", "habitat": 2, "local_mordida": [1, 2], "cor_padrao": 1, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 25: Cobra do Papo Amarelo
    {"nome": "Cobra-papo-amarelo", "habitat": 3, "local_mordida": [3, 4], "cor_padrao": 2, "tamanho": 2, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},

    # Cobra 26: Cobra Caiçara
    {"nome": "Cobra-caiçara", "habitat": 4, "local_mordida": [1, 3], "cor_padrao": 3, "tamanho": 3, "cabeca_triangular": 1,
     "presas_visiveis": 1, "comportamento": [1, 2], "mordida": 1, "sinais_mordida": [1], "sintomas": [2]},
    
    # Cobra 27: Cobra Lisa
    {"nome": "Cobra-lisa", "habitat": 2, "local_mordida": [2, 4], "cor_padrao": 2, "tamanho": 1, "cabeca_triangular": 0,
     "presas_visiveis": 0, "comportamento": [3], "mordida": 2, "sinais_mordida": [0], "sintomas": [0]},
    
    # Cobra 28: Cobra Tapirapé
    {"nome": "Cobra-tapirapé", "habitat": 4, "local_mordida": [1, 4], "cor_padrao": 3, "tamanho": 3, "cabeca_triangular": 1,
     "presas_visiveis": 1, "comportamento": [1], "mordida": 1, "sinais_mordida": [1, 2], "sintomas": [3]},
]

respostas = []  # Lista para armazenar as respostas
indice_pergunta = 0  # Índice da pergunta atual

# Função para Retornar para a pergunta anterior
def voltar_pergunta():
    global indice_pergunta, respostas

    # Verifica se não está na primeira pergunta
    if indice_pergunta > 0:
        # Remove a resposta da pergunta atual
        respostas.pop()
        
        # Volta para a pergunta anterior
        indice_pergunta -= 1

        # Mostra a pergunta anterior
        mostrar_pergunta()

# Função para exibir a próxima pergunta
def mostrar_pergunta():
    global indice_pergunta

    # Reseta a seleção anterior
    resposta_selecionada.set("") 

    # Verifica se a pergunta existe baseado em seu indíce.
    if indice_pergunta < len(perguntas):
        pergunta = perguntas[indice_pergunta]
        label_pergunta.config(text=pergunta[0])

        # Esconder todos os botões de opção primeiro
        for botao in botoes_opcoes:
            botao.pack_forget()

        # Exibir apenas os botões necessários para a pergunta atual
        for i, opcao in enumerate(pergunta[1:], start=0):
            botoes_opcoes[i].config(text=opcao[0], value=opcao[1])
            botoes_opcoes[i].pack(anchor="w")

        # Mostrar o frame de botões e o frame de envio
        botoes_frame.pack()
        botoesEnvio.pack(pady=20)
    else:
        # No caso de não existir, quer dizer que é a ultima pergunta.
        exibir_resultado()

# Função para salvar a resposta e passar para a próxima pergunta
def confirmar_resposta():
    global indice_pergunta

    # Se não selecionar nenhuma, o programa vai apitar um aviso.
    if resposta_selecionada.get() == "":
        messagebox.showwarning("Aviso", "Você precisa selecionar uma resposta!")
        return
    
    # Passa para o próximo indíce de pergunta.
    respostas.append(int(resposta_selecionada.get()))
    indice_pergunta += 1
    mostrar_pergunta()

# Função para exibir o resultado final
def exibir_resultado():
    label_pergunta.pack_forget()
    botoes_frame.pack_forget()
    botoesEnvio.pack_forget()
    conclusao.config(text="Formulário concluído! Analisando as respostas...", font=("Helvetica", 16))
    conclusao.pack(pady=20)

    # Análise das respostas
    resultados = []  # Lista para armazenar as cobras identificadas
    for cobra in cobras:
        if all(
            respostas[i] in cobra.get(chave, []) if isinstance(cobra.get(chave, []), list) else respostas[i] == cobra[chave]
            for i, chave in enumerate([
                "habitat", 
                "local_mordida",
                "cor_padrao",
                "tamanho",
                "cabeca_triangular", 
                "presas_visiveis",
                "comportamento",
                "mordida",
                "sinais_mordida",
                "sintomas"
            ])
        ):
            resultados.append(cobra['nome'])  # Adiciona o nome da cobra à lista de resultados

    # Verifica se alguma cobra foi identificada
    if resultados:
        resultado = "As cobras identificadas são: " + ", ".join(resultados) + "."
    else:
        resultado = "Não foi possível determinar a cobra com base nas respostas."

    conclusao.config(text=resultado)

    # Botão Sair para fechar a aplicação
    botaoSair = ttk.Button(janela, text="Concluir", command=janela.quit)
    botaoSair.pack(pady=20)

# Label para exibir a pergunta atual
label_pergunta = tk.Label(janela, text="", font=("Helvetica", 16), bg=cor_fundo, fg=cor_fontePrincipal)
label_pergunta.pack(pady=20)

# Variável para armazenar a resposta selecionada
resposta_selecionada = tk.StringVar()
resposta_selecionada.set("")

# Estilo dos radiobuttons
estilo_radiobutton = ttk.Style()
estilo_radiobutton.configure("TRadiobutton", background=cor_fundo, foreground=cor_fontePrincipal, font=("Helvetica", 12))

# Criação dos botões de resposta
botoes_frame = tk.Frame(janela, bg=cor_fundo)
botoes_opcoes = []

for _ in range(10):  # Máximo de opções de resposta
    botao_opcao = ttk.Radiobutton(botoes_frame, variable=resposta_selecionada, style="TRadiobutton")
    botoes_opcoes.append(botao_opcao)

# Criando frame para alinhar os botões Confirmar e Voltar lado a lado
botoesEnvio = tk.Frame(janela, bg=cor_fundo)

# Botão de confirmar com o comando que grava a pontuação da resposta para a mensagem final
botaoConfirmar = ttk.Button(botoesEnvio, text="Confirmar", command=confirmar_resposta, width=25)

# Botão de voltar com o comando que retorna a pontuação junto da pergunta no caso do usuário se arrepender da resposta
botaoVoltar = ttk.Button(botoesEnvio, text="Voltar", command=voltar_pergunta, width=25)

# Ativando os botões
botaoConfirmar.pack(side="left", padx=10)
botaoVoltar.pack(side="left", padx=10)

# Exibir a primeira pergunta
mostrar_pergunta()

# Mensagem de conclusão
conclusao = tk.Label(janela, text="Teste concluído! Obrigado por responder.", font=("Helvetica", 16), bg=cor_fundo, fg=cor_fontePrincipal)

# Executando a Janela
janela.mainloop()

