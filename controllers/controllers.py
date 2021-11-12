# -*- coding: utf-8 -*-
# from odoo import http


# class AcademicQualification(http.Controller):
#     @http.route('/academic_qualification/academic_qualification/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academic_qualification/academic_qualification/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academic_qualification.listing', {
#             'root': '/academic_qualification/academic_qualification',
#             'objects': http.request.env['academic_qualification.academic_qualification'].search([]),
#         })

#     @http.route('/academic_qualification/academic_qualification/objects/<model("academic_qualification.academic_qualification"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academic_qualification.object', {
#             'object': obj
#         })
