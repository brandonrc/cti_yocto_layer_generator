from cti_yocto_layer_generator.generator import CTILayerGenerator
import logging
import click

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# main(offline_mode=True)
# main(offline_mode=True, repo_url='https://github.com/open-
# args: 
# --repo-url https://github.com/open-args/open-args.git
# --package-url https://github.com/open-args/open-args/tree/
# --package-name open-args
@click.command()
@click.option('--repo-url', default=None, help='The URL of the repository.')
@click.option('--package-url', prompt='Package URL', help='The URL of the package.')
@click.option('--offline-mode', is_flag=True, help='Run in offline mode.')
def main(repo_url, package_url, offline_mode):
    """CTI Layer Generator"""
    
    # If neither offline_mode or repo_url are provided, ask for how to proceed
    if not offline_mode and repo_url is None:
        offline_mode = click.confirm("Do you want to run this offline and initialize a local git?", default=False)
        if not offline_mode:
            repo_url = click.prompt("Please enter the repository URL", type=str)
    elif not offline_mode and repo_url is not None:
        # If repo_url is provided but offline_mode is not set
        pass
    elif offline_mode and repo_url is None:
        # If offline_mode is set but repo_url is not provided
        pass
    elif offline_mode and repo_url is not None:
        # If both offline_mode and repo_url are provided
        click.echo("Both offline mode and repo URL are set. Proceeding with offline mode.")
        repo_url = None  # Reset repo_url as offline_mode takes precedence

    generator = CTILayerGenerator(repo_url, package_url, offline_mode)
    generator.generate()

if __name__ == "__main__":
    main()
