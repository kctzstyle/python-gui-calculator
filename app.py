
import tkinter as tk

from functools import partial

from calculate import Calculator


class Application(tk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master)
        self.master = master
        self.cal = Calculator()
        self.is_input = False

        self.pack()
        self.create_widgets()
        self.grid_widgets()
        self.set_widgets()

    def create_widgets(self):
        self.txtValue = tk.Entry(self)
        self.varValue = tk.StringVar()
        self.btnBack = tk.Button(self)

        self.btnMod = tk.Button(self)
        self.btnCE = tk.Button(self)
        self.btnC = tk.Button(self)
        self.btnDiv = tk.Button(self)
        
        self.btn7 = tk.Button(self)
        self.btn8 = tk.Button(self)
        self.btn9 = tk.Button(self)
        self.btnMul = tk.Button(self)

        self.btn4 = tk.Button(self)
        self.btn5 = tk.Button(self)
        self.btn6 = tk.Button(self)
        self.btnSub = tk.Button(self)

        self.btn1 = tk.Button(self)
        self.btn2 = tk.Button(self)
        self.btn3 = tk.Button(self)
        self.btnAdd = tk.Button(self)

        self.btnNeg = tk.Button(self)
        self.btn0 = tk.Button(self)
        self.btnDot = tk.Button(self)
        self.btnEq = tk.Button(self)

    def grid_widgets(self):
        self.txtValue.grid(row=0, column=0, columnspan=3)
        self.btnBack.grid(row=0, column=3)

        self.btnMod.grid(row=1, column=0)
        self.btnCE.grid(row=1, column=1)
        self.btnC.grid(row=1, column=2)
        self.btnDiv.grid(row=1, column=3)
        
        self.btn7.grid(row=2, column=0)
        self.btn8.grid(row=2, column=1)
        self.btn9.grid(row=2, column=2)
        self.btnMul.grid(row=2, column=3)

        self.btn4.grid(row=3, column=0)
        self.btn5.grid(row=3, column=1)
        self.btn6.grid(row=3, column=2)
        self.btnSub.grid(row=3, column=3)

        self.btn1.grid(row=4, column=0)
        self.btn2.grid(row=4, column=1)
        self.btn3.grid(row=4, column=2)
        self.btnAdd.grid(row=4, column=3)

        self.btnNeg.grid(row=5, column=0)
        self.btn0.grid(row=5, column=1)
        self.btnDot.grid(row=5, column=2)
        self.btnEq.grid(row=5, column=3)

    def set_widgets(self):
        self.varValue.set('0')
        self.txtValue['textvariable'] = self.varValue

        self.btnBack['text'] = '←'

        self.btnC['text'] = 'Ｃ'
        self.btnCE['text'] = 'ＣＥ'

        self.btnAdd['text'] = '＋'
        self.btnSub['text'] = '－'
        self.btnMul['text'] = '×'
        self.btnDiv['text'] = '÷'
        self.btnMod['text'] = '％'
        self.btnNeg['text'] = '±'
        self.btnDot['text'] = '．'
        self.btnEq['text'] = '＝'

        self.btn0['text'] = '０'
        self.btn1['text'] = '１'
        self.btn2['text'] = '２'
        self.btn3['text'] = '３'
        self.btn4['text'] = '４'
        self.btn5['text'] = '５'
        self.btn6['text'] = '６'
        self.btn7['text'] = '７'
        self.btn8['text'] = '８'
        self.btn9['text'] = '９'

        self.btnBack['padx'] = 10
        self.btnBack['pady'] = 10

        self.btnC['padx'] = 10
        self.btnC['pady'] = 10
        self.btnCE['padx'] = 10
        self.btnCE['pady'] = 10

        self.btnAdd['padx'] = 10
        self.btnAdd['pady'] = 10
        self.btnSub['padx'] = 10
        self.btnSub['pady'] = 10
        self.btnMul['padx'] = 10
        self.btnMul['pady'] = 10
        self.btnDiv['padx'] = 10
        self.btnDiv['pady'] = 10
        self.btnMod['padx'] = 10
        self.btnMod['pady'] = 10
        self.btnNeg['padx'] = 10
        self.btnNeg['pady'] = 10
        self.btnDot['padx'] = 10
        self.btnDot['pady'] = 10
        self.btnEq['padx'] = 10
        self.btnEq['pady'] = 10

        self.btn0['padx'] = 10
        self.btn0['pady'] = 10
        self.btn1['padx'] = 10
        self.btn1['pady'] = 10
        self.btn2['padx'] = 10
        self.btn2['pady'] = 10
        self.btn3['padx'] = 10
        self.btn3['pady'] = 10
        self.btn4['padx'] = 10
        self.btn4['pady'] = 10
        self.btn5['padx'] = 10
        self.btn5['pady'] = 10
        self.btn6['padx'] = 10
        self.btn6['pady'] = 10
        self.btn7['padx'] = 10
        self.btn7['pady'] = 10
        self.btn8['padx'] = 10
        self.btn8['pady'] = 10
        self.btn9['padx'] = 10
        self.btn9['pady'] = 10

        self.btnBack['command'] = self.backspace

        self.btnC['command'] = self.clear
        self.btnCE['command'] = self.clear_entry

        self.btnAdd['command'] = self.add
        self.btnSub['command'] = self.sub
        self.btnMul['command'] = self.mul
        self.btnDiv['command'] = self.div
        self.btnMod['command'] = self.mod
        self.btnNeg['command'] = self.neg
        self.btnDot['command'] = self.dot
        self.btnEq['command'] = self.output

        self.btn0['command'] = partial(self.input, value=0)
        self.btn1['command'] = partial(self.input, value=1)
        self.btn2['command'] = partial(self.input, value=2)
        self.btn3['command'] = partial(self.input, value=3)
        self.btn4['command'] = partial(self.input, value=4)
        self.btn5['command'] = partial(self.input, value=5)
        self.btn6['command'] = partial(self.input, value=6)
        self.btn7['command'] = partial(self.input, value=7)
        self.btn8['command'] = partial(self.input, value=8)
        self.btn9['command'] = partial(self.input, value=9)

    def input(self, value):
        v = self.varValue.get()
        if not self.is_input or v == '0':
            v = str(value)
        else:
            v += str(value)
        self.varValue.set(v)
        self.is_input = True

    def output(self):
        v = self.varValue.get()
        self.cal.values = v
        self.varValue.set(str(self.cal))
        self.cal.reset()
        self.is_input = False

    def backspace(self):
        value = self.varValue.get()
        v = value[:-1] if len(value) > 1 else '0'
        self.varValue.set(v)

    def clear(self):
        self.cal.reset()
        self.varValue.set('0')
        self.is_input = False
    
    def clear_entry(self):
        self.varValue.set('0')
        self.is_input = False

    def add(self):
        self.cal.values = self.varValue.get()
        self.cal.values = '+'
        self.varValue.set(str(self.cal))
        self.is_input = False

    def sub(self):
        self.cal.values = self.varValue.get()
        self.cal.values = '-'
        self.varValue.set(str(self.cal))
        self.is_input = False

    def mul(self):
        self.cal.values = self.varValue.get()
        self.cal.values = '*'
        self.varValue.set(str(self.cal))
        self.is_input = False

    def div(self):
        self.cal.values = self.varValue.get()
        self.cal.values = '/'
        self.varValue.set(str(self.cal))
        self.is_input = False

    def mod(self):
        self.cal.values = self.varValue.get()
        self.cal.values = '%'
        self.varValue.set(str(self.cal))
        self.is_input = False

    def neg(self):
        v = self.varValue.get()
        if v.startswith('-'):
            self.varValue.set(v[1:])
        elif v != '0':
            self.varValue.set('-' + v)
        self.is_input = False

    def dot(self):
        v = self.varValue.get()
        if '.' not in v:
            if v[0] == '0':
                self.is_input = False
                self.input('0.')
            else:
                self.input('.')

