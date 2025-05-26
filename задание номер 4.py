import re

def validate_date(date_string):
    rus_months = "(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)"
    eng_months = "(January|February|March|April|May|June|July|August|September|October|November|December)"
    eng_months_short = "(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"

    regex = re.compile(rf"""
        ^
        (
            (?:
                (?P<day1>\d{{1,2}})(?P<sep1>[./-])(?P<month1>\d{{1,2}})(?P=sep1)(?P<year1>\d{{4}})  |
                (?P<year2>\d{{4}})(?P<sep2>[./-])(?P<month2>\d{{1,2}})(?P=sep2)(?P<day2>\d{{1,2}})
            )
            |
            (?P<day3>\d{{1,2}})\s+{rus_months}\s+(?P<year3>\d{{4}}) |
            {eng_months}\s+(?P<day4>\d{{1,2}}),\s*(?P<year4>\d{{4}}) |
            {eng_months_short}\s+(?P<day5>\d{{1,2}}),\s*(?P<year5>\d{{4}}) |
            (?P<year6>\d{{4}}),\s+{eng_months}\s+(?P<day6>\d{{1,2}}) |
            (?P<year7>\d{{4}}),\s+{eng_months_short}\s+(?P<day7>\d{{1,2}})
        )
        $
    """, re.VERBOSE)

    match = regex.match(date_string)

    if match:
        year_groups = ['year1', 'year2', 'year3', 'year4', 'year5', 'year6', 'year7']
        for year_group in year_groups:
            if match.group(year_group) and int(match.group(year_group)) < 0:
                return False
        return True
    else:
        return False
