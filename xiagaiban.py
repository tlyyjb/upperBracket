# -*- coding:utf-8 -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *
import part
#parament
x2=825.0
x3=1720.0
x4=839.0
x5=130.0
x6=1280.0	##下盖板内径
x7=30.0
z6=748.0
z7=15.0
m=mdb.models['Model-1']
xr=m.ConstrainedSketch(name='T002003',sheetSize=200.0)
xr.setPrimaryObject(option=SUPERIMPOSE)
line1=xr.Line(point1=(0.0,-x3/2),point2=(-x1,-x3/2))
line2=xr.Line(point1=(0.0,-x3/2),point2=(x2,-x3/2))
line3=xr.Line(point1=(-x1,-x3/2),point2=(-x1,-585.0))
line4=xr.Line(point1=(-x1,-585.0),point2=(-x1-60.0,-570.0))
line5=xr.Line(point1=(-x1-60.0,-570.0),point2=(-x1-60.0,-270.0))
line6=xr.Line(point1=(-x1-60.0,-270.0),point2=(-x1-380.0,-270.0))
line7=xr.Line(point1=(-x1-380.0,-270.0),point2=(-x1-380.0,270.0))
line8=xr.Line(point1=(-x1-380.0,270.0),point2=(-x1-60.0,270.0))
line9=xr.Line(point1=(-x1-60.0,270.0),point2=(-x1-60.0,570.0))
line10=xr.Line(point1=(-x1-60.0,570.0),point2=(-x1,585.0))
line11=xr.Line(point1=(-x1,585.0),point2=(-x1,x3/2))
line12=xr.Line(point1=(-x1,x3/2),point2=(0.0,x3/2))
line13=xr.Line(point1=(0.0,x3/2),point2=(x2,x3/2))
line14=xr.Line(point1=(x2,x3/2),point2=(x2,x3/2-150.0))
line15=xr.Line(point1=(x2,x3/2-150.0),point2=(x2+395.0,x3/2-170.0))
line16=xr.Line(point1=(x2+395.0,x3/2-170.0),point2=(x2+395.0,x3/2-344.0))
line17=xr.Line(point1=(x2+395.0,x3/2-344.0),point2=(x2+35.0,x3/2-391.0))
line18=xr.Line(point1=(x2+35.0,x3/2-391.0),point2=(x2+35.0,x3/2-556.0))
line19=xr.Line(point1=(x2+35.0,x3/2-556.0),point2=(x2+395.0,x3/2-556.0))
line20=xr.Line(point1=(x2,-x3/2),point2=(x2,-x3/2-x4-636.0))
line21=xr.Line(point1=(x2,-x3/2-x4-636.0),point2=(x2+395.0,x3/2-x4-556.0))
line21=xr.Line(point1=(x2+395.0,x3/2-x4-556.0),point2=(x2+395.0,x3/2-556.0))
xr.unsetPrimaryObject()
p1=m.Part(name='T002003',dimensionality=THREE_D,type=DEFORMABLE_BODY)
p1.BaseSolidExtrude(sketch=xr,depth=x7)
f,e=p1.faces,p1.edges
f1=f.findAt(((-x1,x3/2,x7),))
e1=e.findAt(((-x1+100,-x3/2,x7),))
fstfromfind=p1.Set(name='fsetfromfind',faces=f1)
esetfromfind=p1.Set(name='eSetFromFind',edges=e1)
t=p1.MakeSketchTransform(sketchPlane=f1[0],sketchUpEdge=e1[0],sketchOrientation=BOTTOM)
xr1=mdb.models['Model-1'].ConstrainedSketch(name='_temp_',sheetSize=200.0,transform=t)
xr1=xr.setPrimaryObject(option=SUPERIMPOSE)
P1.projectReferencesOntoSketch(sketch=xr1,filter=COPLANAR_EDGES)
xr1.CircleBycenterPerimeter(center=(-x1-150.0,0.0),point1=(-x1-150-x5,0.0))
xr1.CircleBycenterPerimeter(center=(x2+165.0,0.0),point1=(x2+x5+165,0.0))
xr1.CircleBycenterPerimeter(center=(0.0,0.0),point1=(x6/2,0.0))
p1.CutExtrude(sketchPlane=f1[0],sketchUpEdge=e1[0],sketchPlaneSide=SIDE1,
			sketchOrientation=BOTTOM,sketch=xr1,flipExtrudeDirection=OFF)
xr1.unsetPrimaryObject()
p2=mab.models['model-1'].parts['T002003']
xr2=mdb.models['Model-1'].ConstrainedSketch(name='_temp_1',sheetSize=200,transform=t)
xr2=s.setPrimaryObject(option=SUPERIMPOSE)
p2.projectReferencesOntoSketch(sketch=xr2,filter=COPLANAR_EDGES)
raidu=xr2.CircleByCenterPerimeter(center=(-z6,0.0),point=(-z6-z7,0.0))
xr2.rotate(centerPoint=(0.0,0.0),angle=4.5,objectList=(raidu,))
xr2.radialPattern(gemoList=(radiu,),vertexList=(),number=40,totalAngle=360.0,centerPoint=(0.0,0.0))
xr2.unsetPrimaryObject()
f, e=p2.faces, p2.edges
f2=f.findAt(((0.0,x3/2-50,x7),))
e2=e.findAt(((-x1+100,-x3/2,x7)))
fSetFromfind=p1.Set(name='fSetFromfind',faces=f2)
eSetFromfind=p1.Set(name='eSetFromfind',edges=e2)
p2.CutExtrude(sketchPlane=f2[0],sketchUpEdge=e2[0],sketchOrientation=BOTTOM,sketch=xr2)
