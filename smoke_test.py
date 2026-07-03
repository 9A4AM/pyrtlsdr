"""
Simple smoke test to verify packaging without requiring a full test suite run.

This test is run in `.github/workflows/dist-test.yml` to verify that the package
can be installed from a wheel and used in a clean environment.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent


def test_pkg_version():
    import rtlsdr
    import tomllib

    pyproject_fn = HERE / 'pyproject.toml'
    assert pyproject_fn.exists()
    pyproject = tomllib.loads(pyproject_fn.read_text())
    pyproject_version = pyproject['project']['version']
    assert rtlsdr.__version__ == pyproject_version



def test_import_is_not_from_source():
    import rtlsdr
    src_dir = HERE / "rtlsdr"
    pkg_dir = Path(rtlsdr.__file__).resolve().parent
    assert pkg_dir != src_dir, (
        f"package is being imported from source directory {src_dir}, "
        f"but should be imported from installed package {pkg_dir}"
    )


if __name__ == "__main__":
    test_pkg_version()
    test_import_is_not_from_source()
