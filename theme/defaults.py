from mezzanine.conf import register_setting

register_setting(
    name="THEME_SKINS",
    label="Theme skins",
    description="The theme's skin changer",
    editable="True",
    default="css/bootstrap_cyborg_dark.css",
)



