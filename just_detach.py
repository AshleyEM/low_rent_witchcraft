# Completely detaches a selected mesh from an armature
import bpy

obj = bpy.context.active_object # selected object

if obj.type == 'MESH' and obj.parent != None:
    if obj.parent.type == 'ARMATURE':
        obj.parent = None # clear object's parent
        obj.vertex_groups.clear() # delete object's vertex groups
        obj.modifiers.remove(obj.modifiers.get('Armature'))# delete object's armature modifier
