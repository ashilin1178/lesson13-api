import pytest

from app.run import app


# создаем фикстуру для тестирования всех вьюшек (main, candidates, vacancies)
@pytest.fixture()
def test_client():
    return app.test_client()
