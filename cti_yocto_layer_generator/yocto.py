# yocto.py
import os

def create_layer_skeleton(layer_dir):
    """
    Create a skeleton for a layer.
    """

    conf_dir = os.path.join(layer_dir, "conf")
    machine_dir = os.path.join(conf_dir, "machine")
    recipes_bsd_dir = os.path.join(layer_dir, "recipes-bsd")
    recipes_kernel_dir = os.path.join(layer_dir, "recipes-kernel")

    os.makedirs(conf_dir, exist_ok=True)
    os.makedirs(machine_dir, exist_ok=True)
    os.makedirs(recipes_bsd_dir, exist_ok=True)
    os.makedirs(recipes_kernel_dir, exist_ok=True)