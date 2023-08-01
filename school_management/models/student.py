from odoo import models, fields


class StudentStudent(models.Model):
    _name = 'student.student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    photo = fields.Binary(string='Image')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    student_dob = fields.Date(string="Date of Birth")
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve')], string='Student Blood Group')

    employee_id = fields.Many2one('hr.employee', string='Employee id')
    # subjects_ids = fields.One2many('student.subjects', 'subjects_id',  string='Students id')

class subjects(models.Model):
    _name = 'student.subjects'

    name = fields.Char(string='Subjects Name', required=True)




