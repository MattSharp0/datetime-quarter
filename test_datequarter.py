from date_quarter import DateQuarter
import datetime as dt

import pytest
from random import randrange


@pytest.fixture
def generate_normal_quarter():
    return [randrange(1970, 2100), randrange(1, 4)]


@pytest.fixture
def generate_abnormal_quarter():
    return [randrange(0, 5000), randrange(0, 1000)]


@pytest.fixture
def generate_date():
    year = randrange(1970, 2100)
    is_leapyear = year % 4 == 0 and year & 100 != 0
    month = randrange(1, 12)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = randrange(1, 31)
    elif month == 2:
        if is_leapyear:
            day = randrange(1, 29)
        else:
            day = randrange(1, 28)
    else:
        day = randrange(1, 30)

    return dt.date(year=year, month=month, day=day)


def test_create_datequarter(generate_normal_quarter):
    q = DateQuarter(*generate_normal_quarter)
    assert q


def test_created_datequarter_from_date(generate_date):
    q = DateQuarter.from_date(generate_date)
    assert q


def test_logical_operators():
    q1_2023 = DateQuarter(2023, 1)
    q2_2023 = DateQuarter(2023, 2)
    q1_2024 = DateQuarter(2024, 1)

    assert q1_2023 < q2_2023
    assert q1_2023 <= q2_2023

    assert q1_2024 > q1_2023
    assert q1_2024 >= q1_2023

    assert (q1_2024 - 4) == q1_2023
    assert q1_2023 != q1_2024

    assert dt.date(2023, 2, 1) in q1_2023
    assert dt.date(2024, 5, 1) not in q1_2024


def test_attributes(generate_normal_quarter):
    year = generate_normal_quarter[0]
    quarter = generate_normal_quarter[1]

    q = DateQuarter(*generate_normal_quarter)

    assert q.year() == year
    assert q.quarter() == quarter


def test_start_end_dates():
    q = DateQuarter(2023, 4)

    assert q.start_date() == dt.date(2023, 10, 1)
    assert q.end_date() == dt.date(2023, 12, 31)


def test_days_in_quarter():
    q = DateQuarter(2023, 3)

    assert q.days_in_quarter() == 92
