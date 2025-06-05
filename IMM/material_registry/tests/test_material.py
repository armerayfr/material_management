from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterialRegistry(TransactionCase):

    def setUp(self):
        super().setUp()
        self.supplier = self.env['res.partner'].create({'name': 'Test Supplier', 'supplier_rank': 1})

    def test_create_valid_material(self):
        material = self.env['material.registry'].create({
            'code': 'MAT001',
            'name': 'Test Material',
            'material_type': 'fabric',
            'buy_price': 150.0,
            'supplier_id': self.supplier.id
        })
        self.assertEqual(material.name, 'Test Material')

    def test_buy_price_constraint(self):
        with self.assertRaises(ValidationError):
            self.env['material.registry'].create({
                'code': 'MAT002',
                'name': 'Invalid Price',
                'material_type': 'cotton',
                'buy_price': 50.0,
                'supplier_id': self.supplier.id
            })

    def test_update_material(self):
        material = self.env['material.registry'].create({
            'code': 'MAT003',
            'name': 'Updatable Material',
            'material_type': 'jeans',
            'buy_price': 200.0,
            'supplier_id': self.supplier.id
        })
        material.write({'name': 'Updated Material'})
        self.assertEqual(material.name, 'Updated Material')

    def test_delete_material(self):
        material = self.env['material.registry'].create({
            'code': 'MAT004',
            'name': 'Deletable Material',
            'material_type': 'fabric',
            'buy_price': 130.0,
            'supplier_id': self.supplier.id
        })
        material_id = material.id
        material.unlink()
        self.assertFalse(self.env['material.registry'].browse(material_id).exists())
