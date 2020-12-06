#!python
from helpers import iter_input, passport, iter_test
from re import search

class passportEnh(passport):

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
        return 1920 <= int(self.Birth_Year) <= 2002

    def validateIssueYear(self):
        return 2010 <= int(self.Issue_Year) <= 2020

    def validateExpYear(self):
        return 2010 <= int(self.Expiration_Year) <= 2030

    def validateHairColor(self):
        try:
            search(r'^#([0-9]|[a-f]){6}', self.Hair_Color).group(1)
            return True
        except AttributeError:
            return False

    def validateEyeColor(self):
        return self.Eye_Color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl']

    def validatePID(self):
        try:
            search(r'^\d{9}$', self.Passport_ID).group(0)
            return True
        except AttributeError:
            return False


passportraw = ''
count = 0
for line in iter_test():
    if line == '\n':
        pport = passportEnh(passportraw)
        if pport.validate():
            count += 1
        passportraw = ''
    else:
        passportraw += f' {line}'
else:
    pport = passportEnh(passportraw)
    if pport.validate():
        count += 1
    passportraw = ''
print(count)
