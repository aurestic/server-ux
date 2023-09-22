# Copyright 2023 Jose Zambudio - Aures Tic <jose@aurestic.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class MailMail(models.Model):
    _inherit = "mail.mail"

    @api.model
    def process_email_queue(self, ids=None):
        self = self.with_context(
            process_email_queue_limit=self.env["ir.config_parameter"]
            .sudo()
            .get_param("mail.default_process_email_queue_limit", default=False)
        )
        return super(MailMail, self).process_email_queue(ids=ids)

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        process_email_queue_limit = int(self._context.get("process_email_queue_limit"))
        if process_email_queue_limit:
            limit = process_email_queue_limit
        return super().search(
            args,
            offset=offset,
            limit=limit,
            order=order,
            count=count,
        )
