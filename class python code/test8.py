from PIL import Image
import matplotlib.pyplot as plt

try:
    # 打开图像
    image = Image.open('example.png')

    # 将图像模式从RGBA转换为RGB（如果原图是RGBA的话）
    if image.mode == 'RGBA':
        image = image.convert('RGB')

        # 获取图像信息
    width, height = image.size
    mode = image.mode
    print(f"Width: {width}, Height: {height}, Mode: {mode}")



    # 将PIL图像转换为numpy数组，以便Matplotlib可以使用
    from numpy import array

    img_array = array(cropped_image)

    # 使用Matplotlib显示图像和绘制点线
    plt.figure(figsize=(8, 6))  # 设置图像大小
    plt.imshow(img_array)  # 显示图像
    plt.axis('off')  # 关闭坐标轴

    # 一些点
    x = [50, 50, 200, 200]  # 注意调整坐标以适应裁剪后的图像
    y = [100, 250, 100, 250]

    # 使用红色星状标记绘制点
    plt.plot(x, y, 'r*')

    # 绘制连接前两个点的线
    plt.plot(x[:2], y[:2], 'b-')  # 使用蓝色实线

    # 添加标题
    plt.title('Plotting on Cropped Image: "example.png"')

    # 显示绘制的图像
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")