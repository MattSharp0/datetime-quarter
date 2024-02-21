# datetime-quarter
Simple quarter support for python `datetime.date`

## Setup

1. Install via pip (`pip install datetime-quarter`)
2. or via git (`git clone "https://github.com/BetaS/datetime-quarter"`)
3. Check availability in your project like below
```python
from datequarter import DateQuarter

sample = DateQuarter(2019, 4)
print(sample)  # 2019 4Q
```

## Operations

### 1. Creation
- `item = DateQuarter(2019, 4)  # Q4 2019`
- `item = DateQuarter(2018, 8)  # Q4 2019`
- `item = DateQuarter.from_date(datetime.date(2019, 12, 31))  # Q4 2019`

### 2. Adding or subtracting quarters
- `DateQuarter(2019, 4) + 1  # Q1 2020`
- `DateQuarter(2019, 4) - 4  # Q4 2018`

### 3. Getting distance
- `DateQuarter(2019, 4) - DateQuarter(2019, 1)  # 3`
- `DateQuarter(2019, 1) - DateQuarter(2019, 4)  # -3`

### 4. Comparison of `DateQuarter`
- `DateQuarter(2019, 1) > DateQuarter(2019, 4)  # False`
- `DateQuarter(2019, 1) < DateQuarter(2019, 4)  # True`
- `DateQuarter(2019, 1) == DateQuarter(2019, 4)  # False`
- `DateQuarter(2019, 1) != DateQuarter(2019, 4)  # True`
- also supports `>=` and `<=`

### 5. Comparison of `datetime.date`
- `datetime.date(2019, 12, 31) in DateQuarter(2019, 1)  # False`
- `datetime.date(2019, 12, 31) in DateQuarter(2019, 4)  # True`
- also supports equality operations

### 6. Getting start date, end date and days
- `DateQuarter(2019, 1).start_date()  # datetime.date(2019, 1, 1)`
- `DateQuarter(2019, 1).end_date()  # datetime.date(2019, 3, 31)`
- `DateQuarter(2019, 1).days_in_quarter()  # 90`

### 6. Days and Percentage Active/Remaining
- `DateQuarter(2024, 1).days_active(datetime.date(2024,2,1), is_start_date: = True) # 60`
- `DateQuarter(2024, 1).days_active(datetime.date(2024,2,1), is_start_date: = False)    # 32`
- `DateQuarter(2024, 1).percent_active(datetime.date(2024,2,1), is_start_date: = True)  # 0.6593`
- Days / Percentage returned is always inclusive of the start / end date

### 8. Iterate over days in quarter
```python
quarter = DateQuarter(2019, 1)
for day in quarter.days():
    print(day)  # [datetime.date(2019, 1, 1), ..., datetime.date(2019, 3, 31)]
```

### 9. Iterate between `DateQuarters`
```python
start = DateQuarter(2019, 1)
end = DateQuarter(2019, 4)
for quarter in DateQuarter.between(start, end):
    print(quarter)  # [DateQuarter(2019, 1), DateQuarter(2019, 2) , DateQuarter(2019,3)]
```
