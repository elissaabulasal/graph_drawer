from PyQt6.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPen, QColor, QBrush
from PyQt6.QtCore import Qt
from graph import Graph

class GraphUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Drawer")
        self.graph = Graph()
        self.init_ui()

    def init_ui(self):
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        btn_start = QPushButton("Start Graph")
        btn_start.clicked.connect(self.cmd_start)

        btn_add = QPushButton("Add Random Vertex")
        btn_add.clicked.connect(self.cmd_add_random)

        layout = QVBoxLayout()
        layout.addWidget(btn_start)
        layout.addWidget(btn_add)
        layout.addWidget(self.view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def draw_graph(self):
        self.scene.clear()
        pen = QPen(Qt.GlobalColor.black)
        brush = QBrush(QColor("skyblue"))

        for edge in self.graph.edges:
            v1 = self.graph.vertices[edge[0]]
            v2 = self.graph.vertices[edge[1]]
            self.scene.addLine(v1.x, v1.y, v2.x, v2.y, pen)

        for v in self.graph.vertices.values():
            self.scene.addEllipse(v.x-10, v.y-10, 20, 20, pen, brush)
            self.scene.addText(str(v.id)).setPos(v.x-5, v.y-5)

    def cmd_start(self):
        self.graph.start_triangle()
        self.draw_graph()

    def cmd_add_random(self):
        if len(self.graph.periphery) < 2:
            return
        import random
        vp, vq = random.sample(self.graph.periphery, 2)
        self.graph.add_vertex(vp, vq)
        self.draw_graph()
