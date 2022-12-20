from src.objects.landscape.Landscape import Landscape
from src.objects.landscape.Column import Column
from src.objects.blocks.Block import *

class MapLoader:
    def saveMapToFile(file, landscape):
        with open(rf"assets\maps\{file}.txt", "w", encoding = "utf-8") as f:
            f.write(f"{landscape.maxYBlocks}\n{landscape.leftEdge, landscape.rightEdge}\n")
            for column in landscape.columns:
                f.write(f"{column.x, column.y}~")
                for block in column.blocks:
                    f.write(f"{str(block.__class__)[33:-2]}:{block.rect.x},{block.rect.y} ")
                f.write("\n")
            f.close()
    def getMapFromFile(file, edges):
        try:
            with open(rf"assets\maps\{file}.txt", "r", encoding = "utf-8") as f:
                data = f.readlines()
                f.close()
            maxYBlocks = int(eval(data[0][:-1]))
            b = eval(data[1][:-1])
            columns = []
            leftEdge, rightEdge = int(b[0]), int(b[1])
            for i in data[2:]:
                lst = i.split("~")
                crd = eval(lst[0])
                bs = []
                for j in lst[1][:-2].split(" "):
                    cr = j.split(":")
                    cd = cr[1].split(",")
                    bs.append(eval(cr[0])(int(cd[0]), int(cd[1])))
                columns.append(Column(int(crd[0]), int(crd[1]), bs))
            landscape = Landscape(maxYBlocks)
            landscape.columns = columns
            landscape.leftEdge, landscape.rightEdge = leftEdge, rightEdge
            return landscape
        except:
            landscape = Landscape(100)
            landscape.preGenerate(edges[0], edges[0])
            return landscape