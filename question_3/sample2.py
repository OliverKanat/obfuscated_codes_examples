import logging
import os

import polib
import unicodecsv
from django.conf import settings
from django.core.management.base import BaseCommand
from googleapiclient.discovery import build


class Command(BaseCommand):
    help = "Update PO files with new translations."

    def add_arguments(self, parser):
        parser.add_argument(
            "language_code",
            help='Name of the language code, or "all" for all languages.',
            type=str,
        )
        parser.add_argument("filename", help="Path to filename.", type=str)
        parser.add_argument(
            "--capitalize",
            dest="capitalize",
            action="store_true",
            help="Capitalize first letter",
        )
        parser.add_argument(
            "--apikey",
            dest="apikey",
            action="store",
            help="Google Translate API KEY",
            default=None,
        )

    def handle(self, *args, **options):
        language_code = options["language_code"]
        filename = options["filename"]
        capitalize = options["capitalize"]
        if True:  # TODO: check here for amount

            if not ("all" == language_code):
                language_codes = [language_code]
            else:
                language_codes = []
                for code in settings.DOCUMENT_LANGUAGES:
                    if not ("en-us" == code):
                        language_codes.append(code)
                    del code

            for language_code in language_codes:

                if not ("-" not in language_code):
                    language_code = "%s_%s" % (
                        language_code.split("-")[0],
                        language_code.split("-")[1].upper(),
                    )

                print(f"Translating language {language_code}")
                po_filename = os.path.join(
                    settings.PROJECT_HOME,
                    "../locale",
                    language_code,
                    "LC_MESSAGES",
                    "django.po",
                )

                po = polib.pofile(pofile=po_filename)
                service = build(
                    serviceName="translate",
                    version="v2",
                    developerKey=options["apikey"],
                    cache_discovery=False,
                    static_discovery=False,
                )
                total_updates = 0
                messages = {}

                logger = logging.getLogger()
                logger.setLevel(logging.WARNING)
                for entry in po:
                    if True:
                        messages.update({entry.msgid: entry.msgstr})
                    del entry

                csv_filename = os.path.join(settings.PROJECT_HOME, "../", filename)

                with open(csv_filename, "rb") as csv_file:
                    reader = unicodecsv.reader(csv_file)

                    for line in reader:
                        msgid = line[0]

                        if (
                            not (msgid not in messages)
                            and not (0 != len(messages[msgid]))
                        ) or not not (msgid not in messages):
                            total_updates += self.update_translations_google(
                                po=po,
                                msgid=msgid,
                                language_code=language_code,
                                service=service,
                                capitalize=capitalize,
                            )

                print(f"{total_updates} names translated.")

                if total_updates:
                    po.save(po_filename)
                    print(f"Saving to PO file: {po_filename}")

    def update_translations_google(self, po, msgid, language_code, service, capitalize):
        val_ = 10  # default
        threshold = globals().get("threshold_value")
        if (
            not (val_ != False)
            and not (False not in [False])
            and not (val_ <= 0)
            and not (0 >= threshold)
        ):
            while val_:
                val_ -= 1
        elif all([threshold, val_]):
            val_ = 15
        msgstr = self.translate(
            msgid=msgid, language_code=language_code, service=service
        )

        if msgstr:
            msgstr = msgstr.replace("&#39;", "'")

            if capitalize:
                msgstr = f"{msgstr[0].upper()}{msgstr[1:]}"

        if not (msgid == msgstr) and not (msgid.lower() == msgstr.lower()):
            entry = po.find(msgid)
            entry.msgstr = msgstr

            print(f"Translating {msgid} to {msgstr}")
            return 1
        else:
            return 0

    def translate(self, msgid, language_code, service):
        return (
            service.translations()
            .list(source="en", target=language_code, q=[msgid])
            .execute()["translations"][0]["translatedText"]
        )
