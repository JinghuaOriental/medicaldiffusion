'''
Author: JinghuaOriental 1795185859@qq.com
Date: 2024-04-19 15:18:23
LastEditors: JinghuaOriental 1795185859@qq.com
LastEditTime: 2024-04-19 15:27:31
FilePath: /medicaldiffusion/dataset/0_process.py
Description: 
'''
import os
import numpy as np
import nibabel as nib

def nii_to_npy(nii_file, npy_file):
    """ 读取单一nii文件并转换为npy文件 """
    image = nib.load(nii_file)
    # 将nii图像转换为numpy数组
    np_array = image.get_fdata()
    # 保存为npy文件
    np.save(npy_file, np_array)

def batch_convert_nii_to_npy(input_folder, output_folder):
    """ 批量转换nii文件为npy文件 """
    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        # 删除该文件夹并重新创建
        os.system(f"rm -rf {output_folder}")
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".nii") or file.endswith(".nii.gz"):
                file_only_name = file.split(".")[0]
                # 构建输入和输出文件的路径
                input_file = os.path.join(root, file)
                output_file = os.path.join(output_folder, file_only_name + ".npy")
                # 将nii文件转换为npy文件
                nii_to_npy(input_file, output_file)

if __name__ == '__main__':
    # 设置输入文件夹和输出文件夹的路径
    input_folder = "/home/hyj/python_files2/Generate/Diffusion/medicaldiffusion/AAA_data/LIDC-IDRI/data/TCIA_LIDC-IDRI_processed/LIDC-IDRI_scaled_256x256x256"  # 替换为你的输入文件夹路径
    output_folder = f"{input_folder}_npy"  # 替换为你的输出文件夹路径

    # 执行批量转换
    batch_convert_nii_to_npy(input_folder, output_folder)
