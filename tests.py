import pydicom
import sys
import numpy as np

firstFile = r'C:\Users\1358365\PycharmProjects\untitled\dataset\Brain-Tumor-Progression\PGBM-001\11-19-1991-FH-HEADBrain Protocols-40993\35637-FLAIRreg-16386\000008.dcm'
secondFile = r'C:\Users\1358365\PycharmProjects\untitled\dataset\Brain-Tumor-Progression\PGBM-001\11-19-1991-FH-HEADBrain Protocols-40993\35637-FLAIRreg-16386\000010.dcm'

dicomFile1 = pydicom.dcmread(firstFile);
dicomFile2 = pydicom.dcmread(secondFile);

image1 = dicomFile1.pixel_array
image2 = dicomFile2.pixel_array

print(image1.dtype)