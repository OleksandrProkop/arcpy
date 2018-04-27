import arcpy

featureClass = r"E:\Python\arcpy_folder1\p_5\PythEveryone10_11\Lesson1\Lesson1\USA.mdb\us_boundaries"

# Describe the feature class and get its spatial reference
desc = arcpy.Describe(featureClass)
spatialRef = desc.spatialReference

# Print the spatial reference name
print spatialRef.Name