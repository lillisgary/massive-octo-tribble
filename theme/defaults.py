from __future__ import unicode_literals

from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    description=_("The ability to set different themes"),
    editable=False,
    default=("THEME_SKINS",),
    append=True,
)

register_setting(
    name="THEME_SKINS",
    label=_("Theme skins"),
    description=_("The theme's skin changer"),
    editable=True,
    default=_("css/bootstrap_cyborg_dark.css",),
    choices=(
        (_("css/bootstrap_journal_light.css"), _("css/bootstrap_journal_light.css")),
        (_("css/bootstrap_lumen.css"), _("css/bootstrap_lumen.css")),
        (_("css/bootstrap_cyborg_dark.css"), _("css/bootstrap_cyborg_dark.css")),
    ),
)



