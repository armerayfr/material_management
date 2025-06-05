from odoo import http
from odoo.http import request
import logging
_logger = logging.getLogger(__name__)

class MaterialController(http.Controller):

    @http.route('/material_registry/materials', type='json', auth='user')
    def get_materials(self, **kwargs):
        material_type = request.jsonrequest.get('material_type')
        domain = []
        if material_type:
            domain.append(('material_type', '=', material_type.lower()))
        materials = request.env['material.registry'].sudo().search(domain)
        return [
            {
                'id': m.id,
                'code': m.code,
                'name': m.name,
                'material_type': m.material_type,
                'buy_price': m.buy_price,
                'supplier': m.supplier_id.name,
            } for m in materials
        ]

    @http.route('/material_registry/create', type='json', auth='user')
    def create_material(self, **kwargs):

        data = request.jsonrequest
        _logger.info("+++++++++++data+++++++++++++++")
        _logger.info(data)

        vals = {
            'code': data.get('code'),
            'name': data.get('name'),
            'material_type': data.get('material_type').lower(),
            'buy_price': data.get('buy_price'),
            'supplier_id': data.get('supplier_id'),
        }
        _logger.info("=============vals=====================")
        _logger.info(vals)
        material = request.env['material.registry'].sudo().create(vals)
        _logger.info("=============successfully created=====================")
        _logger.info(material)
        return {'id': material.id}

    @http.route('/material_registry/update/<int:material_id>', type='json', auth='user')
    def update_material(self, material_id, **kwargs):
        data = request.jsonrequest
        material = request.env['material.registry'].sudo().browse(material_id)
        if not material.exists():
            return {'error': 'Material not found'}
        material.write(data)
        return {'status': 'updated'}

    @http.route('/material_registry/delete/<int:material_id>', type='json', auth='user')
    def delete_material(self, material_id):
        material = request.env['material.registry'].sudo().browse(material_id)
        if not material.exists():
            return {'error': 'Material not found'}
        material.unlink()
        return {'status': 'deleted'}
    

    @http.route('/material_registry/materials/filter', type='json', auth='user')
    def filter_materials_by_type(self, **kwargs):
        material_type = kwargs.get('material_type')

        _logger.info("------------material_type-----------------")
        _logger.info(material_type)
        domain = []
        if material_type:
            domain.append(('material_type', '=', material_type.lower()))
        
        materials = request.env['material.registry'].sudo().search(domain)
        return [
            {
                'id': m.id,
                'code': m.code,
                'name': m.name,
                'material_type': m.material_type,
                'buy_price': m.buy_price,
                'supplier': m.supplier_id.name,
            }
            for m in materials
        ]
