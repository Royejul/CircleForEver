from PIL import Image, ImageDraw, ImageFont


class DrawTools:
    def __init__(self, dim, backColor):
        self.frame = Image.new("RGB",dim,backColor)
        self.img = ImageDraw.Draw(self.frame)

    def PDFSave(self, filename):
        self.frame.save(filename)

    def showtest(self):
        self.frame.show()

    def addEllipse(self, pos, w, h, fillcolor=None, linecolor=None):
        self.img.ellipse((pos, pos[0]+w, pos[1]+h), fillcolor, linecolor)

    def addRectangle(self, pos, w, h, fillColor=None, lineColor=None):
        self.img.rectangle((pos, pos[0]+w, pos[1]+h), fillColor, lineColor)

    def addLine(self, pointA, pointB, fillColor=None, linewidth=0):
        self.img.line((pointA, pointB), fillColor, linewidth)

    def addText(self,pos, text, sizefont=10, fill=None):
        font = ImageFont.truetype("arial.ttf", sizefont)
        self.img.text(pos, text, fill, font)


if __name__ == "__main__":
    p = DrawTools((400, 800), (255, 255, 0))
    p.addEllipse((0, 0), 50, 80, (0, 0, 0))
    p.addRectangle((300, 300), 50, 80, (0, 0, 0))
    p.addText((0, 60), "jambobinous",80,(0,0,0))
    p.showtest()
    #p.PDFSave("poney.pdf")
