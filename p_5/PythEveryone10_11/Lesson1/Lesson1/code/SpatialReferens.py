# This script uses map algebra to find values in an
# elevation raster greater than 3500 (meters).
import arcpy
from arcpy.sa import *

# Specify the input raster
inRaster = r"E:\Python\arcpy_folder1\p_5\PythEveryone10_11\Lesson1\Lesson1\foxlake"
cutoffElevation = 3500

# Check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# Make a map algebra expression and save the resulting raster
outRaster = Raster(inRaster) > cutoffElevation
outRaster.save(r"E:\Python\arcpy_folder1\p_5\PythEveryone10_11\Lesson1\Lesson1\foxlake_hi_3500.tif")

# Check in the Spatial Analyst extension now that you're done
arcpy.CheckInExtension("Spatial")

arcpy.env.overwriteOutput = True