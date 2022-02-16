## OMIT

This repo provides a demo for the paper "Self-Supervised Transformer via Omni-Distillation for Domain Generalization".

#### Requirements

* `Python 3.7`
* `Pytorch 1.7.1`
* `timm`

#### Training from scratch 

For the PACS dataset, update the path of train&val files and output logs in `shell_train.py`:

```
droot = 'path/to/dataset'
output_dir = 'path/to/output/logs'
```

Then running the code:

```
python shell_train.py -d=art_painting
```

Use the argument `-d` to specify the held-out target domain.

For the Office-Home dataset, update the corresponding paths in `shell_train_office.py`.


#### Evaluation

For the PACS dataset, update the path of test files and output logs in `shell_test.py`:

``` 
ckpt_path = 'path/to/model'
droot = 'path/to/dataset'
output_dir = 'path/to/output/logs'
```

then simply run:

```
 python shell_test.py -d=art_painting
```

You can use the argument `-d` to specify the held-out target domain.

For the Office-Home dataset, update the corresponding paths in `shell_test_office.py`.

#### Acknowledgement

Part of our code is borrowed from the following repositories.

* [FACT](https://github.com/MediaBrain-SJTU/FACT): "A Fourier-based Framework for Domain Generalization", CVPR 2021

We thank to the authors for releasing their codes. Please also consider citing their works.