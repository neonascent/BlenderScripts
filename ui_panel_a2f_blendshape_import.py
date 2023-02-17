import bpy
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       PropertyGroup,
                       )
import json 

# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------

#class JSONimportPanelProps(PropertyGroup):
#    filepath = bpy.props.StringProperty(name="String Value")
 

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------        
        


class createAnimation(Operator):
    bl_label = "Create Animation"
    bl_idname = 'object.blendshape_animation_operator'
    
    filepath : bpy.props.StringProperty(name="JSON file", description="JSON blendshape file from Audio2Face",subtype="FILE_PATH") 
    #"E:/DigitalConnection/Participants/Gina/mum/cache/can't speak english.json"
        
    def execute(self,context):
        display = "filepath= "+self.filepath  
        print(display) #Prints to console  
        with open(self.filepath) as f:
            json_animate = json.load(f)
            print(json_animate) 
            
            bs_animation = json_animate['weightMat']
            bs_pose_count = json_animate['numPoses']
            bs_frame_count = json_animate['numFrames']
            bs_names = json_animate['facsNames']
            bs_offset = 1 # basis blendshape at start
            #bs_limit = 68
            bs_limit = bs_pose_count

            #bpy.context.selected_objects[0].active_shape_key_index = 1
            #bpy.context.selected_objects[0].active_shape_key.value = bs_animation[i][j]
            
            for i in range(bs_frame_count): #each keyframe
                print("frame: "+str(i));
                for j in range(bs_limit):#bs_pose_count):# each pose
                     index = bpy.context.selected_objects[0].data.shape_keys.key_blocks.find(bs_names[j])
                     if index > -1: 
                         #print(str(i) + ", " + str(j) + ":" )
                         bpy.context.selected_objects[0].active_shape_key_index = index
                         #bpy.context.selected_objects[0].active_shape_key_index = j + bs_offset
                         bpy.context.selected_objects[0].active_shape_key.value = bs_animation[i][j]
                         bpy.context.selected_objects[0].active_shape_key.keyframe_insert("value",frame=i)
                     # add Merged_Open_Mouth from Mouth_Open
                     #if bs_names[j] == "Mouth_Open":
                        # index = bpy.context.selected_objects[0].data.shape_keys.key_blocks.find("Merged_Open_Mouth")
                        # if index > -1: 
                          #   bpy.context.selected_objects[0].active_shape_key_index = index
                            # bpy.context.selected_objects[0].active_shape_key.value = bs_animation[i][j]
                             #bpy.context.selected_objects[0].active_shape_key.keyframe_insert("value",frame=i)
        return {'FINISHED'}
    
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self) 
        return {'RUNNING_MODAL'}  

# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class JSONimportPanel(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Import A2F Blendshapes"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Josh Tools'

    def draw(self, context):
        layout = self.layout
        
        obj = context.object
        #filename = "c:/example"
        
        row = layout.row()
        row.label(text="Select Object with face Blendshapes")

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
                        
        row = layout.row()
        row.operator("object.blendshape_animation_operator")
        


def register():
    #bpy.utils.register_class(JSONimportPanelProps)
    bpy.utils.register_class(JSONimportPanel)
    bpy.utils.register_class(createAnimation)

def unregister():
    #bpy.utils.unregister_class(JSONimportPanelProps)
    bpy.utils.unregister_class(JSONimportPanel)
    bpy.utils.unregister_class(createAnimation)


if __name__ == "__main__":
    register()
