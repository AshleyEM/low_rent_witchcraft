import bpy
import math
import random

# length=spiral length
# width=spiral width
# tapering=spiral tapers at the end
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
    for i in range(1, length*width): 
        
        # go up, keep "resolution" consistent for different widths
        z += 1/width 
        
        if tapering:
            x += taper * math.cos(i/width)
            y += taper * math.sin(i/width)
            if taper > 0.0: # decrease taper at each new vertex
                taper -= 1/(length * width) 
        else:
            x += math.cos(i/width)
            y += math.sin(i/width)
            
        verts.append((x,y,z)) # place vertex
        edges.append((i-1, i)) # connect prev-->current vertices
        
    # give object geometry data
    mesh.from_pydata(verts, edges, [])

    # add object to scene
    bpy.context.collection.objects.link(obj)
    mesh.update(calc_edges=True)
    

make_spiral(40, 2, False)
