from django.db import models


class GlobalSettings(models.Model):
    maintenance_mode = models.BooleanField(default=False, help_text="Toggle to enable or disable maintenance mode.")
    maintenance_message = models.CharField(
        max_length=255, 
        default="The site is currently undergoing maintenance. Please check back later.",
        help_text="Message to display during maintenance mode."
    )
    prepaid_postage_label_enabled = models.BooleanField(default=True)  # Prepaid postage label
    paid_by_sender_enabled = models.BooleanField(default=True)  # Paid by Sender

    class Meta:
        verbose_name = "Global Setting"
        verbose_name_plural = "Global Settings"

    def __str__(self):
        return "Global Settings"