from PIL import Image, ImageDraw, ImageFont

#Classe qui permet de dessiner les formes voulus
class DrawTools:
    def __init__(self, dim, backColor):
        self.frame = Image.new("RGB",dim,backColor)
        self.img = ImageDraw.Draw(self.frame)

    def PDFSave(self, filename):
        self.frame.save(filename)

    def showtest(self):
        self.frame.show()

    def addEllipse(self, pos, fillcolor=None, linecolor=None):
        self.img.ellipse(pos, fillcolor, linecolor)

    def addRectangle(self, pos, fillColor=None, lineColor=None):
        self.img.rectangle(pos, fillColor, lineColor)

    def addLine(self, pos, fillColor=None, linewidth=0):
        self.img.line(pos, fillColor, linewidth)

    def addText(self,pos, text, sizefont=10, fill=None):
        font = ImageFont.truetype("arial.ttf", sizefont)
        self.img.text(pos, text, fill, font)


if __name__ == "__main__":
    p = DrawTools((1200, 800), (255, 255, 255))
    attt=((0, 0, 50, 80), (0, 0, 0))
    p.addEllipse(*attt)
    p.addRectangle((300, 300, 350, 380), (0, 0, 0))
    p.addLine((0,0,200,300),(0,0,0),5)
    p.addText((0, 60), "jambobinous",80,(0,0,0))
    p.showtest()