import zipfile

comp_file = zipfile.ZipFile('comp_file.zip','w')

comp_file.write('sample.pdf',compress_type=zipfile.ZIP_DEFLATED)

print("File has been created")