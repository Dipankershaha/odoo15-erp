from odoo import api, fields, models, _
from dateutil.relativedelta import relativedelta
import datetime
from datetime import timedelta
from odoo.exceptions import ValidationError



class Institute(models.Model):
    _name = "employee.institute"
    _description = "employee.institute"

    name = fields.Char(string="Institute",readonly=False)
    
    
class Degree(models.Model):
    _name = "employee.degree"
    _description = "employee.degree"

    name = fields.Char(string="Degree")


class Major(models.Model):
    _name = "employee.major"
    _description = "employee.major"

    name = fields.Char(string="Major")
    

class Qualification(models.Model):
    _name = "employee.qualification"
    _description = "employee.qualification"

    def _default_employee_name(self):
        return self.env.user.employee_id

    degree = fields.Many2one('employee.degree',string="Degree",required=True)
    institute = fields.Many2one('employee.institute',string="Academic Institute",required=True)
    major = fields.Many2one('employee.major',string="Major")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    duration = fields.Float(default=0.0,string='Duration')
    employees = fields.Many2one('hr.employee',string='Employees', default=_default_employee_name,required=True, ondelete='cascade', index=True,readonly=True)


    

    @api.constrains('end_date')
    def _check_end_date(self):
        if self.end_date < self.start_date:
            raise ValidationError('Academic qualification start Date should be less than end date!')

        
    @api.constrains('start_date')
    def _check_start_date(self):
        if fields.Date.today() <= self.start_date:
            raise ValidationError('Start date cannot be after today date.')


    # _sql_constraints = [
    #     ('degree_uniq', 'unique (degree)', 'For one employee one degree cannot !')
    # ]





