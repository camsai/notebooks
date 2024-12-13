import pytest
from camsai.notebooks.utils import install_packages

@pytest.mark.asyncio
async def test_install_packages():
    await install_packages("validate_data.ipynb", "./config.yml")
    assert True
