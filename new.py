from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import * 

def init():
    glClearColor(0,0,0,1)
    gluOrtho2D(-300,300,-300,300)
    
def plotline(x1,y1,x2,y2):
    delX=x2-x1
    delY=y2-y1
    if (abs(delX)> abs(delY)):
        steps = delX
    else:
        steps = delY
    XInc=delX/steps
    YInc=delY/steps
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glPointSize(10)
    glBegin(GL_POINTS)
    for step in range(1,steps+1):
        glVertex2f(round(x1),round(y1))
        x1=x1+XInc
        y1=y1+YInc
    glEnd()
    glFlush()

def main():
    print("Enter the coordinates")
    x1=int(input("Enter x1:"))
    y1=int(input("Enter y1:"))
    x2=int(input("Enter x2:"))
    y2=int(input("Enter y2:"))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(500,500)
    glutCreateWindow("DDA")
    glutDisplayFunc(lambda: plotline(x1,y1,x2,y2))
    glutIdleFunc(lambda: plotline(x1,y1,x2,y2))
    init()
    glutMainLoop()

main()