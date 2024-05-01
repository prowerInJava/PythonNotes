import glob

txt_files = glob.glob('PythonNotes/**/*.py')  # 匹配PythonNotes 文件夹下的多个文件夹下的.py文件
for file_path in txt_files:
    print(file_path)
