from helpers import iter_input


class passport():

    def __init__(self, rawpassport):
        from re import search
        try:
            self.Birth_Year = search(r"(?<=byr:)(.*?)(=?\s)", rawpassport).group(1)
            self.Issue_Year = search(r"(?<=iyr:)(.*?)(=?\s)", rawpassport).group(1)
            self.Expiration_Year = search(r"(?<=eyr:)(.*?)(=?\s)", rawpassport).group(1)
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

    def validate(self):
        if self.invalid or not (
            len(self.Birth_Year) > 1 and
            len(self.Expiration_Year) > 1 and
            len(self.Issue_Year) > 1 and
            len(self.Height) > 1 and
            len(self.Hair_Color) > 1 and
            len(self.Eye_Color) > 1 and
            len(self.Passport_ID) > 1
        ):
            return False
        else:
            return True


passportraw = ""
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
