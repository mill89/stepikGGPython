class Graph:
    def set_data(self, data: list) -> None:
        self.data = data

    def draw(self) -> str:
        LIMIT_Y = [0, 10]
        return ' '.join(str(n) for n in self.data
                        if n in range(LIMIT_Y[0], LIMIT_Y[1] + 1))


if __name__ == '__main__':
    graph_1 = Graph()
    graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
    print(graph_1.draw())

    assert graph_1.draw() == '10 0 2 5 7'
