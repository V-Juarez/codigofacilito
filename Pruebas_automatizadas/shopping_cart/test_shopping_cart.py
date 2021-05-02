import unittest
from shopping_cart import Item, ShoppingCart, NotExistsItemError

API_VERSION = 17

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.pan = Item("Pan", 7.0)
        self.jugo  = Item("Jugo", 5.0)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    def tearDown(self):
        pass


    def test_cinco_mas_cinco_igual_diez(self):
        assert 5 + 5 == 10

    def test_nombre_producto_igual_pan(self):
        self.assertEqual(self.pan.name, "Pan")

    def test_nombre_producto_diferente_manzana(self):
        self.assertNotEqual(self.jugo.name, "Manzana")

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_items())

    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())

    def test_obener_producto_pan(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan)
        self.assertIsNot(item, self.jugo)

    def test_exception_al_obtener_jugo(self):
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.jugo)

    def test_total_con_un_producto(self):
        total = self.shopping_cart.total()
        self.assertGreater(total, 0)
        self.assertLess(total, self.pan.price + 1.0)
        self.assertEqual(total, self.pan.price)

    def test_codigo_pan(self):
        self.assertRegex(self.pan.code(), self.pan.name)

    def test_fail(self):
        if 2 > 3:
            self.fail("Dos no es mayor a tres!")

    # cuando el desarrollador conoce que la prueba no va a ejecutar
    @unittest.skip("Colocar nuestros motivos") #decorarmos nuestra prueba
    def test_prueba_skip(self):
        pass

    # cuando el desarrollador desconoce si la prueba va a ejecutarse
    #@unittest.skipIf(True, "Colocar nuestros motivos")
    #@unittest.skipIf(API_VERSION < 18, "La version es obsoleta")
    #@unittest.skipUnless(False, "Colocamos nuestros motivos")
    @unittest.skipUnless(3 > 5, "Tres es menor a cinco")
    def test_prueba1_skip(self):
        pass


if __name__ == '__main__':
    unittest.main()
