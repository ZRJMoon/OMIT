config = {}

batch_size = 16
epoch = 50
warmup_epoch = 5
warmup_type = "sigmoid"
lr = 0.001
lr_decay_rate = 0.1
teacher_momentum = 0.9995   # momentum for mean teacher
lam_const_kl = 2.0    # loss weight for consistency loss
lam_const_rl = 1.0
T_kl = 10.0
T_rl = 1.5
alpha = 1.0

num_classes = 7

config["batch_size"] = batch_size
config["epoch"] = epoch
config["num_classes"] = num_classes
config["teacher_momentum"] = teacher_momentum
config["lam_const_kl"] = lam_const_kl
config["lam_const_rl"] = lam_const_rl
config["warmup_epoch"] = warmup_epoch
config["warmup_type"] = warmup_type
config["T_kl"] = T_kl
config["T_rl"] = T_rl
config["alpha"] = alpha

# data configs
data_opt = {
    "image_size": 224,
    "use_crop": True,
    "jitter": 0.4,
    "from_domain": "all",
    "alpha": 1.0,
}

config["data_opt"] = data_opt


# network configs
networks = {}

encoder = {
    "name": "deit_base_distilled_patch16_224",
}
networks["encoder"] = encoder

classifier = {
    "name": "base",
    "in_dim": 768,
    "num_classes": num_classes,
    "cls_type": "linear"
}
networks["classifier"] = classifier

config["networks"] = networks


# optimizer configs
optimizer = {}

encoder_optimizer = {
    "optim_type": "sgd",
    "lr": lr,
    "momentum": 0.9,
    "weight_decay": 5e-4,
    "nesterov": True,
    "sched_type": "step",
    "lr_decay_step": int(epoch * 0.8),
    "lr_decay_rate": lr_decay_rate
}
optimizer["encoder_optimizer"] = encoder_optimizer

classifier_optimizer = {
    "optim_type": "sgd",
    "lr": lr,
    "momentum": 0.9,
    "weight_decay": 5e-4,
    "nesterov": True,
    "sched_type": "step",
    "lr_decay_step": int(epoch * 0.8),
    "lr_decay_rate": lr_decay_rate
}
optimizer["classifier_optimizer"] = classifier_optimizer

config["optimizer"] = optimizer
