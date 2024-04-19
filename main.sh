#!/bin/bash
###
 # @Author: JinghuaOriental 1795185859@qq.com
 # @Date: 2024-04-19 11:12:03
 # @LastEditors: JinghuaOriental 1795185859@qq.com
 # @LastEditTime: 2024-04-19 11:15:43
 # @FilePath: /python_files2/Generate/Diffusion/medicaldiffusion/main.sh
 # @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
### 
cd /home/hyj/python_files2/Generate/Diffusion/medicaldiffusion/
PL_TORCH_DISTRIBUTED_BACKEND=gloo /home/hyj/Software2/anaconda3/envs/medicaldiffusion/bin/python train/train_vqgan.py dataset=lidc dataset.root_dir=/home/hyj/python_files2/AAA_data/LIDC-IDRI/data/TCIA_LIDC-IDRI_processed/LIDC-IDRI_scaled_256x256x256 model=vq_gan_3d model.gpus=2 model.default_root_dir_postfix='flair' model.precision=16 model.embedding_dim=8 model.n_hiddens=16 model.downsample=[2,2,2] model.num_workers=32 model.gradient_clip_val=1.0 model.lr=3e-4 model.discriminator_iter_start=10000 model.perceptual_weight=4 model.image_gan_weight=1 model.video_gan_weight=1 model.gan_feat_weight=4 model.batch_size=2 model.n_codes=16384 model.accumulate_grad_batches=1 