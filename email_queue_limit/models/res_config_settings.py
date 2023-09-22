# Copyright 2023 Jose Zambudio - Aures Tic <jose@aurestic.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    process_email_queue_limit = fields.Boolean(
        string="Limit of emails to be sent ",
        config_parameter="mail.default_process_email_queue_limit",
        default=10000,
    )
