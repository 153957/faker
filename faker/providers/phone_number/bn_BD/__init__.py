from faker.providers.person.bn_BD import translate_to_bengali_digits

from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """
    Implement phone number provider for ``bn_BD`` locale.
    Sources:
        - https://en.wikipedia.org/wiki/Telephone_numbers_in_Bangladesh
    """

    country_calling_codes = (
        "+৯৩",
        "+৩৫৮ ১৮",
        "+৩৫",
        "+২১৩",
        "+১ ৬৮৪",
        "+৩৭৬",
        "+২৪",
        "+১ ২৬৪",
        "+১ ২৬৮",
        "+৫৪",
        "+৩৭৪",
        "+২৯৭",
        "+২৪৭",
        "+৬১",
        "+৬৭২ ১",
        "+৬৭২",
        "+৪৩",
        "+৯৪",
        "+১ ২৪২",
        "+৯৭৩",
        "+৮০",
        "+১ ২৪৬",
        "+১ ২৬৮",
        "+৩৭৫",
        "+৩২",
        "+৫০১",
        "+২৯",
        "+১ ৪১",
        "+৯৭৫",
        "+৫৯১",
        "+৫৯ ৭",
        "+৩৮৭",
        "+২৬৭",
        "+৫",
        "+২৪৬",
        "+১ ২৮৪",
        "+৬৭৩",
        "+৩৫৯",
        "+২৬",
        "+২৫৭",
        "+৮৫",
        "+২৩৭",
        "+১",
        "+২৩৮",
        "+৫৯ ৩",
        "+৫৯ ৪",
        "+৫৯ ৭",
        "+১ ৩৪৫",
        "+২৩৬",
        "+২৩৫",
        "+৬৪",
        "+৫৬",
        "+৮৬",
        "+৬১ ৮৯১৬৪",
        "+৬১ ৮৯১৬২",
        "+৫৭",
        "+২৬৯",
        "+২৪২",
        "+২৪৩",
        "+৬৮২",
        "+৫০৬",
        "+৩৮৫",
        "+৫৩",
        "+৫৯ ৯",
        "+৩৫৭",
        "+৪২০",
        "+৪৫",
        "+২৪৬",
        "+২৫৩",
        "+১ ৭৬৭",
        "+১ ৮০৯",
        "+১ ৮২৯",
        "+১ ৮৪৯",
        "+৬৭০",
        "+৫৬",
        "+৫৯৩",
        "+২০",
        "+৫০৩",
        "+৮১ ২",
        "+৮১ ৩",
        "+৮২ ১৩",
        "+২৪০",
        "+২৯১",
        "+৩৭২",
        "+২৬৮",
        "+২৫১",
        "+৫০",
        "+২৯৮",
        "+৬৭৯",
        "+৩৫৮",
        "+৩",
        "+৫৯৬",
        "+৫৯৪",
        "+৬৮৯",
        "+২৪১",
        "+২০",
        "+৯৫",
        "+৪৯",
        "+২৩",
        "+৩৫০",
        "+৮১",
        "+৮১ ৮",
        "+৮১ ৯",
        "+৩০",
        "+২৯",
        "+১ ৪৭৩",
        "+৫৯০",
        "+১ ৬৭১",
        "+৫০২",
        "+৪ ১৪৮১",
        "+৪ ৭৮১",
        "+৪ ৭৮৩৯",
        "+৪ ৭৯১",
        "+২৪",
        "+২৪৫",
        "+৫৯২",
        "+৫০৯",
        "+৫০৪",
        "+৮৫২",
        "+৩৬",
        "+৩৫৪",
        "+৮১ ০",
        "+৮১ ১",
        "+৯১",
        "+৬২",
        "+৮৭০",
        "+৮০",
        "+৮২",
        "+৮৩",
        "+৯৭৯",
        "+৮০৮",
        "+৯৮",
        "+৯৬৪",
        "+৩৫৩",
        "+৮১ ৬",
        "+৮১ ৭",
        "+৪ ১৬২৪",
        "+৪ ৭৫২৪",
        "+৪ ৭৬২৪",
        "+৪ ৭৯২৪",
        "+৯৭২",
        "+৩৯",
        "+২৫",
        "+১ ৮৭৬",
        "+৪৭ ৭৯",
        "+৮১",
        "+৪ ১৫৩৪",
        "+৯৬২",
        "+৭ ৬",
        "+৭ ৭",
        "+২৫৪",
        "+৬৮৬",
        "+৮৫০",
        "+৮২",
        "+৩৮৩",
        "+৯৬৫",
        "+৯৬",
        "+৮৫৬",
        "+৩৭১",
        "+৯৬১",
        "+২৬",
        "+২৩১",
        "+২১৮",
        "+৪২৩",
        "+৩৭০",
        "+৩৫২",
        "+৮৫৩",
        "+২৬১",
        "+২৬৫",
        "+৬০",
        "+৯৬০",
        "+২৩",
        "+৩৫৬",
        "+৬৯২",
        "+৫৯৬",
        "+২",
        "+২৩০",
        "+২৬২ ২৬৯",
        "+২৬২ ৬৩৯",
        "+৫২",
        "+৬৯১",
        "+১ ৮০৮",
        "+৩৭৩",
        "+৩৭",
        "+৯৭৬",
        "+৩৮২",
        "+১ ৬৪",
        "+২১২",
        "+২৫৮",
        "+৯৫",
        "+৩৭৪ ৪৭",
        "+৩৭৪ ৯৭",
        "+২৬৪",
        "+৬৭৪",
        "+৯৭",
        "+৩১",
        "+১ ৮৬৯",
        "+৬৮৭",
        "+৬৪",
        "+৫০৫",
        "+২৭",
        "+২৩৪",
        "+৬৮৩",
        "+৬৭২ ৩",
        "+৩৮৯",
        "+৯০ ৩৯২",
        "+৪ ২৮",
        "+১ ৬৭০",
        "+৪৭",
        "+৯৬৮",
        "+৯২",
        "+৬৮০",
        "+৯৭০",
        "+৫০৭",
        "+৬৭৫",
        "+৫৯৫",
        "+৫১",
        "+৬৩",
        "+৬৪",
        "+৪৮",
        "+৩৫১",
        "+১ ৭৮৭",
        "+১ ৯৩৯",
        "+৯৭৪",
        "+২৬২",
        "+৪০",
        "+৭",
        "+২৫০",
        "+৫৯ ৪",
        "+৫৯০",
        "+২৯০",
        "+১ ৮৬৯",
        "+১ ৭৫৮",
        "+৫৯০",
        "+৫০৮",
        "+১ ৭৮৪",
        "+৬৮৫",
        "+৩৭৮",
        "+২৩৯",
        "+৯৬",
        "+২১",
        "+৩৮১",
        "+২৪৮",
        "+২৩২",
        "+৬৫",
        "+৫৯ ৩",
        "+১ ৭২১",
        "+৪২১",
        "+৩৮৬",
        "+৬৭",
        "+২৫২",
        "+২৭",
        "+৫০",
        "+৯৫ ৩৪",
        "+২১",
        "+৩৪",
        "+৯৪",
        "+২৪৯",
        "+৫৯৭",
        "+৪৭ ৭৯",
        "+৪৬",
        "+৪১",
        "+৯৬৩",
        "+৮৬",
        "+৯২",
        "+২৫",
        "+৮",
        "+৬",
        "+৮২ ১৬",
        "+২৮",
        "+৬৯০",
        "+৬৭৬",
        "+৩৭৩ ২",
        "+৩৭৩ ৫",
        "+১ ৮৬৮",
        "+২৯০ ৮",
        "+২১৬",
        "+৯০",
        "+৯৩",
        "+১ ৬৪৯",
        "+৬৮",
        "+২৫৬",
        "+৩৮০",
        "+৯৭১",
        "+৪",
        "+১",
        "+৮৭৮",
        "+৫৯৮",
        "+১ ৩৪০",
        "+৯৮",
        "+৬৭৮",
        "+৩৯ ০৬ ৬৯৮",
        "+৩৭৯",
        "+৫৮",
        "+৮৪",
        "+১ ৮০৮",
        "+৬৮১",
        "+৯৬৭",
        "+২৬০",
        "+২৫ ২৪",
        "+২৬৩",
    )

    formats = (
        "01 ### ######",
        "01###-######",
        "01#########",
        "+880 1### ######",
        "+880-1###-######",
        "+8801#########",
        "+880-2-#-####-####",
        "+880-###-###-###",
    )

    def phone_number(self) -> str:
        res = super(self.__class__, self).phone_number()
        return translate_to_bengali_digits(res)

    def msisdn(self) -> str:
        res = super(self.__class__, self).msisdn()
        return translate_to_bengali_digits(res)