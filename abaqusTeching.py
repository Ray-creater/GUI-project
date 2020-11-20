# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_16-10.28.56 126354
# Run by Ray on Fri Nov 20 21:48:23 2020
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=289.849975585938, 
    height=196.785186767578)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
mdb.saveAs(pathName='C:/Users/Ray/Desktop/abaqusGui/model/caeModel')
#: The model database has been saved to "C:\Users\Ray\Desktop\abaqusGui\model\caeModel.cae".
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
del session.viewports['Viewport: 1']
#* CanvasError: SystemError: the current viewport may not be deleted.
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Concrete')
mdb.models['Model-1'].materials['Concrete'].Density(table=((2.4e-09, ), ))
mdb.models['Model-1'].materials['Concrete'].Elastic(table=((20800000000.0, 
    0.2), ))
mdb.models['Model-1'].materials['Concrete'].ConcreteDamagedPlasticity(table=((
    40.0, 0.1, 1.225, 0.6667, 0.0005), ))
mdb.models['Model-1'].materials['Concrete'].concreteDamagedPlasticity.ConcreteCompressionHardening(
    table=((6780000.0, 0.0), (12500000.0, 6.025e-05), (16900000.0, 0.0001815), 
    (20100000.0, 0.0003637), (22000000.0, 0.0006069), (22600000.0, 0.0009111), 
    (19200000.0, 0.002874), (1130.0, 0.02)))
mdb.models['Model-1'].materials['Concrete'].concreteDamagedPlasticity.ConcreteTensionStiffening(
    table=((2260000.0, 0.0), ))
mdb.save()
#: The model database has been saved to "C:\Users\Ray\Desktop\abaqusGui\model\caeModel.cae".
mdb.save()
#: The model database has been saved to "C:\Users\Ray\Desktop\abaqusGui\model\caeModel.cae".
mdb.save()
#: The model database has been saved to "C:\Users\Ray\Desktop\abaqusGui\model\caeModel.cae".
mdb.save()
#: The model database has been saved to "C:\Users\Ray\Desktop\abaqusGui\model\caeModel.cae".
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.44302, 
    farPlane=4.48518, width=1.7659, height=0.865414, cameraPosition=(1.45627, 
    -1.7746, 2.05898), cameraUpVector=(0.159424, 0.926888, 0.339798), 
    cameraTarget=(-0.5, -0.5, -0.5))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.52285, 
    farPlane=4.40535, width=1.8236, height=0.893693, cameraPosition=(2.17751, 
    -2.59235, 0.173036), cameraUpVector=(0.465468, 0.747885, 0.473294), 
    cameraTarget=(-0.5, -0.5, -0.500001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.46095, 
    farPlane=4.46725, width=1.77885, height=0.871764, cameraPosition=(2.04829, 
    -2.36759, -1.92067), cameraUpVector=(0.677033, 0.604707, 0.419471), 
    cameraTarget=(-0.5, -0.5, -0.500003))
mdb.models['Model-1'].materials['Concrete'].density.setValues(table=((2400.0, 
    ), ))
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Density(table=((7800.0, ), ))
mdb.models['Model-1'].materials['Steel'].Elastic(table=((210000000000.0, 0.3), 
    ))
mdb.models['Model-1'].materials['Steel'].Plastic(table=((327800000.0, 0.0), (
    873800000.0, 0.2574)))
mdb.models['Model-1'].materials.changeKey(fromName='Steel', 
    toName='BiaLinerSteel')
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(25.0, 0.0))
s1.Line(point1=(-24.4948974278318, -5.0), point2=(24.4948974277359, -5.0))
s1.HorizontalConstraint(entity=g[3], addUndoState=False)
s1.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
s1.CoincidentConstraint(entity1=v[3], entity2=g[2], addUndoState=False)
s1.autoTrimCurve(curve1=g[2], point1=(-25.583324432373, 1.61672973632813))
s1.autoTrimCurve(curve1=g[4], point1=(25.4083862304688, -1.26716613769531))
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
    type=ANALYTIC_RIGID_SURFACE)
p = mdb.models['Model-1'].parts['Part-1']
p.AnalyticRigidSurfExtrude(sketch=s1, depth=200.0)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=355.294, 
    farPlane=550.362, width=211.395, height=103.598, viewOffsetX=0.862827, 
    viewOffsetY=2.01151)
p = mdb.models['Model-1'].parts['Part-1']
e = p.edges
p.DatumPointByMidPoint(point1=p.InterestingPoint(edge=e[3], rule=MIDDLE), 
    point2=p.InterestingPoint(edge=e[1], rule=MIDDLE))
session.viewports['Viewport: 1'].view.setValues(nearPlane=345.517, 
    farPlane=565.221, width=205.577, height=100.747, cameraPosition=(102.805, 
    229.472, 370.315), cameraUpVector=(-0.708106, 0.46268, -0.533397), 
    cameraTarget=(-1.66437, -21.5989, 8.23372), viewOffsetX=0.839084, 
    viewOffsetY=1.95616)
p = mdb.models['Model-1'].parts['Part-1']
v1, e1, d1, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=d1[2])
session.viewports['Viewport: 1'].view.setValues(nearPlane=343.453, 
    farPlane=570.077, width=204.349, height=100.145, cameraPosition=(39.7614, 
    186.472, 408.118), cameraUpVector=(-0.788228, 0.37246, -0.489868), 
    cameraTarget=(-1.54185, -21.7508, 8.13036), viewOffsetX=0.834072, 
    viewOffsetY=1.94447)
session.viewports['Viewport: 1'].view.setValues(nearPlane=339.918, 
    farPlane=578.246, width=202.246, height=99.1143, cameraPosition=(-122.955, 
    112.793, 423.574), cameraUpVector=(-0.259485, 0.69957, -0.665785), 
    cameraTarget=(-4.39703, -22.8511, 8.12565), viewOffsetX=0.825487, 
    viewOffsetY=1.92446)
mdb.models['Model-1'].parts.changeKey(fromName='Part-1', 
    toName='LoadSupporter')
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(-100.0, -200.0), point2=(100.0, 200.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=91.8481, 
    farPlane=285.276, width=1167.41, height=592.838, cameraPosition=(92.6396, 
    22.1436, 188.562), cameraTarget=(92.6396, 22.1436, 0))
s.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']
p1 = mdb.models['Model-1'].parts['LoadSupporter']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['LoadSupporter']
s1 = p.features['3D Analytic rigid shell-1'].sketch
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=s1)
s2 = mdb.models['Model-1'].sketches['__edit__']
g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
s2.setPrimaryObject(option=SUPERIMPOSE)
p.projectReferencesOntoSketch(sketch=s2, 
    upToFeature=p.features['3D Analytic rigid shell-1'], filter=COPLANAR_EDGES)
s2.delete(objectList=(g[5], ))
s2.delete(objectList=(g[3], ))
s2.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__edit__']
del mdb.models['Model-1'].parts['LoadSupporter']
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.025, 0.0))
session.viewports['Viewport: 1'].view.setValues(nearPlane=188.553, 
    farPlane=188.571, width=0.105249, height=0.0534478, cameraPosition=(
    0.0113013, -0.00523373, 188.562), cameraTarget=(0.0113013, -0.00523373, 0))
s.Spot(point=(0.0, -0.005))
s.Line(point1=(0.0, -0.005), point2=(-0.0244948973413557, -0.005))
s.HorizontalConstraint(entity=g[3], addUndoState=False)
s.CoincidentConstraint(entity1=v[4], entity2=g[2], addUndoState=False)
s.Line(point1=(0.0, -0.005), point2=(0.0244948973413557, -0.005))
s.HorizontalConstraint(entity=g[4], addUndoState=False)
s.CoincidentConstraint(entity1=v[6], entity2=g[2], addUndoState=False)
s.autoTrimCurve(curve1=g[2], point1=(-0.0250180289149284, 0.00501526286825538))
s.autoTrimCurve(curve1=g[5], point1=(0.0247665606439114, -0.00246283272281289))
p = mdb.models['Model-1'].Part(name='LoadSupporter', dimensionality=THREE_D, 
    type=ANALYTIC_RIGID_SURFACE)
p = mdb.models['Model-1'].parts['LoadSupporter']
p.AnalyticRigidSurfExtrude(sketch=s, depth=0.2)
s.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['LoadSupporter']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=0.357633, 
    farPlane=0.548023, width=0.188018, height=0.0921417, 
    viewOffsetX=-0.0105573, viewOffsetY=0.00212804)
p = mdb.models['Model-1'].parts['LoadSupporter']
e = p.edges
p.DatumPointByMidPoint(point1=p.InterestingPoint(edge=e[4], rule=MIDDLE), 
    point2=p.InterestingPoint(edge=e[1], rule=MIDDLE))
p = mdb.models['Model-1'].parts['LoadSupporter']
v2, e1, d2, n1 = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=d2[2])
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=200.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.rectangle(point1=(-0.1, -0.2), point2=(0.1, 0.2))
session.viewports['Viewport: 1'].view.setValues(nearPlane=188.357, 
    farPlane=188.766, width=2.1825, height=1.10832, cameraPosition=(0.0440615, 
    -0.0888247, 188.562), cameraTarget=(0.0440615, -0.0888247, 0))
p = mdb.models['Model-1'].Part(name='Concrete', dimensionality=THREE_D, 
    type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Concrete']
p.BaseSolidExtrude(sketch=s1, depth=1.2)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Concrete']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.07824, 
    farPlane=3.57651, width=1.42553, height=0.698607, cameraPosition=(0.864317, 
    1.40256, 2.89861), cameraUpVector=(-0.806439, 0.447848, -0.386121))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.11918, 
    farPlane=3.51996, width=1.45361, height=0.712371, cameraPosition=(1.35705, 
    1.40998, 2.63078), cameraUpVector=(-0.807127, 0.514934, -0.288771), 
    cameraTarget=(-0.0150613, -0.0333176, 0.649901))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.35897, 
    farPlane=3.24052, width=1.61809, height=0.792978, cameraPosition=(2.5454, 
    0.866595, 1.38223), cameraUpVector=(-0.618584, 0.781477, -0.0815341), 
    cameraTarget=(-0.0105463, -0.0353821, 0.645157))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.39233, 
    farPlane=3.19837, width=1.64097, height=0.804191, cameraPosition=(2.60445, 
    0.869285, 1.12769), cameraUpVector=(-0.603909, 0.784834, -0.139031), 
    cameraTarget=(-0.0107386, -0.0353909, 0.645986))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Top'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.34203, 
    farPlane=2.78047, width=1.2755, height=0.625082, viewOffsetX=0.0129654, 
    viewOffsetY=0.00112862)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.34851, 
    farPlane=2.77399, width=1.27903, height=0.626812, viewOffsetX=0.0130012, 
    viewOffsetY=0.00113175)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29335, 
    farPlane=2.82744, width=1.24899, height=0.612089, cameraPosition=(2.54769, 
    0.1885, 0.771361), cameraUpVector=(-0.0703642, 0.996452, -0.0461863), 
    cameraTarget=(-0.000906419, 0.00058927, 0.60001), viewOffsetX=0.0126958, 
    viewOffsetY=0.00110517)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29717, 
    farPlane=2.82297, width=1.25107, height=0.613109, cameraPosition=(2.55072, 
    0.0323947, 0.816124), cameraUpVector=(-0.0137207, 0.999839, 0.0115502), 
    cameraTarget=(-0.00117871, -0.000127114, 0.599919), viewOffsetX=0.0127169, 
    viewOffsetY=0.00110701)
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.34135, 
    farPlane=2.78115, width=1.27512, height=0.624899, viewOffsetX=0.0224179, 
    viewOffsetY=0.00854532)
p = mdb.models['Model-1'].parts['Concrete']
v1 = p.vertices
p.DatumPointByOffset(point=v1[3], vector=(0.0, 0.0, 0.1))
p = mdb.models['Model-1'].parts['Concrete']
v2 = p.vertices
p.DatumPointByOffset(point=v2[2], vector=(0.0, 0.0, 0.1))
p = mdb.models['Model-1'].parts['Concrete']
v1 = p.vertices
p.DatumPointByOffset(point=v1[0], vector=(0.0, 0.0, -0.1))
p = mdb.models['Model-1'].parts['Concrete']
v2 = p.vertices
p.DatumPointByOffset(point=v2[1], vector=(0.0, 0.0, -0.1))
p = mdb.models['Model-1'].parts['Concrete']
v1, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=d1[2], vector=(0.0, 0.0, -0.05))
p = mdb.models['Model-1'].parts['Concrete']
v2, d2 = p.vertices, p.datums
p.DatumPointByMidPoint(point1=d2[3], point2=v2[2])
p = mdb.models['Model-1'].parts['Concrete']
v1, d1 = p.vertices, p.datums
p.DatumPointByMidPoint(point1=d1[5], point2=v1[1])
p = mdb.models['Model-1'].parts['Concrete']
v2, d2 = p.vertices, p.datums
p.DatumPointByMidPoint(point1=v2[0], point2=d2[4])
p = mdb.models['Model-1'].parts['Concrete']
v1 = p.vertices
p.DatumPointByOffset(point=v1[1], vector=(0.0, 0.0, -0.3))
p = mdb.models['Model-1'].parts['Concrete']
v2 = p.vertices
p.DatumPointByOffset(point=v2[0], vector=(0.0, 0.0, 0.3))
p = mdb.models['Model-1'].parts['Concrete']
v1 = p.vertices
p.DatumPointByOffset(point=v1[0], vector=(0.0, 0.0, -0.3))
p = mdb.models['Model-1'].parts['Concrete']
v2, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=d1[10], vector=(0.0, 0.0, 0.05))
p = mdb.models['Model-1'].parts['Concrete']
v1, d2 = p.vertices, p.datums
p.DatumPointByOffset(point=d2[12], vector=(0.0, 0.0, 0.05))
p = mdb.models['Model-1'].parts['Concrete']
v2, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=v2[2], vector=(0.0, 0.0, 0.25))
p = mdb.models['Model-1'].parts['Concrete']
v1, d2 = p.vertices, p.datums
p.DatumPointByOffset(point=v1[3], vector=(0.0, 0.0, 0.25))
p = mdb.models['Model-1'].parts['Concrete']
v2, d1 = p.vertices, p.datums
p.DatumPointByOffset(point=d1[15], vector=(0.0, 0.0, 0.05))
p = mdb.models['Model-1'].parts['Concrete']
v1, d2 = p.vertices, p.datums
p.DatumPointByOffset(point=d2[16], vector=(0.0, 0.0, 0.05))
p = mdb.models['Model-1'].parts['Concrete']
d1 = p.datums
p.DatumPointByMidPoint(point1=d1[7], point2=d1[3])
p = mdb.models['Model-1'].parts['Concrete']
d2 = p.datums
p.DatumPointByMidPoint(point1=d2[6], point2=d2[2])
p = mdb.models['Model-1'].parts['Concrete']
d1 = p.datums
p.DatumPointByMidPoint(point1=d1[16], point2=d1[18])
p = mdb.models['Model-1'].parts['Concrete']
d2 = p.datums
p.DatumPointByMidPoint(point1=d2[17], point2=d2[15])
p = mdb.models['Model-1'].parts['Concrete']
d1 = p.datums
p.DatumPointByMidPoint(point1=d1[13], point2=d1[10])
p = mdb.models['Model-1'].parts['Concrete']
d2 = p.datums
p.DatumPointByMidPoint(point1=d2[12], point2=d2[14])
p = mdb.models['Model-1'].parts['Concrete']
d1 = p.datums
p.DatumPointByMidPoint(point1=d1[4], point2=d1[9])
p = mdb.models['Model-1'].parts['Concrete']
d2 = p.datums
p.DatumPointByMidPoint(point1=d2[5], point2=d2[8])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30056, 
    farPlane=2.82194, width=1.93208, height=0.946853, viewOffsetX=-0.248309, 
    viewOffsetY=0.0272974)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29168, 
    farPlane=2.83082, width=1.92463, height=0.9432, viewOffsetX=0.0483691, 
    viewOffsetY=-0.00331244)
p = mdb.models['Model-1'].parts['Concrete']
del p.features['Datum pt-10']
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.32723, 
    farPlane=2.79527, width=1.4344, height=0.702957, viewOffsetX=0.120238, 
    viewOffsetY=-0.0109625)
p = mdb.models['Model-1'].parts['Concrete']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=d1[8], normal=e[1], cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.33442, 
    farPlane=2.78808, width=1.43884, height=0.70513, cameraPosition=(-2.56125, 
    0.0116215, 0.601579), cameraUpVector=(0, 0.996105, 0.0881782), 
    cameraTarget=(0, 0.0116215, 0.601579), viewOffsetX=0.12061, 
    viewOffsetY=-0.0109964)
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
p = mdb.models['Model-1'].parts['Concrete']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e1, v1, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=d2[4], normal=e1[10], 
    cells=pickedCells)
p = mdb.models['Model-1'].parts['Concrete']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=d1[13], normal=e[4], cells=pickedCells)
p = mdb.models['Model-1'].parts['Concrete']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e1, v1, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=d2[10], normal=e1[16], 
    cells=pickedCells)
p = mdb.models['Model-1'].parts['Concrete']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=d1[17], normal=e[4], cells=pickedCells)
p = mdb.models['Model-1'].parts['Concrete']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
e1, v1, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=d2[15], normal=e1[16], 
    cells=pickedCells)
p = mdb.models['Model-1'].parts['Concrete']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
e, v2, d1 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=d1[3], normal=e[18], cells=pickedCells)
p = mdb.models['Model-1'].parts['Concrete']
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#4 ]', ), )
e1, v1, d2 = p.edges, p.vertices, p.datums
p.PartitionCellByPlanePointNormal(point=d2[7], normal=e1[10], 
    cells=pickedCells)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.27107, 
    farPlane=2.85143, width=1.16264, height=0.569775, cameraPosition=(-2.53174, 
    0.290083, 0.342862), cameraUpVector=(0.112138, 0.993551, 0.0167507), 
    cameraTarget=(-3.72529e-009, -5.40167e-008, 0.6))
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Concrete']
a.Instance(name='Concrete-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.21369, 
    farPlane=3.50365, width=1.51844, height=0.744139, cameraPosition=(-1.93419, 
    0.00285918, 2.70536), cameraUpVector=(-0.272747, 0.636354, -0.72157), 
    cameraTarget=(-0.018288, -0.033366, 0.651655))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.17723, 
    farPlane=3.52436, width=1.49343, height=0.731884, cameraPosition=(-1.87969, 
    0.660565, 2.63937), cameraUpVector=(-0.0550229, 0.660397, -0.748898), 
    cameraTarget=(-0.0173384, -0.0219061, 0.650505))
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['LoadSupporter']
a.Instance(name='LoadSupporter-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.53208, 
    farPlane=2.96701, width=1.30448, height=0.639287, cameraUpVector=(0, 
    0.993989, 0.109483))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.53458, 
    farPlane=2.96451, width=1.30577, height=0.639918, cameraUpVector=(0, 
    0.987191, 0.159541))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.53447, 
    farPlane=2.96463, width=1.30571, height=0.639889, cameraUpVector=(0, 
    0.999943, -0.0106395))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.53447, 
    farPlane=2.96462, width=1.30571, height=0.639889, cameraUpVector=(0, 
    0.997506, -0.070587))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.53447, 
    farPlane=2.96462, width=1.30571, height=0.639889, cameraUpVector=(0, 
    0.999168, -0.0407922))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.53447, 
    farPlane=2.96462, width=1.30571, height=0.639889, viewOffsetX=-0.171608, 
    viewOffsetY=0.00662237)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.53447, 
    farPlane=3.06462, width=1.30571, height=0.639889, cameraPosition=(-2.74955, 
    -0.0196241, 0.549026), cameraUpVector=(0, 0.998028, 0.0627782), 
    cameraTarget=(0, -0.0196241, 0.549026), viewOffsetX=-0.171608, 
    viewOffsetY=0.00662237)
a = mdb.models['Model-1'].rootAssembly
a.rotate(instanceList=('LoadSupporter-1', ), axisPoint=(0.0, -0.025, -0.1), 
    axisDirection=(0.0, 0.025, 0.0), angle=90.0)
#: The instance LoadSupporter-1 was rotated by 90. degrees about the axis defined by the point 0., -25.E-03, -100.E-03 and the vector 0., 25.E-03, 0.
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.24468, 
    farPlane=3.57365, width=1.15642, height=0.566725, cameraPosition=(-2.23431, 
    -0.389612, -1.22208), cameraUpVector=(-0.248765, 0.960123, 0.127594), 
    cameraTarget=(-0.0965417, -0.0613371, 0.475629), viewOffsetX=-0.151987, 
    viewOffsetY=0.00586518)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.25784, 
    farPlane=3.56049, width=1.1632, height=0.570048, cameraPosition=(-2.24409, 
    -0.341127, -1.21914), cameraUpVector=(-0.0968759, 0.992833, -0.0699908), 
    cameraTarget=(-0.106321, -0.012852, 0.478568), viewOffsetX=-0.152878, 
    viewOffsetY=0.00589958)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.25725, 
    farPlane=3.56109, width=1.16289, height=0.569898, cameraPosition=(-2.24588, 
    -0.321154, -1.22074), cameraUpVector=(-0.033041, 0.988213, -0.149479), 
    cameraTarget=(-0.108114, 0.00712069, 0.476963), viewOffsetX=-0.152838, 
    viewOffsetY=0.00589803)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.53958, 
    farPlane=3.10747, width=1.30834, height=0.641178, cameraPosition=(-2.73434, 
    0.476256, 0.597033), cameraUpVector=(0.141731, 0.959064, -0.245172), 
    cameraTarget=(-0.0137589, 0.0785718, 0.6141), viewOffsetX=-0.171954, 
    viewOffsetY=0.00663573)
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.36557, 
    farPlane=2.88248, width=1.20477, height=0.590419, cameraUpVector=(0, 
    0.994951, -0.100361))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.36774, 
    farPlane=2.88031, width=1.20588, height=0.590963, viewOffsetX=-0.149299, 
    viewOffsetY=0.0168191)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.23947, 
    farPlane=3.04305, width=1.14055, height=0.55895, cameraPosition=(-2.3532, 
    1.06831, 0.285386), cameraUpVector=(0.411862, 0.906986, -0.0880165), 
    cameraTarget=(-0.0151775, 0.0364445, 0.592803), viewOffsetX=-0.141211, 
    viewOffsetY=0.0159079)
a = mdb.models['Model-1'].rootAssembly
a.translate(instanceList=('LoadSupporter-1', ), vector=(-0.1, 0.225, 0.375))
#: The instance LoadSupporter-1 was translated by -100.E-03, 225.E-03, 375.E-03 with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30111, 
    farPlane=2.87142, width=1.17195, height=0.574336, cameraPosition=(-2.51594, 
    0.583257, 0.424389), cameraUpVector=(0.219876, 0.965232, 0.141358), 
    cameraTarget=(-0.0167503, -0.0102744, 0.589787), viewOffsetX=-0.145098, 
    viewOffsetY=0.0163458)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.28725, 
    farPlane=2.92132, width=1.16489, height=0.570877, cameraPosition=(-2.55384, 
    -0.015877, 0.0898004), cameraUpVector=(-0.0263421, 0.99065, 0.133858), 
    cameraTarget=(-0.0280513, -0.0157351, 0.585778), viewOffsetX=-0.144224, 
    viewOffsetY=0.0162474)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.261, 
    farPlane=2.94758, width=1.3864, height=0.679433, viewOffsetX=-0.125357, 
    viewOffsetY=0.0283127)
a = mdb.models['Model-1'].rootAssembly
a.LinearInstancePattern(instanceList=('LoadSupporter-1', ), direction1=(1.0, 
    0.0, 0.0), direction2=(0.0, 1.0, 0.0), number1=2, number2=2, spacing1=0.2, 
    spacing2=0.0199999999153)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.27893, 
    farPlane=3.1076, width=1.39739, height=0.684819, cameraPosition=(-2.55253, 
    0.407638, 0.336783), cameraUpVector=(0.1363, 0.969578, 0.203323), 
    cameraTarget=(-0.0245186, -0.0020074, 0.595537), viewOffsetX=-0.126351, 
    viewOffsetY=0.0285371)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.25424, 
    farPlane=3.13875, width=1.38225, height=0.677398, cameraPosition=(-2.27603, 
    1.2852, 0.440828), cameraUpVector=(0.471199, 0.875537, -0.106806), 
    cameraTarget=(-0.00577698, 0.0843532, 0.612722), viewOffsetX=-0.124982, 
    viewOffsetY=0.0282279)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.16218, 
    farPlane=3.1581, width=1.3258, height=0.649733, cameraPosition=(-2.33675, 
    0.948227, 1.12717), cameraUpVector=(0.378551, 0.921481, 0.0870119), 
    cameraTarget=(0.0163591, 0.0279649, 0.635605), viewOffsetX=-0.119878, 
    viewOffsetY=0.0270751)
a = mdb.models['Model-1'].rootAssembly
a.deleteFeatures(('LoadSupporter-1-lin-2-2', 'LoadSupporter-1-lin-2-1', ))
a1 = mdb.models['Model-1'].rootAssembly
a1.LinearInstancePattern(instanceList=('LoadSupporter-1-lin-1-2', ), 
    direction1=(1.0, 0.0, 0.0), direction2=(0.0, 1.0, 0.0), number1=1, 
    number2=2, spacing1=0.2, spacing2=0.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.16695, 
    farPlane=2.9705, width=1.32873, height=0.651168, cameraPosition=(-2.34664, 
    0.927874, 1.11795), cameraUpVector=(0.397409, 0.883256, 0.248846), 
    cameraTarget=(0.00647276, 0.00761159, 0.626383), viewOffsetX=-0.120143, 
    viewOffsetY=0.0271349)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.16299, 
    farPlane=2.93751, width=1.3263, height=0.649977, cameraPosition=(-2.45207, 
    0.337992, 1.22549), cameraUpVector=(0.233018, 0.868917, 0.436676), 
    cameraTarget=(0.0217927, -0.0152774, 0.60834), viewOffsetX=-0.119923, 
    viewOffsetY=0.0270853)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30433, 
    farPlane=2.8518, width=1.41297, height=0.69245, cameraPosition=(-2.54914, 
    0.399948, 0.527456), cameraUpVector=(0.134786, 0.9599, 0.245814), 
    cameraTarget=(-0.00630561, 0.0152307, 0.635464), viewOffsetX=-0.127759, 
    viewOffsetY=0.0288552)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29669, 
    farPlane=2.85944, width=1.40829, height=0.690155, cameraPosition=(-2.54875, 
    0.402972, 0.528962), cameraUpVector=(0.136537, 0.965146, 0.223275), 
    cameraTarget=(-0.00591209, 0.0182544, 0.63697), viewOffsetX=-0.127336, 
    viewOffsetY=0.0287596)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.40217, 
    farPlane=2.75397, width=0.203369, height=0.0996648, viewOffsetX=0.196324, 
    viewOffsetY=0.198386)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('LoadSupporter-1-lin-1-2-lin-1-2', ), vector=(0.0, 
    -0.045, 0.65))
#: The instance LoadSupporter-1-lin-1-2-lin-1-2 was translated by 0., -45.E-03, 650.E-03 with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('LoadSupporter-1-lin-1-2-lin-1-2', ), vector=(0.0, 
    0.005, 0.0))
#: The instance LoadSupporter-1-lin-1-2-lin-1-2 was translated by 0., 5.E-03, 0. with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.35561, 
    farPlane=2.80054, width=0.790793, height=0.387544, viewOffsetX=0.264706, 
    viewOffsetY=0.136712)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.35165, 
    farPlane=2.80449, width=0.789466, height=0.386893, cameraPosition=(
    -2.56606, 0.301623, 0.575481), cameraUpVector=(0.15354, 0.980574, 
    -0.122067), cameraTarget=(-0.0232217, -0.0830951, 0.683489), 
    viewOffsetX=0.264262, viewOffsetY=0.136482)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.26817, 
    farPlane=2.88798, width=1.84051, height=0.901977, viewOffsetX=0.436054, 
    viewOffsetY=-0.0263497)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.25902, 
    farPlane=2.89713, width=1.83309, height=0.898339, viewOffsetX=-0.130179, 
    viewOffsetY=0.0632419)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.3142, 
    farPlane=2.84194, width=1.14469, height=0.560978, viewOffsetX=-0.237545, 
    viewOffsetY=0.168999)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.2959, 
    farPlane=2.87537, width=1.13564, height=0.55654, cameraPosition=(-2.42939, 
    0.916704, 0.62592), cameraUpVector=(0.392298, 0.91888, -0.0419647), 
    cameraTarget=(-0.0616921, -0.0921086, 0.670449), viewOffsetX=-0.235666, 
    viewOffsetY=0.167662)
a1 = mdb.models['Model-1'].rootAssembly
a1.rotate(instanceList=('LoadSupporter-1-lin-1-2', ), axisPoint=(-0.1, 0.24, 
    0.275), axisDirection=(0.2, 0.0, 0.0), angle=180.0)
#: The instance LoadSupporter-1-lin-1-2 was rotated by 180. degrees about the axis defined by the point -100.E-03, 240.E-03, 275.E-03 and the vector 200.E-03, 0., 0.
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.33145, 
    farPlane=2.7992, width=1.15323, height=0.565161, cameraPosition=(-2.55902, 
    0.235426, 0.70647), cameraUpVector=(0.124967, 0.986258, -0.108068), 
    cameraTarget=(-0.00585825, -0.0907846, 0.681827), viewOffsetX=-0.239315, 
    viewOffsetY=0.170258)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29848, 
    farPlane=2.83347, width=1.13692, height=0.557168, cameraPosition=(-2.52729, 
    0.481818, 0.734463), cameraUpVector=(0.229963, 0.972837, -0.0265567), 
    cameraTarget=(-0.0235393, -0.111853, 0.667788), viewOffsetX=-0.23593, 
    viewOffsetY=0.16785)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.28251, 
    farPlane=2.86849, width=1.12902, height=0.553297, cameraPosition=(-2.53157, 
    -0.44765, 0.399349), cameraUpVector=(-0.125925, 0.988974, -0.0779325), 
    cameraTarget=(0.00429913, -0.103007, 0.675444), viewOffsetX=-0.23429, 
    viewOffsetY=0.166683)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.35383, 
    farPlane=2.7688, width=1.1643, height=0.570586, cameraPosition=(-2.55753, 
    -0.176196, 0.668441), cameraUpVector=(-0.0283446, 0.997118, -0.0703733), 
    cameraTarget=(0.0154358, -0.102536, 0.675853), viewOffsetX=-0.241611, 
    viewOffsetY=0.171891)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('LoadSupporter-1-lin-1-2', ), vector=(0.0, -0.46, 
    -0.2))
#: The instance LoadSupporter-1-lin-1-2 was translated by 0., -460.E-03, -200.E-03 with respect to the assembly coordinate system
a1 = mdb.models['Model-1'].rootAssembly
a1.LinearInstancePattern(instanceList=('LoadSupporter-1-lin-1-2', ), 
    direction1=(1.0, 0.0, 0.0), direction2=(0.0, 1.0, 0.0), number1=2, 
    number2=1, spacing1=0.2, spacing2=0.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.35086, 
    farPlane=2.97169, width=1.16283, height=0.569867, cameraPosition=(-2.55937, 
    -0.114728, 0.69785), cameraUpVector=(-0.0267706, 0.962293, -0.270693), 
    cameraTarget=(0.0135914, -0.0410683, 0.705262), viewOffsetX=-0.241306, 
    viewOffsetY=0.171674)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.33041, 
    farPlane=2.9896, width=1.15272, height=0.564911, cameraPosition=(-2.55271, 
    -0.216745, 0.674761), cameraUpVector=(-0.0696926, 0.916668, -0.393527), 
    cameraTarget=(0.0121727, -0.00399723, 0.716104), viewOffsetX=-0.239207, 
    viewOffsetY=0.170181)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.11519, 
    farPlane=3.24491, width=1.04626, height=0.51274, cameraPosition=(-1.87298, 
    -1.67521, -0.104981), cameraUpVector=(-0.489722, 0.775323, -0.398806), 
    cameraTarget=(-0.00156775, -0.0906142, 0.677623), viewOffsetX=-0.217116, 
    viewOffsetY=0.154464)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.03893, 
    farPlane=3.32117, width=2.13651, height=1.04704, viewOffsetX=-0.126848, 
    viewOffsetY=0.331679)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.02945, 
    farPlane=3.33065, width=2.12658, height=1.04217, viewOffsetX=0.0290151, 
    viewOffsetY=0.137343)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.09902, 
    farPlane=3.26108, width=1.26029, height=0.61763, viewOffsetX=-0.208518, 
    viewOffsetY=0.122327)
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('LoadSupporter-1-lin-1-2-lin-2-1', ), vector=(-0.2, 
    0.02, 0.525))
#: The instance LoadSupporter-1-lin-1-2-lin-2-1 was translated by -200.E-03, 20.E-03, 525.E-03 with respect to the assembly coordinate system
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.19526, 
    farPlane=2.878, width=1.31807, height=0.645947, cameraPosition=(-2.05294, 
    -1.48426, 0.767636), cameraUpVector=(-0.427373, 0.530702, -0.731921), 
    cameraTarget=(0.00119469, 0.065038, 0.691589), viewOffsetX=-0.218078, 
    viewOffsetY=0.127936)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.91589, 
    farPlane=2.94373, width=1.15033, height=0.563742, cameraPosition=(-2.03615, 
    -0.00990408, 1.93324), cameraUpVector=(-0.419378, 0.61151, -0.670953), 
    cameraTarget=(0.181534, 0.0807233, 0.629687), viewOffsetX=-0.190325, 
    viewOffsetY=0.111655)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.59715, 
    farPlane=3.05477, width=0.958952, height=0.469954, cameraPosition=(
    -0.209096, 1.36216, 2.48425), cameraUpVector=(-0.542825, 0.635999, 
    -0.548494), cameraTarget=(0.228769, -0.0697469, 0.390569), 
    viewOffsetX=-0.158661, viewOffsetY=0.0930792)
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.43245, 
    farPlane=2.74226, width=0.586423, height=0.287388, viewOffsetX=0.0101919, 
    viewOffsetY=-0.120031)
a = mdb.models['Model-1'].rootAssembly
f1 = a.instances['Concrete-1'].faces
faces1 = f1.getSequenceFromMask(mask=('[#4000000 ]', ), )
leaf = dgm.LeafFromGeometry(faceSeq=faces1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.either(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.39515, 
    farPlane=2.77956, width=1.11036, height=0.544155, viewOffsetX=0.00227022, 
    viewOffsetY=-0.0543909)
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
a = mdb.models['Model-1'].rootAssembly
c1 = a.instances['Concrete-1'].cells
cells1 = c1.getSequenceFromMask(mask=('[#20 ]', ), )
leaf = dgm.LeafFromGeometry(cellSeq=cells1)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.36284, 
    farPlane=2.81187, width=1.49865, height=0.734444, viewOffsetX=-0.140758, 
    viewOffsetY=0.00877188)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1.95381, 
    farPlane=3.50307, width=1.23922, height=0.607304, cameraPosition=(
    -0.528969, 0.911956, 3.12567), cameraUpVector=(0.507231, 0.836075, 
    -0.209033), cameraTarget=(0.122172, -0.0600491, 0.817942), 
    viewOffsetX=-0.116392, viewOffsetY=0.00725338)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.22478, 
    farPlane=3.18574, width=1.41109, height=0.691531, cameraPosition=(-2.36717, 
    0.401894, 1.8638), cameraUpVector=(0.28791, 0.932944, 0.216158), 
    cameraTarget=(-0.0461487, -0.0734539, 0.823953), viewOffsetX=-0.132534, 
    viewOffsetY=0.00825935)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.24172, 
    farPlane=3.12081, width=1.42183, height=0.696795, cameraPosition=(-2.58025, 
    0.326221, -0.0800937), cameraUpVector=(0.159381, 0.985133, -0.0641077), 
    cameraTarget=(-0.153318, -0.0123774, 0.750413), viewOffsetX=-0.133543, 
    viewOffsetY=0.00832222)
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
mdb.save()
#: The model database has been saved to "C:\Users\Ray\Desktop\abaqusGui\model\caeModel.cae".
a1 = mdb.models['Model-1'].rootAssembly
a1.translate(instanceList=('LoadSupporter-1-lin-1-2-lin-2-1', ), vector=(0.0, 
    -0.02, 0.525))
#: The instance LoadSupporter-1-lin-1-2-lin-2-1 was translated by 0., -20.E-03, 525.E-03 with respect to the assembly coordinate system
leaf = dgm.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
    leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.29491, 
    farPlane=2.8798, width=1.16251, height=0.569712, cameraPosition=(-2.55112, 
    0.361435, 0.364343), cameraUpVector=(0.136155, 0.98971, 0.0439943), 
    cameraTarget=(-7.45058e-009, -6.70552e-008, 0.6))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
    constraints=ON, connectors=ON, engineeringFeatures=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30065, 
    farPlane=2.87405, width=1.16542, height=0.571136, cameraPosition=(-2.55112, 
    0.361435, 0.364343), cameraUpVector=(0.138099, 0.990137, 0.0236009), 
    cameraTarget=(-7.567e-009, -6.70552e-008, 0.6))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30066, 
    farPlane=2.87404, width=1.16542, height=0.571138, cameraPosition=(-2.55112, 
    0.361435, 0.364343), cameraUpVector=(0.140145, 0.99013, 0.00144217), 
    cameraTarget=(-7.567e-009, -6.79865e-008, 0.6))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.35913, 
    farPlane=2.81557, width=0.472391, height=0.231504, viewOffsetX=-0.20055, 
    viewOffsetY=0.119345)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.36174, 
    farPlane=2.81296, width=0.472912, height=0.23176, cameraPosition=(-2.55376, 
    0.326585, 0.339434), cameraUpVector=(0.123073, 0.978106, 0.167815), 
    cameraTarget=(-0.00263648, -0.0348498, 0.575091), viewOffsetX=-0.200772, 
    viewOffsetY=0.119477)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30482, 
    farPlane=2.86988, width=1.18676, height=0.581592, viewOffsetX=-0.107496, 
    viewOffsetY=0.0808446)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30397, 
    farPlane=2.87157, width=1.18631, height=0.581376, cameraPosition=(-2.542, 
    0.44312, 0.39962), cameraUpVector=(0.171331, 0.971955, 0.161086), 
    cameraTarget=(-0.00501481, -0.0333275, 0.576061), viewOffsetX=-0.107456, 
    viewOffsetY=0.0808146)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30374, 
    farPlane=2.87181, width=1.18619, height=0.581318, cameraPosition=(-2.5418, 
    0.444806, 0.401356), cameraUpVector=(0.172851, 0.974181, 0.145237), 
    cameraTarget=(-0.00481888, -0.0316414, 0.577797), viewOffsetX=-0.107445, 
    viewOffsetY=0.0808065)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Concrete-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#800000 ]', ), )
region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-1')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['LoadSupporter-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-1')
mdb.models['Model-1'].Tie(name='Constraint-1', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
del mdb.models['Model-1'].constraints['Constraint-1']
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.39503, 
    farPlane=2.7805, width=0.141419, height=0.0693053, viewOffsetX=-0.280938, 
    viewOffsetY=0.166066)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.23142, 
    farPlane=2.84147, width=0.131759, height=0.0645708, cameraPosition=(
    -2.40155, 0.741617, 0.993067), cameraUpVector=(0.395807, 0.726802, 
    0.561334), cameraTarget=(-0.0272653, -0.129279, 0.446529), 
    viewOffsetX=-0.261746, viewOffsetY=0.154722)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Concrete-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#800000 ]', ), )
region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-3')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['LoadSupporter-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-3')
mdb.models['Model-1'].Tie(name='up1', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.21408, 
    farPlane=2.85879, width=0.359098, height=0.175983, viewOffsetX=-0.257377, 
    viewOffsetY=0.156012)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.21226, 
    farPlane=2.86062, width=0.358802, height=0.175838, viewOffsetX=-0.254203, 
    viewOffsetY=0.154519)
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.37889, 
    farPlane=2.79582, width=1.20505, height=0.59056, cameraUpVector=(0, 
    0.998337, -0.0576428))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.00524, 
    farPlane=3.16947, width=1.01578, height=0.497802, cameraPosition=(-1.92925, 
    1.1004, 1.92722), cameraUpVector=(0.564277, 0.812461, 0.146626), 
    cameraTarget=(2.38419e-007, 4.17233e-007, 0.600001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.19169, 
    farPlane=2.98302, width=1.11023, height=0.544087, cameraPosition=(-2.41265, 
    0.635961, 1.28488), cameraUpVector=(0.309225, 0.921945, 0.233233), 
    cameraTarget=(-1.3411e-007, 4.74975e-008, 0.600001))
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.23085, 
    farPlane=2.94385, width=0.537822, height=0.26357, viewOffsetX=0.125797, 
    viewOffsetY=0.122566)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.23381, 
    farPlane=2.9409, width=0.538535, height=0.263919, cameraPosition=(-2.41321, 
    0.63031, 1.28815), cameraUpVector=(0.303058, 0.931098, 0.203008), 
    cameraTarget=(-0.000560868, -0.00565127, 0.603273), viewOffsetX=0.125964, 
    viewOffsetY=0.122729)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.09754, 
    farPlane=3.28868, width=0.505683, height=0.247819, cameraPosition=(
    -1.67164, 1.23059, 2.31612), cameraUpVector=(0.618286, 0.785583, 
    0.0241481), cameraTarget=(-0.0886734, 0.0358015, 0.654464), 
    viewOffsetX=0.11828, viewOffsetY=0.115242)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.10553, 
    farPlane=3.2807, width=0.421612, height=0.206619, viewOffsetX=0.108907, 
    viewOffsetY=0.109942)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Concrete-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #2 ]', ), )
region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-5')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['LoadSupporter-1-lin-1-2-lin-1-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-5')
mdb.models['Model-1'].Tie(name='up2', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.10781, 
    farPlane=3.27842, width=0.422069, height=0.206843, viewOffsetX=0.0640046, 
    viewOffsetY=0.0503901)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.10781, 
    farPlane=3.27842, width=0.42207, height=0.206843, viewOffsetX=-0.00727817, 
    viewOffsetY=-0.0416591)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.10781, 
    farPlane=3.27842, width=0.42207, height=0.206843, viewOffsetX=-0.114203, 
    viewOffsetY=-0.121667)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.10781, 
    farPlane=3.27842, width=0.42207, height=0.206843, viewOffsetX=-0.158152, 
    viewOffsetY=-0.155115)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.12076, 
    farPlane=3.26547, width=0.258861, height=0.12686, viewOffsetX=-0.188863, 
    viewOffsetY=-0.153703)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.3463, 
    farPlane=3.24167, width=0.286391, height=0.140351, cameraPosition=(
    -2.34924, 0.15884, 2.11409), cameraUpVector=(-0.0451965, 0.996331, 
    -0.072672), cameraTarget=(-0.222559, 0.147823, 0.640496), 
    viewOffsetX=-0.208948, viewOffsetY=-0.170049)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.34391, 
    farPlane=3.24404, width=0.286099, height=0.140208, viewOffsetX=-0.24016, 
    viewOffsetY=-0.205426)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.34391, 
    farPlane=3.24405, width=0.286098, height=0.140208, viewOffsetX=-0.257416, 
    viewOffsetY=-0.232996)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.59619, 
    farPlane=3.32797, width=0.316892, height=0.155299, cameraPosition=(
    -2.71437, -1.00543, 1.29484), cameraUpVector=(-0.467876, 0.870636, 
    -0.151935), cameraTarget=(-0.470969, 0.0783921, 0.597071), 
    viewOffsetX=-0.285123, viewOffsetY=-0.258074)
session.viewports['Viewport: 1'].view.setValues(width=0.297568, 
    height=0.145829, viewOffsetX=-0.289752, viewOffsetY=-0.259666)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.59517, 
    farPlane=3.329, width=0.297762, height=0.145924, viewOffsetX=-0.347035, 
    viewOffsetY=-0.314579)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.59517, 
    farPlane=3.329, width=0.297762, height=0.145924, viewOffsetX=-0.361214, 
    viewOffsetY=-0.336477)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Concrete-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#40 ]', ), )
region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-7')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['LoadSupporter-1-lin-1-2'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-7')
mdb.models['Model-1'].Tie(name='Down1', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.49982, 
    farPlane=3.29963, width=0.286822, height=0.140563, cameraPosition=(
    -2.72885, -0.615332, 1.45727), cameraUpVector=(-0.437366, 0.828213, 
    -0.350392), cameraTarget=(-0.455321, 0.188589, 0.51963), 
    viewOffsetX=-0.347942, viewOffsetY=-0.324114)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50077, 
    farPlane=3.29868, width=0.286932, height=0.140617, viewOffsetX=-0.299251, 
    viewOffsetY=-0.353161)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50077, 
    farPlane=3.29868, width=0.286932, height=0.140617, viewOffsetX=-0.203243, 
    viewOffsetY=-0.403551)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50077, 
    farPlane=3.29868, width=0.286932, height=0.140617, viewOffsetX=-0.0720742, 
    viewOffsetY=-0.442844)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50077, 
    farPlane=3.29868, width=0.286932, height=0.140617, viewOffsetX=0.0137322, 
    viewOffsetY=-0.490141)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50077, 
    farPlane=3.29868, width=0.286932, height=0.140617, viewOffsetX=0.111016, 
    viewOffsetY=-0.556357)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50077, 
    farPlane=3.29868, width=0.286932, height=0.140617, viewOffsetX=0.225789, 
    viewOffsetY=-0.608384)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50077, 
    farPlane=3.29868, width=0.286932, height=0.140617, viewOffsetX=0.32362, 
    viewOffsetY=-0.628941)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50077, 
    farPlane=3.29868, width=0.286932, height=0.140617, viewOffsetX=0.394488, 
    viewOffsetY=-0.671873)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50077, 
    farPlane=3.29868, width=0.286932, height=0.140617, viewOffsetX=0.37372, 
    viewOffsetY=-0.67533)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.51047, 
    farPlane=3.11262, width=0.288046, height=0.141163, cameraPosition=(-2.7563, 
    -0.602113, 0.957117), cameraUpVector=(-0.38229, 0.884451, -0.267584), 
    cameraTarget=(-0.371795, 0.287691, 0.491544), viewOffsetX=0.37517, 
    viewOffsetY=-0.67795)
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['Concrete-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#0 #1 ]', ), )
region1=a.Surface(side1Faces=side1Faces1, name='m_Surf-9')
a = mdb.models['Model-1'].rootAssembly
s1 = a.instances['LoadSupporter-1-lin-1-2-lin-2-1'].faces
side1Faces1 = s1.getSequenceFromMask(mask=('[#3 ]', ), )
region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-9')
mdb.models['Model-1'].Tie(name='Down2', master=region1, slave=region2, 
    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON, thickness=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.50873, 
    farPlane=3.07242, width=0.287848, height=0.141065, cameraPosition=(
    -2.78782, -0.260285, 1.06912), cameraUpVector=(-0.286489, 0.956141, 
    -0.0609756), cameraTarget=(-0.337654, 0.445884, 0.630507), 
    viewOffsetX=0.374911, viewOffsetY=-0.677481)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.31802, 
    farPlane=3.26313, width=2.58063, height=1.26469, viewOffsetX=0.76305, 
    viewOffsetY=-0.440345)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, interactions=OFF, constraints=OFF, 
    engineeringFeatures=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.30779, 
    farPlane=3.27336, width=2.56925, height=1.25911, viewOffsetX=0.136539, 
    viewOffsetY=-0.41397)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.49095, 
    farPlane=3.09021, width=0.46098, height=0.225912, viewOffsetX=-0.3882, 
    viewOffsetY=-0.586298)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.49345, 
    farPlane=3.0877, width=0.461443, height=0.226139, cameraPosition=(-2.78577, 
    -0.263524, 1.07534), cameraUpVector=(-0.285127, 0.957086, -0.0518475), 
    cameraTarget=(-0.335606, 0.442645, 0.63673), viewOffsetX=-0.38859, 
    viewOffsetY=-0.586887)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.58503, 
    farPlane=3.46308, width=0.478391, height=0.234445, cameraPosition=(
    -2.77691, -0.645759, -0.556711), cameraUpVector=(-0.357415, 0.923193, 
    -0.141313), cameraTarget=(-0.603201, 0.347533, 0.43462), 
    viewOffsetX=-0.402862, viewOffsetY=-0.608442)
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['LoadSupporter-1-lin-1-2'].referencePoints
refPoints1=(r1[3], )
region = a.Set(referencePoints=refPoints1, name='Set-1')
mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', 
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.58357, 
    farPlane=3.46456, width=0.478121, height=0.234312, cameraPosition=(
    -2.76169, -0.602412, -0.633522), cameraUpVector=(-0.312736, 0.920026, 
    -0.236109), cameraTarget=(-0.587979, 0.39088, 0.357809), 
    viewOffsetX=-0.402634, viewOffsetY=-0.608097)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-0.228992, 
    viewOffsetY=-0.649321)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-0.0647614, 
    viewOffsetY=-0.690545)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=0.150469, 
    viewOffsetY=-0.719341)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=0.254897, 
    viewOffsetY=-0.736922)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=0.294361, 
    viewOffsetY=-0.745409)
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['LoadSupporter-1-lin-1-2-lin-2-1'].referencePoints
refPoints1=(r1[3], )
region = a.Set(referencePoints=refPoints1, name='Set-2')
mdb.models['Model-1'].DisplacementBC(name='BC-2', createStepName='Initial', 
    region=region, u1=SET, u2=SET, u3=SET, ur1=SET, ur2=SET, ur3=SET, 
    amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.86644, 
    farPlane=3.3701, width=0.530469, height=0.259967, cameraPosition=(-3.20642, 
    0.0527072, 0.483893), cameraUpVector=(-0.221907, 0.965131, 0.138851), 
    cameraTarget=(-0.691816, 0.589382, 0.772254), viewOffsetX=0.32659, 
    viewOffsetY=-0.827022)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
    description='load')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.8619, 
    farPlane=3.37464, width=0.52963, height=0.259555, viewOffsetX=0.145831, 
    viewOffsetY=-0.687708)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.8619, 
    farPlane=3.37464, width=0.52963, height=0.259555, viewOffsetX=0.113213, 
    viewOffsetY=-0.572201)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.8619, 
    farPlane=3.37464, width=0.52963, height=0.259555, viewOffsetX=0.110187, 
    viewOffsetY=-0.45938)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.8619, 
    farPlane=3.37464, width=0.52963, height=0.259555, viewOffsetX=0.103462, 
    viewOffsetY=-0.413379)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.96313, 
    farPlane=3.42197, width=0.548364, height=0.268736, cameraPosition=(
    -3.12609, 0.963632, 0.46072), cameraUpVector=(0.0766577, 0.994588, 
    0.0701322), cameraTarget=(-0.563264, 0.746267, 0.741918), 
    viewOffsetX=0.107122, viewOffsetY=-0.428001)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.9615, 
    farPlane=3.42359, width=0.548063, height=0.268589, viewOffsetX=0.0232009, 
    viewOffsetY=-0.432283)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.9615, 
    farPlane=3.42359, width=0.548063, height=0.268589, viewOffsetX=-0.105551, 
    viewOffsetY=-0.451046)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.9615, 
    farPlane=3.42359, width=0.548063, height=0.268589, viewOffsetX=-0.193589, 
    viewOffsetY=-0.459038)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.9615, 
    farPlane=3.42359, width=0.548063, height=0.268589, viewOffsetX=-0.275712, 
    viewOffsetY=-0.450699)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.9615, 
    farPlane=3.42359, width=0.548063, height=0.268589, viewOffsetX=-0.294851, 
    viewOffsetY=-0.463903)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['LoadSupporter-1'].referencePoints
refPoints1=(r1[3], )
region = a.Set(referencePoints=refPoints1, name='Set-3')
mdb.models['Model-1'].DisplacementBC(name='BC-3', createStepName='Step-1', 
    region=region, u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
    localCsys=None)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.9615, 
    farPlane=3.42359, width=0.548064, height=0.268589, viewOffsetX=-0.168536, 
    viewOffsetY=-0.463903)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.9615, 
    farPlane=3.42359, width=0.548064, height=0.268589, viewOffsetX=-0.0578793, 
    viewOffsetY=-0.454869)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.9615, 
    farPlane=3.42359, width=0.548064, height=0.268589, viewOffsetX=0.0214595, 
    viewOffsetY=-0.437149)
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['LoadSupporter-1-lin-1-2-lin-1-2'].referencePoints
refPoints1=(r1[3], )
region = a.Set(referencePoints=refPoints1, name='Set-4')
mdb.models['Model-1'].DisplacementBC(name='BC-4', createStepName='Step-1', 
    region=region, u1=UNSET, u2=0.0, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
    localCsys=None)
mdb.models['Model-1'].boundaryConditions['BC-3'].setValues(u2=0.02)
mdb.models['Model-1'].boundaryConditions['BC-4'].setValues(u2=0.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.9033, 
    farPlane=3.4818, width=1.2829, height=0.628712, viewOffsetX=0.169912, 
    viewOffsetY=-0.476224)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.89699, 
    farPlane=3.4881, width=1.28012, height=0.627347, cameraPosition=(-3.11649, 
    0.906178, 0.328812), cameraUpVector=(0.103392, 0.976861, -0.187223), 
    cameraTarget=(-0.553664, 0.688813, 0.61001), viewOffsetX=0.169543, 
    viewOffsetY=-0.47519)
mdb.models['Model-1'].boundaryConditions['BC-4'].setValues(u2=-0.02)
mdb.models['Model-1'].boundaryConditions['BC-3'].setValues(u2=-0.02)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.89699, 
    farPlane=3.48811, width=1.28012, height=0.627347, cameraPosition=(-3.11423, 
    0.878203, 0.286603), cameraUpVector=(0.111199, 0.95489, -0.275356), 
    cameraTarget=(-0.551405, 0.660838, 0.567801), viewOffsetX=0.169543, 
    viewOffsetY=-0.475189)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.80452, 
    farPlane=3.58057, width=2.46775, height=1.20937, viewOffsetX=0.449723, 
    viewOffsetY=-0.58098)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
    bcs=OFF, predefinedFields=OFF, connectors=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)
p = mdb.models['Model-1'].parts['Concrete']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p = mdb.models['Model-1'].parts['Concrete']
p.seedPart(size=0.05, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['Concrete']
p.generateMesh()
p = mdb.models['Model-1'].parts['LoadSupporter']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.92498, 
    farPlane=3.46011, width=0.906329, height=0.444164, viewOffsetX=-0.0977441, 
    viewOffsetY=-0.363273)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.92979, 
    farPlane=3.4553, width=0.90782, height=0.444895, cameraPosition=(-3.11521, 
    0.878348, 0.29562), cameraUpVector=(0.10939, 0.960949, -0.254188), 
    cameraTarget=(-0.552382, 0.660983, 0.576818), viewOffsetX=-0.0979049, 
    viewOffsetY=-0.363871)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
#: Warning: Some of the entities selected belong to an analytical rigid part instance. All selected entities must belong to that instance.
session.viewports['Viewport: 1'].view.setValues(nearPlane=2.91382, 
    farPlane=3.47128, width=1.15642, height=0.566725, viewOffsetX=-0.127877, 
    viewOffsetY=-0.381468)
a = mdb.models['Model-1'].rootAssembly
r1 = a.instances['LoadSupporter-1-lin-1-2-lin-1-2'].referencePoints
refPoints1=(r1[3], )
r2 = a.instances['LoadSupporter-1'].referencePoints
refPoints2=(r2[3], )
a.Set(referencePoints=(refPoints1, refPoints2, ), name='up')
#: The set 'up' has been created (2 reference points).
regionDef=mdb.models['Model-1'].rootAssembly.sets['up']
mdb.models['Model-1'].HistoryOutputRequest(name='H-Output-2', 
    createStepName='Step-1', variables=('RF1', 'RF2', 'RF3'), region=regionDef, 
    sectionPoints=DEFAULT, rebar=EXCLUDE)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', multiprocessingMode=DEFAULT, numCpus=4, numDomains=4, 
    numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
