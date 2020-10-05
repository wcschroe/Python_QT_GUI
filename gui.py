# USE THIS TO INSTALL STUFF: "pip install PySide2 pyqtgraph"
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLayout, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy, QLabel, QMainWindow, QFrame, QTabWidget, QComboBox, QLineEdit
from PySide2.QtCore import QTimer
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from PySide2.QtGui import QFont
import sys, os
from random import randint

# Create Application
app = QApplication([])
appFont = QFont()
appFont.setPointSize(15)

# first page layou
tab1 = QWidget()
x = [0,1,2,3,4]  # x points
y = [0,1,2,3,4]  # y points

graph = pg.PlotWidget()
graph.enableMouse(False)
graph.setTitle("Data From CSV")
graph.setBackground((255,255,255))
graph.addLegend()
graph.showGrid(x = True, y = True)
graph.setLabel("bottom", "Column 1")
graph.setLabel("left", "Column 2")

pen = pg.mkPen(color=(0,0,255)) #blue line
line = graph.plot(x, y, pen = pen)
line.setData(x, y)

tab1Layout = QGridLayout()
tab1Layout.columnCount = 2
tab1Layout.rowCount = 2
tab1Layout.setColumnStretch(0, 2)
tab1Layout.setColumnStretch(1, 1)

fileLocation = QLineEdit()
fileLocation.setPlaceholderText("CSV File Location")
openFileButton = QPushButton("Open File")
errorOutput = QLabel("")

fileOpenLayout = QVBoxLayout()
fileOpenLayout.addWidget(fileLocation)
fileOpenLayout.addWidget(errorOutput)
fileOpenLayout.addWidget(openFileButton)


tab1Layout.addWidget(graph, 0, 0)
tab1Layout.addLayout(fileOpenLayout, 0, 1)

tab1.setLayout(tab1Layout)

# Setup Tabs
tabs = QTabWidget()
tabs.setTabPosition(QTabWidget.North)
tab2 = QWidget()
tab3 = QWidget()
tabs.addTab(tab1, "Tab 1")
tabs.addTab(tab2, "Tab 2")
tabs.addTab(tab3, "Tab 3")

# add data to graph
def PlotCSV():
    line.clear()
    try:
        csv = open(fileLocation.text(), 'r') #open csv for reading
        pairs = csv.read().splitlines()
        for pair in pairs:
            x.append(float(pair.split(',')[0]))
            y.append(float(pair.split(',')[1]))
    except FileNotFoundError:
        errorOutput.setText(fileLocation.text() + " Not Found (Try sine.csv)")
    line.setData(x, y)

openFileButton.released.connect(PlotCSV)


# Window Setup
win = QMainWindow()
win.setCentralWidget(tabs)
win.resize(800, 480)
win.show()
sys.exit (app.exec_())