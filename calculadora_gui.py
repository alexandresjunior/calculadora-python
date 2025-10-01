import tkinter as tk

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.expressao = ""
        self.tela_var = tk.StringVar()
        self.tela_entry = tk.Entry(
            root, 
            textvariable=self.tela_var, 
            font=('Arial', 24, 'bold'), 
            bd=10, 
            insertwidth=2, 
            width=14, 
            borderwidth=4,
            justify='right'
        )
        self.tela_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.tela_var.set('0')
        self.criar_botoes()

    def press_botao(self, num):
        """Chamado quando um botão de número ou operador é pressionado."""
        if self.expressao == "Erro":
            self.expressao = ""
            
        self.expressao += str(num)
        self.tela_var.set(self.expressao)

    def press_igual(self):
        """Chamado quando o botão '=' é pressionado para calcular o resultado."""
        try:
            # A função eval() avalia a string como uma expressão Python.
            total = str(eval(self.expressao))
            self.tela_var.set(total)
            self.expressao = total
        except (SyntaxError, ZeroDivisionError, NameError):
            self.tela_var.set("Erro")
            self.expressao = "Erro"

    def limpar_tela(self):
        """Limpa a tela e a expressão."""
        self.expressao = ""
        self.tela_var.set("0")

    def criar_botoes(self):
        """Cria e posiciona todos os botões na grade da calculadora."""
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('LIMPAR', 5, 0)
        ]

        for (texto, linha, coluna) in botoes:
            if texto == '=':
                comando = self.press_igual
            elif texto == 'LIMPAR':
                comando = self.limpar_tela
            else:
                comando = lambda t=texto: self.press_botao(t)

            # Estilo dos botões
            cor_bg = '#f0f0f0'
            cor_fg = 'black'
            if texto in '/*-+=':
                cor_bg = '#ff9500'
                cor_fg = 'white'
            if texto == 'LIMPAR':
                cor_bg = '#d4d4d2'
            
            botao = tk.Button(
                self.root, 
                text=texto, 
                padx=20, 
                pady=20, 
                font=('Arial', 18),
                command=comando,
                bg=cor_bg,
                fg=cor_fg,
                width=3
            )
            if texto == 'LIMPAR':
                botao.grid(row=linha, column=coluna, columnspan=4, sticky="nsew", padx=5, pady=5)
            else:
                botao.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)


if __name__ == "__main__":
    janela_principal = tk.Tk()
    app = CalculadoraApp(janela_principal)
    janela_principal.mainloop()