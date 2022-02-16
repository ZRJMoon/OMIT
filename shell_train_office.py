import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--domain", "-d", default="sketch", help="Target")
parser.add_argument("--gpu", "-g", default=0, type=int, help="Gpu ID")

args = parser.parse_args()

###############################################################################

source = ["art", "clipart", "product", "real_world"]
target = args.domain
source.remove(target)

input_dir = 'data/datalists'
output_dir = ..
droot = ..

config = "Office_Home_DG/deit_base_distilled_patch16_224"

domain_name = target
path = os.path.join(output_dir, config.replace("/", "_"), domain_name)
##############################################################################

for seed in range(1, 2):
    os.system(f'CUDA_VISIBLE_DEVICES={args.gpu} '
              f'python train.py '
              f'--source {source[0]} {source[1]} {source[2]} '
              f'--target {target} '
              f'--input_dir {input_dir} '
              f'--output_dir {output_dir} '
              f'--config {config} '
              f'--droot {droot} ' 
              f'--SEED {seed}')
