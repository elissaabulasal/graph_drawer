import math

class Vertex:
    def __init__(self, id, x, y, color=1):
        self.id = id
        self.x = x
        self.y = y
        self.color = color

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = set()
        self.periphery = []
        self.counter = 1

    def start_triangle(self):
        self.vertices.clear()
        self.edges.clear()
        self.periphery.clear()
        self.counter = 1

        v1 = Vertex(self.counter, 0, 100)
        v2 = Vertex(self.counter+1, -100, -100)
        v3 = Vertex(self.counter+2, 100, -100)
        self.vertices[v1.id] = v1
        self.vertices[v2.id] = v2
        self.vertices[v3.id] = v3

        self.edges.update({(v1.id, v2.id), (v2.id, v3.id), (v3.id, v1.id)})
        self.periphery = [v1.id, v2.id, v3.id]
        self.counter += 3

    def add_vertex(self, vp, vq):
        if vp not in self.periphery or vq not in self.periphery:
            return None
        i = self.periphery.index(vp)
        j = self.periphery.index(vq)
        n = len(self.periphery)

        if i <= j:
            span = self.periphery[i:j+1]
        else:
            span = self.periphery[i:] + self.periphery[:j+1]

        angle = 2 * math.pi / len(span)
        radius = 200
        center_x = 0
        center_y = 0

        new_id = self.counter
        self.counter += 1

        mid_angle = angle * (len(span) - 1) / 2
        x = center_x + radius * math.cos(mid_angle)
        y = center_y + radius * math.sin(mid_angle)

        new_vertex = Vertex(new_id, x, y)
        self.vertices[new_id] = new_vertex

        for vid in span:
            self.edges.add((new_id, vid))

        insert_idx = self.periphery.index(span[-1])
        self.periphery.insert(insert_idx, new_id)
        return new_vertex
