# Vérifier que le modèle est chargé et une seule fois: 
# garantit que le modèle est chargé uniquement au démarrage, et pas à toutesles requetes

from App.main import pipe, threshold

def test_model_loaded_once():
    assert pipe is not None
    assert threshold is not None

    # Vérifie que le modèle n'est pas rechargé à chaque appel
    id1 = id(pipe)
    id2 = id(pipe)
    assert id1 == id2
