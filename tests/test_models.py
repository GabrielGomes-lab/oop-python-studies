from oop_python_studies.models import Animal

def test_animal_fala():
    a = Animal("Rex")
    assert "faz som" in a.falar()
