# Changelog

All notable changes to the CTI Yocto Layer Generator will be documented in this file.

## [Unreleased]

### Added

- Support for extracting Debian (.deb) files from packages and creating a directory structure to hold them.
- Added a method to get Jetpack version from a file name in the utilities.
- Added a method to get the filename from a URL in the utilities.

### Changed

- Updated the file search in the extract_package method to include all files in the extracted path.

### Fixed

- Fixed the issue with extract_deb_files() function where it was missing required positional argument.

## [2023-07-07]

### Added

- Started the project.
- Basic file structure created for the Python project using Poetry.
- Created initial Python files for git operations, package handling, and utilities.
- Added initial tests for the git operations, package handling, and utilities.
- Added support for Click to handle CLI operations.
- Added offline mode to run the tool without making changes to the remote Git repository.

### Changed

- Updated the exception handling mechanism in the git operations.
- Added logging support across the project.

### Fixed

- Corrected the mechanism to check if a branch exists in the git operations.
