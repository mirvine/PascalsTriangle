# 
# Pascals Triangle vizulation of mod triangles 
#
# @Author Mark Irvine
#

# pt is the main PascalTriangle object 
pt = None

# If enabled, screensshots will be taken for each mod
saveScreenshot=True

# The first mod to start on
step = 25

# The gap between mod numbbers
stepJump=1

i=0

def setup():
    # The size of the canvas should be large enough for your triangle.
    
    size(2000,2000)
    noStroke()
    background(000)
    fill(0)
    textSize(24)
    textAlign(LEFT)  
    
    # If the w and h of each block are 2, then number of rows should be half the window size
    # The startx should be half the window size  
    # the num_rows should also be half the window size
    startx = 1000
    starty = 50
    num_rows = startx
    gap = 0
    w = h = 2

    global pt 
    pt = PascalTriangle(startx, starty, num_rows, gap, w, h)
    
def draw():
    global step, pt, saveScreenshot, i
    
    pt.boxNumberDisplay.drawIterationNumber(step-1)

    pt.drawBoxes() 
    pt.clearBoxes()
    pt.colorBoxes(step)
    if saveScreenshot: saveFrame("frames/frame-####.png")
    if i % 200 == 0:
        step+=1
    i+=1

class BoxNumberDisplay():
    def __init__(self, x=20, y=20, w = 90, h=40):
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.number = 0
    
    def drawIterationNumber(self,n):        
        fill(0)
        rect(self.x,self.y+50,self.w,self.h)
        fill(255)
        text("%d" % n, self.x+20, self.y+80)
    
    def update(self,number):
        self.number = long(number)
        
class Box:
    def __init__(self, row, index, x, y, w=20, h=20):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.number = long(1)
        self.color = (255,255,255)
        
    def draw(self):
        fill(self.color[0], self.color[1], self.color[2])
        rect(self.x, self.y, self.w, self.h)
        
class PascalTriangle:
    def __init__(self, startx=1500, starty=50, num_rows=1500, gap=0, w=2, h=2):
        self.startx   = startx
        self.starty   = starty
        self.num_rows = num_rows
        self.gap      = gap
        self.w        = w 
        self.h        = h
        
        self.rows = []
        self.boxNumberDisplay=BoxNumberDisplay()
        self.constructTriangle()
        self.assignNumbers()
        self.boxNumberDisplay.update(1)
        
    
    def constructTriangle(self):
        rows = self.rows
        boxes_in_row = 1

        y = self.starty
        for i in range(self.num_rows):
            rows.append([])
            x = self.startx
            for n in range(boxes_in_row):
                box = Box(i, n, x, y, self.w, self.h)
                rows[i].append(box)
                x += self.w
            boxes_in_row += 1
            y += self.gap + self.h
            self.startx = self.startx - self.w / 2
    
    def assignNumbers(self):
        rows = self.rows
        maxNumber = 0
        rows[0][0].number = 1
        r=1
        for eachRow in rows[1:]:
            i = 0
            left=0
            for eachBox in eachRow: 
                last = len(eachRow)-1
                if i != last :
                    right = long(rows[r-1][i].number)
                else:
                    right = 0
                if i>0: left = long(rows[r-1][i-1].number)
                eachBox.number = long(left) + long(right)
                if eachBox.number > maxNumber: maxNumber = eachBox.number
                i+=1
            r+=1
        println("highest number %d" % maxNumber)
    
    def drawBoxes(self):
        for eachRow in self.rows:
            for eachBox in eachRow:
                eachBox.draw()
                
    def clearBoxes(self):
        for eachRow in self.rows:
            for eachBox in eachRow:
                eachBox.color = (0,0,0)

    def colorBoxes(self,n):
        for eachRow in self.rows:
            for eachBox in eachRow:
                if eachBox.number % n == 0: 
                    eachBox.color= (0,random(100,255),20)    
    
