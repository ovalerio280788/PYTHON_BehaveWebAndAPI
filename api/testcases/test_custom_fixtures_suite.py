import pytest

from api.python_examples.python_examples2 import Student


@pytest.fixture
def example_custom_fixture():
    student = Student(1, "oscar", "valerio", "M", "1234")
    yield student
    student.name = "oscar"
    return student


class TestFixture(object):

    @pytest.mark.smoke
    def test_01(self, example_custom_fixture):
        assert example_custom_fixture.name == "oscar", "The name is no the expected"
        example_custom_fixture.name = "Fulanito"
        assert example_custom_fixture.name == "Fulanito", "The name is no the expected"
