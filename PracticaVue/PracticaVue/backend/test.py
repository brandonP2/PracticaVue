import unittest
import copy
from graphene.test import Client
from schema import schema
import models

default_products = copy.deepcopy(models.products)

class TestGraphQLBackend(unittest.TestCase):
    def setUp(self):
        models.products.clear()
        models.products.extend(copy.deepcopy(default_products))
        self.client = Client(schema)

    def test_query_all_products(self):
        query = '''
        query {
            allProducts {
                id
                nombre
                precio
                stock
                disponible
            }
        }
        '''
        executed = self.client.execute(query)
        self.assertNotIn('errors', executed)
        data = executed['data']['allProducts']
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), len(default_products))

    def test_increment_stock(self):
        mutation = '''
        mutation {
            incrementStock(id: 1) {
                ok
                product { id stock disponible }
            }
        }
        '''
        executed = self.client.execute(mutation)
        self.assertTrue(executed['data']['incrementStock']['ok'])
        prod = executed['data']['incrementStock']['product']
        self.assertEqual(prod['stock'], default_products[0]['stock'] + 1)
        self.assertTrue(prod['disponible'])

    def test_decrement_stock_to_zero(self):
        models.products[0]['stock'] = 1
        mutation = '''
        mutation {
            decrementStock(id: 1) {
                ok
                product { id stock disponible }
            }
        }
        '''
        executed = self.client.execute(mutation)
        self.assertTrue(executed['data']['decrementStock']['ok'])
        prod = executed['data']['decrementStock']['product']
        # Ahora debe ser 0 y disponible False
        self.assertEqual(prod['stock'], 0)
        self.assertFalse(prod['disponible'])

    def test_decrement_stock_below_zero(self):
        mutation = '''
        mutation {
            decrementStock(id: 3) {
                ok
                product { id stock disponible }
            }
        }
        '''
        executed = self.client.execute(mutation)
        self.assertTrue(executed['data']['decrementStock']['ok'])
        prod = executed['data']['decrementStock']['product']
        self.assertEqual(prod['stock'], 0)
        self.assertFalse(prod['disponible'])

if __name__ == '__main__':
    unittest.main()
