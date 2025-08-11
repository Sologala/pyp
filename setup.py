from setuptools import setup, find_packages
import os

# 动态获取build目录下的二进制文件路径
def get_binary_files():
    binary_files = []
    # 遍历build目录下的所有.so和.pyd文件
    for root, dirs, files in os.walk("./build/Release/"):
        for file in files:
            if file.endswith((".so", ".pyd")):
                # 保存相对路径
                rel_path = os.path.relpath(os.path.join(root, file), ".")
                binary_files.append(rel_path)
    return binary_files

bin_files = get_binary_files()
bin_files.append("./build/Release/_dynamic_lib.dll")
print(bin_files)
setup(
    name="myproject",
    version="0.1.0",
    packages=find_packages(),

    # 声明需要包含的二进制文件（从build目录获取）
    # package_data={
    #     # 将build目录的二进制文件安装到myproject的libs子目录
    #     "myproject": ["build/**/*.so", "build/**/*.pyd", "build/**/*.dll"]
    # },

    # 或者使用data_files（安装到指定系统路径，不推荐）
    data_files=[
        (".", bin_files)  # 目标路径: 包内libs目录
    ],

    author="Your Name",
    description="Project with binaries from build directory",
    platforms=["win_amd64"],  # 明确声明仅支持Windows 64位
    python_requires=">=3.6",
)

