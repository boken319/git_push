from PIL import Image
import os

# 假设 filelist 已经被定义为一个包含文件路径的列表
# 例如: filelist = ['image1.png', 'image2.jpg', 'image3.bmp']

filelist = ['D:\class python code\image\1.png', '"D:\class python code\image\2.png"', 'D:\class python code\image\5.png']

for infile in filelist:
    # 获取文件的扩展名，并构建输出文件名（去除原扩展名并添加.jpg）
    outfile = os.path.splitext(infile)[0] + ".jpg"

    # 如果原文件名和输出文件名不同（即原文件不是.jpg格式），则尝试转换
    if infile != outfile:
        try:
            # 尝试打开图像文件
            with Image.open(infile) as img:
                # 保存为.jpg格式
                img.save(outfile)
                print(f"Converted {infile} to {outfile}")
        except IOError as e:
            # 如果发生错误（如文件不存在），打印错误信息
            print(f"Cannot convert {infile}: {e}")