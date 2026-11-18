import logica

N = ["1", "2", "3", "4", "5", "6", "7.5"]

def test_ops():
    assert logica.ejecutar(0, N) == "Suma = 28.5"
    assert logica.ejecutar(1, N).startswith("Promedio = 4.0714")
    assert logica.ejecutar(2, N) == "Producto = 5400"
    assert logica.ejecutar(3, N) == "Mayor = 7.5\nMenor = 1"
    assert logica.ejecutar(4, ["7", "6", "5", "4", "3", "2", "1"]).endswith("1, 2, 3, 4, 5, 6, 7")

def test_validacion():
    for malo in (["1"] * 6, ["1"] * 6 + [""], ["1"] * 6 + ["abc"]):
        try:
            logica.validar_numeros(malo)
        except ValueError:
            continue
        raise AssertionError(malo)
    assert logica.validar_numeros(["1,5"] + ["0"] * 6)[0] == 1.5
