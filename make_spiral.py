import bpy
import math
import random

# length=sprial length
# width=sprial width
# tapering=sprial tapers at the end
def make_spiral(length, width, tapering=False):
    
    mesh = bpy.data.meshes.new('spiral') 
    obj = bpy.data.objects.new('spiral', mesh)

    x = 0.0
    y = 0.0
    z = 0.0

    verts = [(x,y,z)] 
    edges = []
    taper = 1
    
    # generate vertices in a spiral
    for i in range(1,length): 
        z += 1
        if tapering:
            x += width*math.cos(i)*taper
            y += width*math.sin(i)*taper
            if taper > 0.0:
                taper -= 1/length # taper based on length
        else:
            x += width*math.cos(i) 
            y += width*math.sin(i)
            
        verts.append((x,y,z)) # place vertex
        edges.append((i-1, i)) # connect prev-->current vertices
        
    # give object geometry data
    mesh.from_pydata(verts, edges, [])

    # add object to scene
    bpy.context.collection.objects.link(obj)
    mesh.update(calc_edges=True) # idk what this does
    

make_spiral(40, 15, False) 