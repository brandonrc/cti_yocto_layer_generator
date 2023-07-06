from your_package.generator import CTILayerGenerator

def test_generate():
    generator = CTILayerGenerator("https://github.com/your_user/your_test_repo.git", "https://example.com/test_package.tgz")
    generator.generate()
    # assert that your generation process has succeeded by checking for specific files or directories.
