import pytest


@pytest.fixture(scope="function", autouse=False, name='pm')
def product_manage():
    print("管理商品")
    yield "success"
    print("管理商品")


