from PIL import Image
import os

# 用户输入文件夹路径
texture_folder = input("请输入贴图文件夹路径（例如 C:/Users/Administrator/Textures）：").strip()

# 检查路径是否存在
if not os.path.exists(texture_folder):
    print("❌ 错误：文件夹不存在，请检查路径是否正确！")
    input("按 Enter 退出...")
    exit()

# 用户输入缩放比例
try:
    scale = float(input("请输入缩放比例（例如 0.25 表示缩小到 1/4）：").strip())
    if scale <= 0 or scale > 1:
        raise ValueError
except ValueError:
    print("❌ 错误：缩放比例必须是 0 到 1 之间的小数！")
    input("按 Enter 退出...")
    exit()

# 用户输入图片质量
try:
    quality = int(input("请输入输出图片质量（1-100，推荐 90）：").strip())
    if quality < 1 or quality > 100:
        raise ValueError
except ValueError:
    print("❌ 错误：质量必须是 1 到 100 之间的整数！")
    input("按 Enter 退出...")
    exit()

# 遍历文件夹及所有子文件夹
for root, _, files in os.walk(texture_folder):
    for filename in files:
        if filename.lower().endswith(".jpg"):  # 只处理 JPG 文件
            img_path = os.path.join(root, filename)

            try:
                # 打开图片
                img = Image.open(img_path)

                # 计算新尺寸
                new_size = (int(img.width * scale), int(img.height * scale))
                img_resized = img.resize(new_size, Image.LANCZOS)

                # 保存并覆盖原文件
                img_resized.save(img_path, quality=quality)

                print(f"✅ 处理完成：{img_path} → 新尺寸 {new_size}")

            except Exception as e:
                print(f"❌ 处理失败：{img_path}，错误：{e}")

print("\n🎉 批量缩小完成！所有 JPG 贴图已替换为缩小后的版本。")

# 防止窗口立即关闭
input("按 Enter 退出...")