import FreeCAD, FreeCADGui, Part
p= _P
class Punt():
    '''
    crear un punt amb coordenades x,y,z i afegir-hi atributs com Id de punt i codi de punt
    '''
    
    def __init__(self,obj ,id_point='',x=0, y=0, z=0, code=''):
        
        obj.addProperty("App::PropertyString","dd_punt","Punt","Identificacio del punt").string=id_point
        obj.addProperty("App::PropertyLength","codi","Punt","descripcio").string=code
        obj.addProperty("App::PropertyVector","coor","punt","Coordenades").coor=FreeCAD.Vector(x,y,z)
        obj.draft().makePoint(x,y,z)
        
    def execute(self, fp):
        
        
 
        
        
        