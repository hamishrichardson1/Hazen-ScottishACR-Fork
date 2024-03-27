
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
parser.add_argument('-RunGhosting',action="store_true",default=False)
parser.add_argument('-SlicePos',action="store_true",default=False)
parser.add_argument('-SliceThickness',action="store_true",default=False)
args = parser.parse_args()
Seq = args.seq

if args.RunAll == True:
    TotalTests = 7
else:
    TotalTests=0
    if args.runSNR ==True:
        TotalTests+=1
    if args.RunGeoAcc ==True:
        TotalTests+=1
    if args.RunSpatialRes ==True:
        TotalTests+=1
    if args.RunUniformity ==True:
        TotalTests+=1
    if args.RunGhosting ==True:
        TotalTests+=1
    if args.SlicePos ==True:
        TotalTests+=1
    if args.SliceThickness ==True:
        TotalTests+=1
        
#load in the DICOM
DICOMPath="DataTransfer"
#DICOMPath="MedACRTesting\ACR_ARDL_Tests"
files = get_dicom_files(DICOMPath)
ACRDICOMSFiles = {}
for file in files:
    data = pydicom.dcmread(file)
    if (data.SeriesDescription not in ACRDICOMSFiles.keys()):
        ACRDICOMSFiles[data.SeriesDescription]=[]
    ACRDICOMSFiles[data.SeriesDescription].append(file)
Data = ACRDICOMSFiles[Seq]

ToleranceTable = {}
ToleranceTable["SNR"]=[None,None]
ToleranceTable["Geometric Acuracy"]=[None,None]
ToleranceTable["Spatial Resolution"]=[None,None]
ToleranceTable["Uniformity"]=[None,None]
ToleranceTable["Ghosting"]=[None,None]
ToleranceTable["Slice Position"]=[None,None]
ToleranceTable["Slice Thickness"]=[None,None]

f = open("ToleranceTable/ToleranceTable.txt")
for line in f: 
    if line[0]!="#":
        Name = line.split(",")[0].strip()
        Lower = line.split(",")[1].strip()
        Upper = line.split(",")[2].strip()
        if Lower == "None" or Lower=="none":
            Lower = None
        else:
            Lower=float(Lower)
        if Upper == "None" or Upper=="none":
            Upper = None
        else:
            Upper=float(Upper)
        ToleranceTable[Name] = [Lower,Upper]

FileName = "OutputFolder/Results_" + Seq +"_" + str(date.today())+".txt"
ReportFile = open(FileName,"w")

ReportFile.write("Date Analysed: " + str(date.today()) + "\n")
ReportFile.write("Sequence Analysed: " + Seq + "\n")


def GetPassResult(Value,TestName):
    if ToleranceTable[TestName]==[None,None]:
        return "Result: No Tolerance Set"
    Pass=True
    if ToleranceTable[TestName][1]!=None:
        if Value > ToleranceTable[TestName][1]:
            Pass=False
    if ToleranceTable[TestName][0]!=None:
        if Value < ToleranceTable[TestName][0]:
            Pass=False
    if Pass ==True:
        return ("Result: Pass")
    else:
        return ("Result: Fail") 
    
TestCounter=0
if args.RunAll==True or args.RunSNR == True:
    acr_snr_task = ACRSNR(input_data=Data, report_dir="OutputFolder",report=True,MediumACRPhantom=True)
    snr = acr_snr_task.run()
    print("SNR :" +str(snr["measurement"]["snr by smoothing"]["measured"]))
    ReportFile.write("\nSNR Module\n")
    ReportFile.write("\tSNR: " +str(snr["measurement"]["snr by smoothing"]["measured"]) +"\t" + GetPassResult(snr["measurement"]["snr by smoothing"]["measured"],"SNR") +"\n")
    TestCounter+=1
    print("Progress " +str(TestCounter) +"/" +str(TotalTests))

if args.RunAll==True or args.RunGeoAcc == True:
    acr_geometric_accuracy_task = ACRGeometricAccuracy(input_data=Data,report_dir="OutputFolder",MediumACRPhantom=True,report=True)
    GeoDist = acr_geometric_accuracy_task.run()
    print("Slice 1 Hor Dist: "+str(GeoDist["measurement"][GeoDist["file"][0]]["Horizontal distance"]) + "   "+ " Vert Dist: "+str(GeoDist["measurement"][GeoDist["file"][0]]["Vertical distance"]))
    print("Slice 5 Hor Dist:"+str(GeoDist["measurement"][GeoDist["file"][1]]["Horizontal distance"]) + "   "+ " Vert Dist:"+str(GeoDist["measurement"][GeoDist["file"][1]]["Vertical distance"])+ "   "+ " Diag SW Dist:"+str(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SW"])+ "   "+ "Diag SE Dist:"+str(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SE"]))
    
    ReportFile.write("\nGeometric Accuracy Module\n")
    ReportFile.write("\tSlice 1:\n")
    ReportFile.write("\t\tHor Dist (mm): "+str(GeoDist["measurement"][GeoDist["file"][0]]["Horizontal distance"])+"\t" + GetPassResult(GeoDist["measurement"][GeoDist["file"][0]]["Horizontal distance"],"Geometric Acuracy") +"\n")
    ReportFile.write("\t\tVert Dist (mm): "+str(GeoDist["measurement"][GeoDist["file"][0]]["Vertical distance"])+"\t" + GetPassResult(GeoDist["measurement"][GeoDist["file"][0]]["Vertical distance"],"Geometric Acuracy")+"\n")

    ReportFile.write("\tSlice 5:\n")
    ReportFile.write("\t\tHor Dist (mm): "+str(GeoDist["measurement"][GeoDist["file"][1]]["Horizontal distance"]) +"\t" + GetPassResult(GeoDist["measurement"][GeoDist["file"][1]]["Horizontal distance"],"Geometric Acuracy")+"\n")
    ReportFile.write("\t\tVert Dist (mm): "+str(GeoDist["measurement"][GeoDist["file"][1]]["Vertical distance"])+"\t" + GetPassResult(GeoDist["measurement"][GeoDist["file"][1]]["Vertical distance"],"Geometric Acuracy")+"\n")
    ReportFile.write("\t\tDiagonal distance SW (mm): "+str(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SW"])+"\t" + GetPassResult(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SW"],"Geometric Acuracy")+"\n")
    ReportFile.write("\t\tDiagonal distance SE (mm): "+str(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SE"])+"\t" + GetPassResult(GeoDist["measurement"][GeoDist["file"][1]]["Diagonal distance SE"],"Geometric Acuracy")+"\n")

    TestCounter+=1
    print("Progress " +str(TestCounter) +"/" +str(TotalTests))

if args.RunAll==True or args.RunSpatialRes == True:
    acr_spatial_resolution_task = ACRSpatialResolution(input_data=Data,report_dir="OutputFolder",report=True,MediumACRPhantom=True,UseDotMatrix=True)
    Res = acr_spatial_resolution_task.run()
    ReportFile.write("\nSpatial Resoloution Module\n")
    ReportFile.write("\t1.1mm Holes Score: "+str(Res["measurement"]["1.1mm holes"])+"\t" + GetPassResult(Res["measurement"]["1.1mm holes"],"Spatial Resolution")+"\n")
    ReportFile.write("\t1.0mm Holes Score: "+str(Res["measurement"]["1.0mm holes"])+"\t" + GetPassResult(Res["measurement"]["1.0mm holes"],"Spatial Resolution")+"\n")
    ReportFile.write("\t0.9mm Holes Score: "+str(Res["measurement"]["0.9mm holes"])+"\t" + GetPassResult(Res["measurement"]["0.9mm holes"],"Spatial Resolution")+"\n")
    ReportFile.write("\t0.8mm Holes Score: "+str(Res["measurement"]["0.8mm holes"])+"\t" + GetPassResult(Res["measurement"]["0.8mm holes"],"Spatial Resolution")+"\n")

    TestCounter+=1
    print("Progress " +str(TestCounter) +"/" +str(TotalTests))

if args.RunAll==True or args.RunUniformity == True:
    acr_uniformity_task = ACRUniformity(input_data=Data,report_dir="OutputFolder",MediumACRPhantom=True,report=True)
    UniformityResult=acr_uniformity_task.run()
    print(" Uniformity :" + str(UniformityResult["measurement"]["integral uniformity %"]))
    ReportFile.write("\nUniformity Module\n")
    ReportFile.write("\tUniformity (%): "+str(UniformityResult["measurement"]["integral uniformity %"])+"%"+"\t" + GetPassResult(UniformityResult["measurement"]["integral uniformity %"],"Uniformity")+"\n")

    TestCounter+=1
    print("Progress " +str(TestCounter) +"/" +str(TotalTests))

if args.RunAll==True or args.RunGhosting == True:
    acr_ghosting_task = ACRGhosting(input_data=Data,report_dir="OutputFolder",MediumACRPhantom=True,report=True)
    ghosting = acr_ghosting_task.run()
    print("Ghosting :" + str(ghosting["measurement"]["signal ghosting %"]))
    ReportFile.write("\nGhosting Module\n")
    ReportFile.write("\tGhosting (%): " + str(ghosting["measurement"]["signal ghosting %"])+"%" +"\t" + GetPassResult(ghosting["measurement"]["signal ghosting %"],"Ghosting") +"\n")

    TestCounter+=1
    print("Progress " +str(TestCounter) +"/" +str(TotalTests))

if args.RunAll==True or args.SlicePos == True:
    acr_slice_position_task = ACRSlicePosition(input_data=Data,report_dir="OutputFolder",report=True,MediumACRPhantom=True)
    SlicePos = acr_slice_position_task.run()
    print("Slice Pos difference " + SlicePos['file'][0] + " :" + str(SlicePos['measurement'][SlicePos['file'][0]]['length difference']) + "mm    " + SlicePos['file'][1] + " :" + str(SlicePos['measurement'][SlicePos['file'][1]]['length difference'])+"mm")
    ReportFile.write("\nSlice Position Module\n")
    ReportFile.write("\tSlice 1 Position Error (mm): " + str(SlicePos['measurement'][SlicePos['file'][0]]['length difference'])+"\t" + GetPassResult(SlicePos['measurement'][SlicePos['file'][0]]['length difference'],"Slice Position") +"\n")
    ReportFile.write("\tSlice 11 Position Error (mm): " + str(SlicePos['measurement'][SlicePos['file'][1]]['length difference'])+"\t" + GetPassResult(SlicePos['measurement'][SlicePos['file'][1]]['length difference'],"Slice Position") +"\n")

    TestCounter+=1
    print("Progress " +str(TestCounter) +"/" +str(TotalTests))

if args.RunAll==True or args.SliceThickness == True:
    acr_slice_thickness_task = ACRSliceThickness(input_data=Data,report_dir="OutputFolder",report=True,MediumACRPhantom=True)
    SliceThick = acr_slice_thickness_task.run()
    print("Slice Width (mm): " + str(SliceThick['measurement']['slice width mm']))
    ReportFile.write("\nSlice Thickness Module\n")
    ReportFile.write("\tSlice Width (mm): " + str(SliceThick['measurement']['slice width mm'])+"\t" + GetPassResult(SliceThick['measurement']['slice width mm'],"Slice Thickness") +"\n")

    TestCounter+=1
    print("Progress " +str(TestCounter) +"/" +str(TotalTests))

ReportFile.close()

