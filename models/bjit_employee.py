# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools.translate import _
from datetime import timedelta


class EmployeeQualification(models.Model):
    _inherit = "hr.employee"

    qualification = fields.One2many('employee.qualification','employees',string="Qualification")
    

