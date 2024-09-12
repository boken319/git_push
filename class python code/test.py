from PIL import Image, ImageFilter, ImageDraw

try:
    # 打开图像
    image = Image.open('example.png')

    # 将图像模式从RGBA转换为RGB
    image = image.convert('RGB')
    # 'RGB' 是目标模式，表示图像将转换为红、绿、蓝三个通道的图像。
    # RGBA 模式表示图像有红、绿、蓝和透明度四个通道。

    # 获取图像信息
    width, height = image.size
    mode = image.mode
    print(f"Width: {width}, Height: {height},  Mode: {mode}")

    # 裁剪图像
    box = (100, 100, 400, 400)
    cropped_image = image.crop(box)
    cropped_image.show()

    # 调整图像大小
    new_size = (300, 300)
    resized_image = image.resize(new_size)
    resized_image.show()

    # 旋转图像
    rotated_image = image.rotate(45)
    rotated_image.show()

    # 应用滤镜
    # ImageFilter.BLUR是一个预定义的滤镜，用于模糊图像。
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.show()

    # 转换为灰度图像
    gray_image = image.convert('L')
    gray_image.show()

    # 生成第一张图片：左边是原图的左半部分，右边是灰度图片的右半部分
    try:
        combined_image1 = Image.new('RGB', (width, height))
        left_half_1 = image.crop((0, 0, width // 2, height))
        right_half_1 = gray_image.crop((width // 2, 0, width, height))
        combined_image1.paste(left_half_1, (0, 0))
        combined_image1.paste(right_half_1, (width // 2, 0))
        combined_image1.save('combined_image1.jpg')
        print("第一张图片已生成并保存为 combined_image1.jpg")

        # 生成第二张图片：左边是灰度图片的左半部分，右边是原图的右半部分
        combined_image2 = Image.new('RGB', (width, height))
        left_half_2 = gray_image.crop((0, 0, width // 2, height))
        right_half_2 = image.crop((width // 2, 0, width, height))
        combined_image2.paste(left_half_2, (0, 0))
        combined_image2.paste(right_half_2, (width // 2, 0))
        combined_image2.save('combined_image2.jpg')
        print("第二张图片已生成并保存为 combined_image2.jpg")

        # 生成 GIF 动画
        frames = [image, combined_image1, combined_image2]
        frame_durations = [500, 500, 500]  # 每帧显示 500 毫秒
        frames[0].save('animation.gif', save_all=True, append_images=frames[1:], duration=frame_durations, loop=0)
        print("GIF 动画已生成并保存为 animation.gif")

    except Exception as e:
        print(f"生成图片时发生错误: {e}")
    # 绘制图形
    draw = ImageDraw.Draw(image)
    draw.rectangle([50, 50, 2500, 1450], outline="red", width=10)
    image.show()

    # 保存图像
    image.save('new_example.jpg')

    # 生成缩略图
    thumbnail_size = (100, 100)
    image.thumbnail(thumbnail_size)
    image.save('thumbnail_example.jpg')
    print("缩略图已生成并保存为 thumbnail_example.jpg")

    # 将图像转换为点阵
    # 定义每个像素块的大小（例如，每个块20x20像素）
    block_size = (20, 20)

    # 获取原始图像的宽度和高度
    width, height = image.size

    # 计算新的宽度和高度（基于像素块大小，向下取整到最近的块倍数）
    new_width = (width // block_size[0]) * block_size[0]
    new_height = (height // block_size[1]) * block_size[1]

    # 先将图像调整为新的尺寸（使用最近邻插值）
    resized_image = image.resize((new_width, new_height), Image.NEAREST)

    # 创建一个与 resized_image 相同大小的新图像，但颜色模式保持不变
    pixelated_image = Image.new(image.mode, (new_width, new_height))

    # 遍历每个块，并将块内的代表性像素（这里使用左上角像素）复制到新图像中
    for x in range(0, new_width, block_size[0]):
        for y in range(0, new_height, block_size[1]):
            # 获取块内左上角像素的坐标
            block_x, block_y = x, y
            # 从 resized_image 中获取该像素的值（或颜色）
            pixel = resized_image.getpixel((block_x, block_y))
            # 将这个值（或颜色）应用到整个块中
            pixelated_image.paste(pixel, (x, y, x + block_size[0], y + block_size[1]))

            # 保存和显示像素化后的图像
    pixelated_image.save('pixelated_example.jpg')
    print("点阵图像已生成并保存为 pixelated_example.jpg")
    pixelated_image.show()



except FileNotFoundError:
    print("文件未找到，请检查文件路径。")
except Exception as e:
    print(f"发生错误: {e}")
