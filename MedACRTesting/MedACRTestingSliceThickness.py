import sys
#sys.path.insert(0,"C:\\Users\\Johnt\\Documents\\GitHub\\Hazen-ScottishACR-Fork")
sys.path.insert(0,"C:\\Users\\hamis\\gitest\\Hazen-ScottishACR-Fork")
import pydicom
from hazenlib.utils import get_dicom_files
from hazenlib.tasks.acr_slice_thickness import ACRSliceThickness
from hazenlib.ACRObject import ACRObject
import pathlib
from tests import TEST_DATA_DIR, TEST_REPORT_DIR
from tkinter import filedialog as fd

ReportDirPath = "MedACRTests"
'''
#Make sure it works with the test data
files = get_dicom_files("tests\\data\\acr\\GE")
acr_slice_thickness_task = ACRSliceThickness(input_data=files,report_dir=ReportDirPath,report=True)
dcm = acr_slice_thickness_task.ACR_obj.dcms[0]
SliceThick = acr_slice_thickness_task.get_slice_thickness(dcm)
print(SliceThick)
'''

#files = get_dicom_files("C:\\Users\\hamis\\gitest\\Hazen-ScottishACR-Fork\\MedACRTesting\\ACR_Phantom_Data")
folder_sel = fd.askdirectory()
files = get_dicom_files(folder_sel)
ACRDICOMSFiles = {}
for file in files:
    data = pydicom.dcmread(file)
    if (data.SeriesDescription not in ACRDICOMSFiles.keys()):
        ACRDICOMSFiles[data.SeriesDescription]=[]
    ACRDICOMSFiles[data.SeriesDescription].append(file)
ChosenData = ACRDICOMSFiles[data.SeriesDescription]

acr_slice_thickness_task = ACRSliceThickness(input_data=ChosenData,report_dir=ReportDirPath,report=True,MediumACRPhantom=True)
dcm = acr_slice_thickness_task.ACR_obj.dcms[0]
SliceThick = acr_slice_thickness_task.get_slice_thickness(dcm)
#print(SliceThick)
print(f'Results for series {data.SeriesDescription}: Slice Width = {SliceThick}mm')