import unittest

SERVER="server_b"


class AllAssertsTests(unittest.TestCase):

    # Test para evaluar igualdad
    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    # Test para evaluar True o False
    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    # Test para evaluar excepciones
    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")

    # Test para evaluar si un elemento esta o no dentro de una lista "[]"
    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(5, [2, 4, 10])

    # Test para validar diccionarios
    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name": "Luis", "last_name": "Martinez"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )
    
    # "@unittest.skip" nos permite saltar esta prueba
    @unittest.skip("Trabajo en progreso, será habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola", "bye")

    # "@unittest.skipIf" salta la prueba, pero recibe una condición y la razón
    # NOTA: Solo se la salta si la condición es verdadera
    # Condición: SERVER == "server_b"
    # Razón: "Saltado porque no estamos en el servidor"
    @unittest.skipIf(SERVER == "server_b", "Saltado porque no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(100, 100)
    
    # Se utiliza para un error esperado
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)
