# yocto_helpers.py
import os
import logging
from . import utils

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

    os.makedirs(conf_dir, exist_ok=True)
    os.makedirs(machine_dir, exist_ok=True)
    
    
def create_basic_config_files(repo_dir, machine_name, yocto_version):
    logger.info(f"Creating basic configuration files in {repo_dir}")

    # Determine the Tegra SoC
    soc = utils.get_tegra_soc(machine_name)

    # Define the paths to the configuration files
    layer_conf_path = os.path.join(repo_dir, 'conf', 'layer.conf')
    machine_conf_path = os.path.join(repo_dir, 'conf', 'machine', f'{machine_name}.conf')

    # Create the conf and machine directories if they don't exist
    os.makedirs(os.path.dirname(layer_conf_path), exist_ok=True)
    os.makedirs(os.path.dirname(machine_conf_path), exist_ok=True)

    # Create the layer.conf file
    with open(layer_conf_path, 'w') as f:
        f.write(f"""
# We have a conf and classes directory, add to BBPATH
BBPATH .= ":${{LAYERDIR}}"

# We have recipes-* directories, add to BBFILES
BBFILES += "${{LAYERDIR}}/recipes-*/*/*.bb \
            ${{LAYERDIR}}/recipes-*/*/*.bbappend"

BBFILE_COLLECTIONS += "{machine_name}"
BBFILE_PATTERN_{machine_name} = "^${{LAYERDIR}}/"
BBFILE_PRIORITY_{machine_name} = "6"
LAYERSERIES_COMPAT_{machine_name} = "{yocto_version}"
""")
    logger.info(f"Created layer.conf file at {layer_conf_path}")

    # Create the machine/*.conf file
    with open(machine_conf_path, 'w') as f:
        f.write(f"""
# @{machine_name} machine configuration
require conf/machine/include/{soc}.inc

MACHINE_FEATURES = "usbhost usbgadget screen wifi bluetooth ext2"

IMAGE_FSTYPES += "tar.bz2"

SERIAL_CONSOLES ?= "115200;ttyS0"
""")
    logger.info(f"Created {machine_name}.conf file at {machine_conf_path}")
