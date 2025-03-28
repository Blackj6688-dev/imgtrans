# **📌 批量图片缩小脚本**  

本脚本用于 **批量缩小图片尺寸**，支持：
✅ **自定义图片文件夹路径**
✅ **自由设置缩放比例**（如 `0.25` 表示缩小到 1/4）
✅ **调整图片质量**（`1-100`，可控制输出清晰度）
✅ **递归遍历所有子文件夹，批量处理图片**  

**适用场景**：倾斜摄影数据处理、3D 贴图优化、大规模图片压缩等。  

---

## **🔹 环境准备**  

本脚本依赖 **Python 3.x**，请确保您的系统已安装 Python。  

### **1️⃣ 安装 Pillow（图像处理库）**  

如果尚未安装 `Pillow`，请运行以下命令：  

```Bash
pip install pillow
```

---

## **🔹 使用方法**  

### **1️⃣ 运行脚本**  

在 **命令行（CMD / PowerShell）** 中执行：  

```Bash
./imgtrans.py
```

### **2️⃣ 输入参数**  

执行后，按提示输入以下参数：  

- **图片文件夹路径**（如 `C:/Users/Admin/Textures/`）  
- **缩放比例**（如 `0.25` 表示缩小到 1/4）  
- **图片质量**（`1-100`，推荐 `90`）  

### **3️⃣ 处理完成**  

脚本会 **自动遍历所有子文件夹**，批量缩小 `.jpg` 图片，并 **覆盖原文件**。  

---

## **🔹 示例**  

![](https://secure2.wostatic.cn/static/hQHBGoZNddr8mCjtratCan/截屏2025-03-27 17.18.05.png?auth_key=1743128822-x6JBtRNbhDbNron3x9T8Mk-0-15fc72644b2df321b88dccce49ee3796)

```Bash
请输入贴图文件夹路径（例如 C:/Users/Administrator/Textures）：C:/Users/Administrator/Textures
请输入缩放比例（例如 0.25 表示缩小到 1/4）：0.25
请输入输出图片质量（1-100，推荐 90）：90
✅ 处理完成：C:/Users/Administrator/Textures/image1.jpg → 新尺寸 (1024, 768)
✅ 处理完成：C:/Users/Administrator/Textures/Subfolder/image2.jpg → 新尺寸 (512, 384)
🎉 批量缩小完成！所有 JPG 贴图已替换为缩小后的版本。
```

---

## **🔹 注意事项**  

- **确保 Python 环境可用**，可运行 `python --version` 检查  
- **避免图片被其他程序占用**（如 Photoshop、Blender）  
- **操作前建议备份原始文件**，避免不可逆修改  

🚀 **使用本脚本，轻松完成大规模图片处理！** 🎉
