from enum import Enum
from typing import Tuple
from PIL import Image, ImageDraw

class Color(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    GREEN2 = (0, 127, 0)
    RED = (255, 0, 0)

class CartesianPlane:

    max: int = 1200
    half: int = 600
    unit: int = 20

    def __init__(self) -> None:
        self._im = Image.new(mode="RGB", size=(self.max, self.max))
        self._draw = ImageDraw.Draw(self._im)

        for i in range(self.max):
            # vertical
            start = (i * self.unit , 0)
            end = (i * self.unit , self.max)
            self._draw.line([start, end], fill=Color.GREEN2.value)
            if i % 5 == 0:
                pass
            # horizontal
            start = (0, i * self.unit )
            end = (self.max, i * self.unit)
            self._draw.line([start, end], fill=Color.GREEN2.value)
            if i % 5 == 0:
                pass

        # main axis
        self._draw.line([(self.half,0),(self.half,self.max)],fill=Color.GREEN2.value,width=4)
        self._draw.line([(0,self.half),(self.max,self.half)],fill=Color.GREEN2.value,width=4)

        # labels
        for i in range(1,self.half-self.unit):
            if i % 5 == 0:
                self._draw.text(xy=(self.half + self.unit * i + 3, self.half + 3),
                    text=f"{i}",
                    fill=Color.GREEN2.value)
                self._draw.text(xy=(self.half - self.unit * i + 3, self.half + 3),
                        text=f"-{i}",
                        fill=Color.GREEN2.value)
                self._draw.text(xy=(self.half - 13, self.half - self.unit * i ),
                    text=f"{i}",
                    fill=Color.GREEN2.value)
                self._draw.text(xy=(self.half - 14, self.half + self.unit * i ),
                    text=f"-{i}",
                    fill=Color.GREEN2.value)

    def show(self) -> None:
        self._im.show()

    def pointToImgPoint(self, point: Tuple[float,float]) -> Tuple[float,float]:
        x = self.half + point[0] * self.unit
        y = self.half - (point[1] * self.unit)
        return (x,y)

    def drawLine(self, start: Tuple[float,float], end: Tuple[float,float]) -> None:
        self._draw.line([
            self.pointToImgPoint(start),
            self.pointToImgPoint(end)
        ])

    def drawCircle(self, center: Tuple[float,float], radius: float) -> None:
        c = self.pointToImgPoint(center)
        r = radius * self.unit
        cor = [c[0]-r, c[0]-r,c[0]+r,c[0]+r]
        print(cor)
        self._draw.ellipse(
            cor
        )


if __name__ == "__main__":
    cp = CartesianPlane()
    cp.drawLine((0,0),(10,10))
    cp.drawLine((0,0),(8,-8))
    cp.drawLine((0,0),(-4,-6))
    cp.drawLine((-10,-3),(-4,6))
    cp.drawCircle((0,0),2)
    cp.drawCircle((2,2),1)
    cp.show()
