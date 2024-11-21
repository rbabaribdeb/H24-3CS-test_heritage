from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

def action():
    print("Action ")
    lbl1.setText("Action ... ")

app = QApplication([])
fen = QWidget()

# Grid Layout
grid = QGridLayout()
fen.setLayout(grid)


# Qlabel
lbl1 = QLabel(fen)
lbl1.setText("Hello World")
lbl1.setGeometry(50,50,200,200)
grid.addWidget(lbl1, 0, 0)
# Input
input1 = QLineEdit(fen)
grid.addWidget(input1, 0, 1)
# Bouton
btn1 = QPushButton()
btn1.setParent(fen)
btn1.setText("Ok")
btn1.clicked.connect(action)
grid.addWidget(btn1, 2, 1)

fen.setGeometry(100, 100, 200, 200)
fen.setWindowTitle("Premiere Fenetre")
fen.show()
app.exec()