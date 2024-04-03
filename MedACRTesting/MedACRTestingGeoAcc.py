import pydicom
import sys
#sys.path.insert(0,"C:\\Users\\Johnt\\Documents\\GitHub\\Hazen-ScottishACR-Fork")
sys.path.insert(0,"C:\\Users\\hamis\\gitest\\Hazen-ScottishACR-Fork")
from hazenlib.utils import get_dicom_files
from hazenlib.tasks.acr_geometric_accuracy import ACRGeometricAccuracy
from hazenlib.tasks.slice_width import SliceWidth
from hazenlib.ACRObject import ACRObject
import pathlib
from tests import TEST_DATA_DIR, TEST_REPORT_DIR
from tkinter import filedialog as fd

ReportDirPath = "MedACRTests"
'''
#Make sure it works with the test data
ACR_DATA_SIEMENS = pathlib.Path(TEST_DATA_DIR / "acr" / "Siemens")
ChosenData = get_dicom_files(ACR_DATA_SIEMENS)
acr_geometric_accuracy_task = ACRGeometricAccuracy(input_data=ChosenData,report_dir=ReportDirPath,MediumACRPhantom=False,report=True)
dcm_1 = acr_geometric_accuracy_task.ACR_obj.dcms[0]
dcm_5 = acr_geometric_accuracy_task.ACR_obj.dcms[4]
slice1_vals = acr_geometric_accuracy_task.get_geometric_accuracy_slice1(dcm_1)
slice5_vals = acr_geometric_accuracy_task.get_geometric_accuracy_slice5(dcm_5)
print(slice1_vals,slice5_vals)
'''

folder_sel = fd.askdirectory()
files = get_dicom_files(folder_sel)
#files = get_dicom_files("C:\\Users\\hamis\\gitest\\Hazen-ScottishACR-Fork\\MedACRTesting\\ACR_Phantom_Data")
ACRDICOMSFiles = {}
for file in files:
    data = pydicom.dcmread(file)
    if (data.SeriesDescription not in ACRDICOMSFiles.keys()):
        ACRDICOMSFiles[data.SeriesDescription]=[]
    ACRDICOMSFiles[data.SeriesDescription].append(file)
ChosenData = ACRDICOMSFiles[data.SeriesDescription]


acr_geometric_accuracy_task = ACRGeometricAccuracy(input_data=ChosenData,report_dir=ReportDirPath,MediumACRPhantom=True,report=True)
dcm_1 = acr_geometric_accuracy_task.ACR_obj.dcms[0]
dcm_5 = acr_geometric_accuracy_task.ACR_obj.dcms[4]
slice1_vals = acr_geometric_accuracy_task.get_geometric_accuracy_slice1(dcm_1)
slice5_vals = acr_geometric_accuracy_task.get_geometric_accuracy_slice5(dcm_5)
print(
    f"""Results for series {data.SeriesDescription}:\n 
      Slice1 hoizontal = {slice1_vals[0]} \n 
      Slice1 vertical= {slice1_vals[1]} \n 
      Slice5 horizontal={slice5_vals[0]} \n 
      Slice5 vertical={slice5_vals[1]} \n 
      Slice5 NW>SE={slice5_vals[2]} \n 
      Slice5 NE>SW={slice5_vals[3]}"""
)


#Try calculating distortion on the rods using the MagNET code
'''
acr_geometric_accuracy_task = SliceWidth(input_data=ChosenData,report_dir=ReportDirPath,MediumACRPhantom=True,report=True)
dcm_5 = acr_geometric_accuracy_task.single_dcm #ACR_obj.dcms[4]
slice5_vals=acr_geometric_accuracy_task.get_rod_distortions(120,120)
print(f'Results for series {data.SeriesDescription}: Horizontal Distortion= {slice5_vals[0]}, Vertical Distortion={slice5_vals[1]}')
'''