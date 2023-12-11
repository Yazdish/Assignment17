
import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def zero ( ):
    global number
    number = number + "0" 
    window.textbox.setText (number)

def one ():
    global number
    number = number + "1"
    window.textbox.setText (number)

def two () :
    global number
    number = number + "2"
    window.textbox.setText (number)

def three () :
    global number
    number = number + "3"
    window.textbox.setText (number)

def four () :
    global number
    number = number + "4"
    window.textbox.setText (number)

def five () :
    global number
    number = number + "5"
    window.textbox.setText (number)

def six () :
    global number
    number = number + "6"
    window.textbox.setText (number)

def seven () :
    global number
    number = number + "7"
    window.textbox.setText (number)

def eight () :
    global number 
    number = number + "8"
    window.textbox.setText (number)

def nine () :
    global number
    number = number + "9"
    window.textbox.setText (number)

def point () :
    global number
    number = number + "."
    window.textbox.setText (number)

def minus () :
    global number
    number = "-" + number
    window.textbox.setText (number)

def ac () :
    global number 
    number = ""
    window.textbox.setText (number)

def sum () :
    global number
    global operation
    global first
    first = float ( number )
    operation = "+"
    number = ""
    window.textbox.setText (number)

def sub () :
    global number
    global operation
    global first
    first = float (number)
    operation = "-"
    number = ""
    window.textbox.setText (number)

def multi () :
    global number 
    global operation
    global first
    first = float (number)
    operation = "*"
    number = ""
    window.textbox.setText (number)

def divid () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "/"
    number = ""
    window.textbox.setText (number)

def sqrt () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "sqrt"
    text = f"sqrt ({first})"
    window.textbox.setText (text)

def percent () :
    global number
    first = float (number)
    result = first / 100
    window.textbox.setText (str(result))
    number = ""

def log () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "log"
    text = f"log({number})"
    window.textbox.setText (text)

def sin () :
    global number
    global operation
    global first
    first = float (number)
    operation = "sin"
    text = f"sin({number})"
    window.textbox.setText (text)

def cos () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "cos"
    text = f"cos({number})"
    window.textbox.setText (text)

def tan () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "tan"
    text = f"tan({number})"
    window.textbox.setText (text)

def cot () : 
    global number
    global operation
    global first
    first = float (number)
    operation = "cot"
    text = f"cot({number})"
    window.textbox.setText (text)

def equal () :
    global number
    global first
    global operation

    if operation == "+" or operation == "-" or operation == "*" or operation == "/" :
        second = float ( number )

        if operation == "+" :
            result = first + second

        elif operation == "-" :
            result = first - second
        
        elif operation == "*" :
            result = first * second

        elif operation == "/" :
            if second == 0 :
                result = " Error!! "

            else :
                result = first / second
    
    else :
        if operation == "sqrt" :
            if first >= 0 :
                result = math.sqrt (first)
            
            else :
                result = " Error!! "

        elif operation == "log" :
            result = math.log10 (first)

        elif operation == "sin" : 
            rad = first * ( math.pi / 180 )
            result = math.sin (rad)      

        elif operation == "cos" :
            rad = first * ( math.pi / 180 )
            result = math.cos (rad)

        elif operation == "tan" : 
            rad = first * ( math.pi / 180 )
            result = math.tan (rad)

        elif operation == "cot" : 
            rad = first * ( math.pi / 180 )
            result = 1 / ( math.tan (rad) )
    
    window.textbox.setText (str(result))
    number = ""
    operation = ""
    first = ""

app = QApplication ([])
loader = QUiLoader ()
window = loader.load ("calculator.ui")
number = ""
operation = ""

window.zero.clicked.connect (zero)
window.one.clicked.connect (one)
window.two.clicked.connect (two)
window.three.clicked.connect (three)
window.four.clicked.connect (four)
window.five.clicked.connect (five)
window.six.clicked.connect (six)
window.seven.clicked.connect (seven)
window.eight.clicked.connect (eight)
window.nine.clicked.connect (nine)
window.point.clicked.connect (point)
window.minus.clicked.connect (minus)

window.equal.clicked.connect (equal)
window.sum.clicked.connect (sum)
window.sub.clicked.connect (sub)
window.multi.clicked.connect (multi)
window.divide.clicked.connect (divid)
window.sqrt.clicked.connect (sqrt)
window.percent.clicked.connect (percent)
window.log.clicked.connect (log)
window.sin.clicked.connect (sin)
window.cos.clicked.connect (cos)
window.tan.clicked.connect (tan)
window.cot.clicked.connect (cot)

window.ac.clicked.connect (ac)

window.show ()
app.exec ()