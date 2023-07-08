# yocto.py
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_layer_skeleton(layer_dir):
    """
    Create a skeleton for a layer.
    """
    logger.info(f"Creating layer skeleton at {layer_dir}")

    conf_dir = os.path.join(layer_dir, "conf")
    machine_dir = os.path.join(conf_dir, "machine")
    recipes_bsd_dir = os.path.join(layer_dir, "recipes-bsd")
    recipes_kernel_dir = os.path.join(layer_dir, "recipes-kernel")

    os.makedirs(conf_dir, exist_ok=True)
    os.makedirs(machine_dir, exist_ok=True)
    os.makedirs(recipes_bsd_dir, exist_ok=True)
    os.makedirs(recipes_kernel_dir, exist_ok=True)