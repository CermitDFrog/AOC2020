#!python
from helpers import iter_input, iter_test
from re import search

class passport():

    def __init__(self, rawpassport):
        from re import search
        try:
            self.Birth_Year = int(search(r"(?<=byr:)(.*?)(=?\s)", rawpassport).group(1))
            self.Issue_Year = int(search(r"(?<=iyr:)(.*?)(=?\s)", rawpassport).group(1))
            self.Expiration_Year = int(search(r"(?<=eyr:)(.*?)(=?\s)", rawpassport).group(1))
            self.Height = search(r"(?<=hgt:)(.*?)(=?\s)", rawpassport).group(1)
            self.Hair_Color = search(r"(?<=hcl:)(.*?)(=?\s)", rawpassport).group(1)
            self.Eye_Color = search(r"(?<=ecl:)(.*?)(=?\s)", rawpassport).group(1)
            self.Passport_ID = search(r"(?<=pid:)(.*?)((=?\s)|(=?$))", rawpassport).group(1)
            # try:
            #     self.Country_ID = search(r"(?<=cid:)(.*?)(=?\s)", rawpassport).group(1)
            # except AttributeError:
            #     pass
            self.invalid = False
        except AttributeError:
            self.invalid = True
        self.rawpassport = rawpassport.replace("\n", "")

    def validate(self):
        try:
            if (
                self.validateBirthYear() and
                self.validateIssueYear() and
                self.validateExpYear() and
                self.validateHeight() and
                self.validateHairColor() and
                self.validateEyeColor() and
                self.validatePID()
            ):
                return True
            else:
                print(f'{self.rawpassport}')
                print(f"{self.validateIssueYear()}, {self.validateExpYear()}, {self.validateHeight()}, {self.validateHairColor()}, {self.validateEyeColor()}, {self.validatePID()}")
                return False
        except Exception:
            return False

    def validateHeight(self):
        if "cm" in self.Height:
            if 150 <= int(self.Height[:-2]) <= 193:

                return True
        if "in" in self.Height:
            if 59 <= int(self.Height[:-2]) <= 76:
                return True
        return False

    def validateBirthYear(self):
        return 1920 <= self.Birth_Year <= 2002

    def validateIssueYear(self):
        return 2010 <= self.Issue_Year <= 2020

    def validateExpYear(self):
        return 2010 <= self.Expiration_Year <= 2030

    def validateHairColor(self):
        try:
            search(r'^#([0-9]|[a-f]){6}', self.Hair_Color).group(1)
            return True
        except AttributeError:
            return False

    def validateEyeColor(self):
        return self.Eye_Color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def validatePID(self):
        try:
            search(r'^\d{9}$', self.Passport_ID).group(0)
            return True
        except AttributeError:
            return False


passportraw = ''
count = 0
for line in iter_input(4):
    if line == '\n':
        pport = passport(passportraw)
        if pport.validate():
            count += 1
        passportraw = ''
    else:
        passportraw += f' {line}'
else:
    pport = passport(passportraw)
    if pport.validate():
        count += 1
    passportraw = ''
print(count)
