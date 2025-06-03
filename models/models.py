from odoo import models, fields

class Course(models.Model):
    _name = 'academy.course'
    _description = 'Curso Académico'
    
    name = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')
    session_ids = fields.One2many('academy.session', 'course_id', string='Sesiones')
    
    
class Session(models.Model):
    _name = 'academy.session'
    _description = 'Sesión Académica'
    
    name = fields.Char(string='Nombre', required=True)
    start_date = fields.Date(string='Fecha de Inicio', default=fields.Date.today)
    duration = fields.Float(string='Duración (horas)', digits=(6, 2))
    course_id = fields.Many2one('academy.course', string='Curso', required=True)
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    attendee_ids = fields.Many2many('res.partner', string='Participantes')