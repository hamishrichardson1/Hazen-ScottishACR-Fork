import os
import unittest
import pathlib
import pydicom

from hazenlib.utils import get_dicom_files
from hazenlib.tasks.acr_snr import ACRSNR
from hazenlib.ACRObject import ACRObject
from tests import TEST_DATA_DIR, TEST_REPORT_DIR
import matplotlib.pyplot as plt

'''
#Get it working with just the test data
files = get_dicom_files("tests\\data\\acr\\GE")
acr_snr_task = ACRSNR(input_data=files, report_dir="TestReportDump",report=True)
snr_dcm = acr_snr_task.ACR_obj.dcms[6]
snr, _ = acr_snr_task.snr_by_smoothing(snr_dcm)
print(snr)
'''


files = get_dicom_files("ACR_MRI1_20240116_104902641")
ACRDICOMSFiles = {}
for file in files:
    data = pydicom.dcmread(file)
    if (data.SeriesDescription not in ACRDICOMSFiles.keys()):
        ACRDICOMSFiles[data.SeriesDescription]=[]
    ACRDICOMSFiles[data.SeriesDescription].append(file)

acr_snr_task = ACRSNR(input_data=ACRDICOMSFiles["ACR AxT1"], report_dir="TestReportDump",report=True,MediumACRPhantom=True)
snr_dcm = acr_snr_task.ACR_obj.dcms[6]
snr, _ = acr_snr_task.snr_by_smoothing(snr_dcm)