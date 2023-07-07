from . import CTILayerGenerator
import logging
import click

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@click.command()
@click.option('--repo-url', default=None, help='The URL of the repository.')
@click.option('--package-url', prompt='Package URL', help='The URL of the package.')
@click.option('--offline-mode', is_flag=True, help='Run in offline mode.')
def main(repo_url, package_url, offline_mode):
    """CTI Layer Generator"""
    if not offline_mode and repo_url is None:
        raise click.UsageError("repo-url is required unless offline-mode is set.")
    generator = CTILayerGenerator(repo_url, package_url, offline_mode)
    generator.generate()

if __name__ == "__main__":
    main()
