import sys
#sys.path.insert(0,"C:\\Users\\Johnt\\Documents\\GitHub\\Hazen-ScottishACR-Fork")
sys.path.insert(0,"C:\\Users\\hamis\\gitest\\Hazen-ScottishACR-Fork")
import pydicom
from hazenlib.utils import get_dicom_files
from hazenlib.tasks.acr_snr import ACRSNR
from hazenlib.tasks.acr_uniformity import ACRUniformity
from hazenlib.ACRObject import ACRObject
import pathlib
from tests import TEST_DATA_DIR, TEST_REPORT_DIR
from tkinter import filedialog as fd

ReportDirPath = "MedACRTests"
'''
#Make sure it works with the test data
files = get_dicom_files("tests\\data\\acr\\GE")
acr_snr_task = ACRSNR(input_data=files, report_dir=ReportDirPath,report=True)
snr_dcm = acr_snr_task.ACR_obj.dcms[6]
snr, _ = acr_snr_task.snr_by_smoothing(snr_dcm)
print(snr)
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
#ChosenData = ACRDICOMSFiles["ACR AxT1"]
ChosenData = ACRDICOMSFiles[data.SeriesDescription]
#print (ACRDICOMSFiles)

#Test SNR
#Only change neede was the paramaters of the hough circles
acr_snr_task = ACRSNR(input_data=ChosenData, report_dir=ReportDirPath,report=True,MediumACRPhantom=True)
snr_dcm = acr_snr_task.ACR_obj.slice7_dcm #acr_snr_task.ACR_obj.dcms[6]
snr,normalised_snr = acr_snr_task.snr_by_smoothing(snr_dcm)
print(f'SNR Results for series {data.SeriesDescription}: SNR = {snr} , Normalised SNR =  {normalised_snr}') 


