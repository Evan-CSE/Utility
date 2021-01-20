import zipfile

filename = input("Enter file name")

print("-----------Extracting file ------------\n");

ob = zipfile.ZipFile(filename);

ob.extractall();
