from abaqus import *
from abaqusConstants import *
from caeModules import *
def greatZt():
    m=mdb.models['Model-1']
    z1=660
    z2=805
    z3=717
    z4=25
    z5=17
    z6=748
    z7=15
    z1=float(z1)
    z2=float(z2)
    z3=float(z3)
    z4=float(z4)
    z5=float(z5)
    z6=float(z6)
    z7=float(z7)
    sr=m.ConstrainedSketch(name='T002005',sheetSize=200)
    T002005=sr.geometry
    sr.setPrimaryObject(option=SUPERIMPOSE)
    oo=sr.ConstructionLine(point1=(0.0,100.0),point2=(0.0,-100.0))
    line1=sr.Line(point1=(-z1,0.0),point2=(-z1,-z4))
    line2=sr.Line(point1=(-z2,0.0),point2=(-z2,-z5))
    line3=sr.Line(point1=(-z1,0.0),point2=(-z2,0.0))
    line4=sr.Line(point1=(-z2,-z5),point2=(-z3,-z5))
    line5=sr.Line(point1=(-z3,-z5),point2=(-z3,-z4))
    line6=sr.Line(point1=(-z3,-z4),point2=(-z1,-z4))
    sr.unsetPrimaryObject()
    zt=m.Part(name='T002005',dimensionality=THREE_D,type=DEFORMABLE_BODY)
    zt.BaseSolidRevolve(sketch=sr,angle=360)
    p=mdb.models['Model-1'].parts['T002005']
    f,e=p.faces,p.edges
    f1=f.findAt(((0.0,0.0,z1+10),))
    e1=e.findAt(((0.0,0.0,z1),))
    fSetFromfind=p.Set(name='fsetfromfind',faces=f1)
    eSetFromfind=p.Set(name='eSetFind',edges=e1)
    t=p.MakeSketchTransform(sketchPlane=f1[0],sketchUpEdge=e1[0],sketchOrientation=BOTTOM)
    sr1=mdb.models['Model-1'].ConstrainedSketch(name='_temp2_',sheetSize=200.0,transform=t)
    sr1.setPrimaryObject(option=SUPERIMPOSE)
    p.projectReferencesOntoSketch(sketch=sr1,filter=COPLANAR_EDGES)
    radiu=sr1.CircleByCenterPerimeter(center=(-z6,0.0),point1=(-z6-z7,0.0))
    sr1.rotate(centerPoint=(0.0,0.0),angle=4.5,objectList=(radiu, ))
    sr1.radialPattern(geomList=(radiu, ),vertexList=(),number=40,totalAngle=360.0,centerPoint=(0.0,0.0))
    sr1.unsetPrimaryObject()
    p.CutExtrude(sketchPlane=f1[0],sketchUpEdge=e1[0],sketchPlaneSide=SIDE1,
    	sketchOrientation=BOTTOM,sketch=sr1,flipExtrudeDirection=OFF)
if __name__ == '__main__':
    greatZt()
