
from hazenlib.utils import get_dicom_files
from hazenlib.tasks.acr_snr import ACRSNR
from hazenlib.tasks.acr_uniformity import ACRUniformity
from hazenlib.tasks.acr_geometric_accuracy import ACRGeometricAccuracy
from hazenlib.tasks.acr_spatial_resolution import ACRSpatialResolution
from hazenlib.tasks.acr_ghosting import ACRGhosting
from hazenlib.tasks.acr_slice_position import ACRSlicePosition
from hazenlib.tasks.acr_slice_thickness import ACRSliceThickness
from hazenlib.ACRObject import ACRObject
from tests import TEST_DATA_DIR, TEST_REPORT_DIR
import argparse
import pydicom
import sys
import glob
from datetime import date

# get the args
parser = argparse.ArgumentParser()
parser.add_argument('-seq', type=str, required=True)
parser.add_argument('-RunAll',action="store_true",default=False)
parser.add_argument('-RunSNR',action="store_true",default=False)
parser.add_argument('-RunGeoAcc',action="store_true",default=False)
parser.add_argument('-RunSpatialRes',action="store_true",default=False)
parser.add_argument('-RunUniformity',action="store_true",default=False)
args = parser.parse_args()
Seq = args.seq

#load in the DICOM
#DICOMPath="DataTransfer"
DICOMPath="MedACRTesting\ACR_ARDL_Tests"
files = get_dicom_files(DICOMPath)
ACRDICOMSFiles = {}
for file in files:
    data = pydicom.dcmread(file)
    if (data.SeriesDescription not in ACRDICOMSFiles.keys()):
        ACRDICOMSFiles[data.SeriesDescription]=[]
    ACRDICOMSFiles[data.SeriesDescription].append(file)
Data = ACRDICOMSFiles[Seq]

FileName = "OutputFolder/Results_" + Seq +"_" + str(date.today())
ReportFile = open(FileName,"w")

ReportFile.write("Date Analysed: " + str(date.today()) + "\n")
ReportFile.write("Sequence Analysed: " + Seq + "\n")


if args.RunAll==True or args.RunSNR == True:
    acr_snr_task = ACRSNR(input_data=Data, report_dir="OutputFolder",report=True,MediumACRPhantom=True)
    snr = acr_snr_task.run()
    print("SNR :" +str(snr["measurement"]["snr by smoothing"]["measured"]))
    ReportFile.write("\nSNR Module\n")
    ReportFile.write("\tSNR: " +str(snr["measurement"]["snr by smoothing"]["measured"]) + "\n")

if args.RunAll==True or args.RunGeoAcc == True:
        acr_geometric_accuracy_task = ACRGeometricAccuracy(input_data=Data,report_dir="OutputFolder",MediumACRPhantom=True,report=True)
        GeoDist = acr_geometric_accuracy_task.run()
        print("Slice 1 Hor Dist: "+str(GeoDist["measurement"][GeoDist["file"][0]]["Horizontal distance"]) + "   "+ " Vert Dist: "+str(GeoDist["measurement"][GeoDist["file"][0]]["Vertical distance"]))
        print("Slice 5 Hor Dist:"+str(GeoDist["measurement"][GeoDist["file"][1]]["Horizontal distance"]) + "   "+ " Vert Dist:"+str(GeoDist["measurement"][GeoDist["file"][1]]["Vertical distance"])+ "   "+ " Diag SW Dist:"+str(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SW"])+ "   "+ "Diag SE Dist:"+str(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SE"]))
        
        ReportFile.write("\nGeometric Accuracy Module\n")
        ReportFile.write("Slice 1:\n")
        ReportFile.write("\tHor Dist: "+str(GeoDist["measurement"][GeoDist["file"][0]]["Horizontal distance"])+"\n")
        ReportFile.write("\tVert Dist: "+str(GeoDist["measurement"][GeoDist["file"][0]]["Vertical distance"])+"\n")

        ReportFile.write("Slice 5:\n")
        ReportFile.write("\tHor Dist: "+str(GeoDist["measurement"][GeoDist["file"][1]]["Horizontal distance"])+"\n")
        ReportFile.write("\tVert Dist: "+str(GeoDist["measurement"][GeoDist["file"][1]]["Vertical distance"])+"\n")
        ReportFile.write("\tDiagonal distance SW: "+str(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SW"])+"\n")
        ReportFile.write("\tDiagonal distance SE: "+str(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SE"])+"\n")

if args.RunAll==True or args.RunSpatialRes == True:
    acr_spatial_resolution_task = ACRSpatialResolution(input_data=Data,report_dir="OutputFolder",report=True,MediumACRPhantom=True,UseDotMatrix=True)
    Res = acr_spatial_resolution_task.run()
    ReportFile.write("\nSpatial Resoloution Module\n")
    ReportFile.write("\t1.1mm Holes Score: "+str(Res["measurement"]["1.1mm holes"])+"\n")
    ReportFile.write("\t1.0mm Holes Score: "+str(Res["measurement"]["1.0mm holes"])+"\n")
    ReportFile.write("\t0.9mm Holes Score: "+str(Res["measurement"]["0.9mm holes"])+"\n")
    ReportFile.write("\t0.8mm Holes Score: "+str(Res["measurement"]["0.8mm holes"])+"\n")

if args.RunAll==True or args.RunUniformity == True:
    acr_uniformity_task = ACRUniformity(input_data=Data,report_dir="OutputFolder",MediumACRPhantom=True,report=True)
    UniformityResult=acr_uniformity_task.run()
    print(" Uniformity :" + str(UniformityResult["measurement"]["integral uniformity %"]))
    ReportFile.write("\nUniformity Module\n")
    ReportFile.write("\tUniformity (%): "+str(UniformityResult["measurement"]["integral uniformity %"])+"\n")
ReportFile.close()