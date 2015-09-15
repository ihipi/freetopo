import FreeCAD, FreeCADGui, Part, Draft
from FreeCAD import Base
from pivy import coin
from Part import Point


Point.__

class PartFeature:
    def __init__(self, obj):
        obj.Proxy = self
        
        
class Punt(PartFeature,P):
    '''
    crear un punt amb coordenades x,y,z i afegir-hi atributs com Id de punt i codi de punt
    '''
    
    def __init__(self,obj ,id_point='numero',x=0.0, y=0.0, z=0.0, code='codi',color=[1.0,0.0,0.0], size=5):
        PartFeature.__init__(self, obj)
        obj.addProperty("App::PropertyString","Nom","Punt","Identificacio del punt").Nom=id_point
        obj.addProperty("App::PropertyString","Codi","Punt","descripcio").Codi=code
        #obj.addProperty("App::PropertyVector","Color","View","Color").Color=FreeCAD.Vector(color)
        obj.addProperty("App::PropertyFloat","Size","Punt","East").Size=size
        obj.addProperty("App::PropertyFloat","X","Coordenades","Coordenades").X=x
        obj.addProperty("App::PropertyFloat","Y","Coordenades","Coordenades").X=y
        obj.addProperty("App::PropertyFloat","Z","Coordenades","Coordenades").X=z
        
    '''
    def onChanged(self, fp, prop):
        FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
        if prop == "Coord" or prop == "Size" or prop == "Color" or prop == "Nom" or prop == "Codi":
            fp.X=x
            fp.Y=y
            fp.Z=z
            fp.Codi=codi
    '''

    def execute(self, fp):
        ''' Print a short message when doing a recomputation, this method is mandatory '''
        FreeCAD.Console.PrintMessage("Recompute Python Punt feature\n")
        v=FreeCAD.Vector(fp.X,fp.Y,fp.Z)
        fp.shape= Part.Point(v)
        

class ViewProviderPunt:
    def __init__(self, obj):
        ''' Set this object to the proxy object of the actual view provider '''
        obj.Proxy = self

    def attach(self, obj):
        ''' Setup the scene sub-graph of the view provider, this method is mandatory '''
        return

    def updateData(self, fp, prop):
        ''' If a property of the handled feature has changed we have the chance to handle this here '''
        if prop == "X":
            s = fp.getPropertyByName("X")
            fp.X=s
        if prop == "Y":
            s = fp.getPropertyByName("Y")
            fp.X=s
        if prop == "Z":
            s = fp.getPropertyByName("Z")
            fp.coord.z

    def getDisplayModes(self,obj):
        ''' Return a list of display modes. '''
        modes=[]
        return modes

    def getDefaultDisplayMode(self):
        ''' Return the name of the default display mode. It must be defined in getDisplayModes. '''
        return "Shaded"

    def setDisplayMode(self,mode):
        ''' Map the display mode defined in attach with those defined in getDisplayModes.
        Since they have the same names nothing needs to be done. This method is optinal.
        '''
        return mode

    def onChanged(self, vp, prop):
        ''' Print the name of the property that has changed '''
        FreeCAD.Console.PrintMessage("Change pr,,,,operty: " + str(prop) + "\n")

    def getIcon(self):
        ''' Return the icon in XMP format which will appear in the tree view. This method is optional
        and if not defined a default icon is shown.
        '''
        return """
            /* XPM */
            static const char * ViewProviderPunt_xpm[] = {
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


def makePunt(name):
    a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython",name)
    Punt(a,name)
    ViewProviderPunt(a.ViewObject)
        
        
 
makePunt('0001')
        
        