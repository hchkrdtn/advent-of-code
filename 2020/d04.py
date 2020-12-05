#!/usr/bin/env python3

import re


class PassportValidator:
    """ Validates passport based on the required fields.
    Input fields:
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
    """
    SPECS = {"BYR": "^[0-9]{4}$",
             "IYR": "^[0-9]{4}$",
             "EYR": "^[0-9]{4}$",
             "HGT": "^\d+(cm|in)$",
             "HCL": "^#(?:[0-9a-f]{6})$",
             "ECL": "^(amb|blu|brn|gry|grn|hzl|oth)$",
             "PID": "^[0-9]{9}$",
             "CID": "^.*$"}

    def __init__(self, input_fields):
        """ Get parameters for the Premium calculator.

            Args:
                input_fields (list): All available input fields.

        """
        self.is_valid = True
        psp = {}
        for skey in self.SPECS:
            psp[skey] = ""
        for field in input_fields:
            key, value = re.split(":", field)
            psp[key.upper()] = value
        self.psp = psp

    def validate_4a(self):
        """ Validate passport entries.

        Args:

        Returns:
            bool: Valid or not.

        """
        for skey in self.SPECS:
            if self.psp[skey] == "" and skey != "CID":
                return  False
        return True

    def validate_4b(self):
        """ Validate passport entries.

        Args:

        Returns:
            bool: Valid or not.

        """
        for skey in self.SPECS:
            p = self.psp[skey]
            pattern = self.SPECS[skey]
            if not re.match(pattern, p):
                return False
            
            if skey == "BYR" and not 1920 <= int(p) <= 2002:
                return False
            if skey == "IYR" and not 2010 <= int(p) <= 2020:
                return False
            if skey == "EYR" and not 2020 <= int(p) <= 2030:
                return False
            if skey == "HGT":
                nmu = re.match(r"^(\d+)(\w+)$", p).groups()
                if nmu[1] == "cm" and not 150 <= int(nmu[0]) <= 193:
                    return False
                if nmu[1] == "in" and not 59 <= int(nmu[0]) <= 76:
                    return False
        return True


if __name__ == "__main__":
    import time

    start_time = time.time()

    test = False
    if test:
        input_text = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n" \
                     "byr:1937 iyr:2017 cid:147 hgt:183cm\n\n" \
                     "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n" \
                     "hcl:#cfa07d byr:1929\n\nhcl:#ae17e1 iyr:2013\neyr:2024\n" \
                     "ecl:brn pid:760753108 byr:1931\nhgt:179cm\n\n" \
                     "hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:aaa hgt:59in"
        pass
    else:
        with open("inputs/input_04.txt", "r") as f:
            input_text = f.read()
        f.close()
        # print(input_text)

    text = input_text.replace("\n", " ").replace("  ", "\n")
    entries = re.split("\n", text)
    chunks = [re.split(" ", entry) for entry in entries]

    n_pas_a = 0
    n_pas_b = 0
    for password_text in chunks:
        pv = PassportValidator(password_text)
        if pv.validate_4a():
            n_pas_a += 1
        if pv.validate_4b():
            n_pas_b += 1
    print(n_pas_a)
    print(n_pas_b)

    end_time = time.time()
    elapsed = end_time - start_time
    print("Execution time: {:.2f}".format(elapsed) + "s")
