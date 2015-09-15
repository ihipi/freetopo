import FreeCAD, FreeCADGui, Part, Draft
from Part import Point
from FreeCAD import Base
from pivy import coin


class Point(Point):
    def __init__(self, obj,x=0.0,y=0.0,z=0.0):
        obj.Vector=FreeCAD.Vector(x,y,z)

        Point.__init__(self,obj.Vector)
        obj.Proxy = self
        
        
    def onChanged(self, fp, prop):
        ''' Print the name of the property that has changed '''
        return

    def execute(self, fp):
        ''' Print a short message when doing a recomputation, this method is mandatory '''
        return

class ViewProviderPoints:
    def __init__(self, obj):
        ''' Set this object to the proxy object of the actual view provider '''
        obj.Proxy = self

    def attach(self, obj):
        ''' Setup the scene sub-graph of the view provider, this method is mandatory '''
        return

    def updateData(self, fp, prop):
        ''' If a property of the handled feature has changed we have the chance to handle this here '''
        return

    def getDisplayModes(self,obj):
        ''' Return a list of display modes. '''
        modes=[]
        return modes

    def getDefaultDisplayMode(self):
        ''' Return the name of the default display mode. It must be defined in getDisplayModes. '''
        return "Points"

    def setDisplayMode(self,mode):
        ''' Map the display mode defined in attach with those defined in getDisplayModes.
        Since they have the same names nothing needs to be done. This method is optinal.
        '''
        return mode

    def onChanged(self, vp, prop):
        ''' Print the name of the property that has changed '''
        return

    def getIcon(self):
        ''' Return the icon in XMP format which will appear in the tree view. This method is optional
        and if not defined a default icon is shown.
        '''
        return """
            /* XPM */
            static const char * ViewProviderBox_xpm[] = {
            "16 16 6 1",
            "     c None",
            ".    c #141010",
            "+    c #615BD2",
            "@    c #C39D55",
            "#    c #000000",
            "$    c #57C355",
            "        ........",
            "   ......++..+..",
            "   .@@@@.++..++.",
            "   .@@@@.++..++.",
            "   .@@  .++++++.",
            "  ..@@  .++..++.",
            "###@@@@ .++..++.",
            "##$.@@$#.++++++.",
            "#$#$.$$$........",
            "#$$#######      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            "#$$#$$$$$#      ",
            " #$#$$$$$#      ",
            "  ##$$$$$#      ",
            "   #######      "};
            """

    def __getstate__(self):
        ''' When saving the document this object gets stored using Python's cPickle module.
        Since we have some un-pickable here -- the Coin stuff -- we must define this method
        to return a tuple of all pickable objects or None.
        '''
        return None

    def __setstate__(self,state):
        ''' When restoring the pickled object from document we have the chance to set some
        internals here. Since no data were pickled nothing needs to be done here.
        '''
        return None


def makePoints():
import Points
    p=Points.Points()

    l=[]
    for s in m:
        l.append(s.Vector)

    p.addPoints(l)


    a=FreeCAD.ActiveDocument.addObject("Points::FeaturePython","Points")
    a.Points=p
    PointFeature(a)
    ViewProviderPoints(a.ViewObject)
