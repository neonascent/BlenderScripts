def SmoothKeyframes(action_name, data_path, channelindex, factor):
    #
    #bpy.data.objects["Mum"].pose.bones["CC_Base_Head"].rotation_quaternion[0]
    # Configuration
    #action_name = 'MyAction'
    #data_path = 'location'
    #index = 2                   # Z axis
    
    # Find the appropriate action
    action = bpy.data.actions.get(action_name)
    if action:
        # From this action, retrieve the appropriate F-Curve
        fcurve = action.fcurves.find(data_path, index=channelindex)
        if fcurve:
            # Iterate over all keyframes
            average = fcurve.keyframe_points[0].co[1] # first value (asuming it starts from 0 and not actual frame!)
            for kfp in fcurve.keyframe_points:
                # Print current keyframe info
                print('Frame = {:04}; Value = {}'.format(kfp.co[0], kfp.co[1]))
                # Change keyframe data
                # Push back in time by 2 frames
                #kfp.co[0] += 2
                # Move F-Curve up by 1
                kfp.co[1] = (kfp.co[1] + (factor * average) )/ (factor + 1)
                
                
SmoothKeyframes("Gina's Mum 0-3", 'pose.bones["CC_Base_Head"].rotation_quaternion', 1, 3)