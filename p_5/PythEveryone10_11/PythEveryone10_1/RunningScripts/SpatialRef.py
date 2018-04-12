#import modules
import arcpy

#set workspace
arcpy.env.workspace = r"E:\\Python\\arcpy_folder1\\p_5\\PythEveryone10_11\\PythEveryone10_1\\RunningScripts\\Oregon_Polk.gdb"

#set up a describe object for each fc in gdb
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    desc = arcpy.Describe(fc)
    print desc.spatialReference.name

print "Script completed"    