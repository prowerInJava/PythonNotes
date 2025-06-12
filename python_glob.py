import glob

txt_files = glob.glob('./**/*.py')  # 匹配当前文件夹下的一层文件夹下的.py文件
for file_path in txt_files:
    print(file_path)

print(glob.glob("*/*/apple.txt"))  # 通配符*，表示匹配所有字符
print(glob.glob('*/?anana.txt'))  # 通配符？，表示任意一个字符

