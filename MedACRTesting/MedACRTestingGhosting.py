import pydicom
import sys
#sys.path.insert(0,"C:\\Users\\Johnt\\Documents\\GitHub\\Hazen-ScottishACR-Fork")
sys.path.insert(0,"C:\\Users\\hamis\\gitest\\Hazen-ScottishACR-Fork")
from hazenlib.utils import get_dicom_files
from hazenlib.tasks.acr_snr import ACRSNR
from hazenlib.tasks.acr_ghosting import ACRGhosting
from hazenlib.ACRObject import ACRObject
import pathlib
from tests import TEST_DATA_DIR, TEST_REPORT_DIR
from tkinter import filedialog as fd

ReportDirPath = "MedACRTests"
'''
#Make sure it works with the test data
ACR_DATA_SIEMENS = pathlib.Path(TEST_DATA_DIR / "acr" / "ge")
ChosenData = get_dicom_files(ACR_DATA_SIEMENS)
acr_ghosting_task = ACRGhosting(input_data=ChosenData,report_dir=ReportDirPath,MediumACRPhantom=False,report=True)
ghosting = acr_ghosting_task.get_signal_ghosting(acr_ghosting_task.ACR_obj.slice7_dcm)
print(ghosting)
'''

folder_sel = fd.askdirectory()
files = get_dicom_files(folder_sel)
#files = get_dicom_files("ACR_MRI1_20240116_104902641")
ACRDICOMSFiles = {}
for file in files:
    data = pydicom.dcmread(file)
    if (data.SeriesDescription not in ACRDICOMSFiles.keys()):
        ACRDICOMSFiles[data.SeriesDescription]=[]
    ACRDICOMSFiles[data.SeriesDescription].append(file)
ChosenData = ACRDICOMSFiles[data.SeriesDescription]


acr_ghosting_task = ACRGhosting(input_data=ChosenData,report_dir=ReportDirPath,MediumACRPhantom=True,report=True)
ghosting = acr_ghosting_task.get_signal_ghosting(acr_ghosting_task.ACR_obj.slice7_dcm)
print(ghosting)