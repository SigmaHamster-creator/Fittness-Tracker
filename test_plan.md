# Testing Plan

## Overview
**Functions tested:**  
**Testing types:** Unit / Integration / Regression  
**Date:**  

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail |  Notes  |
|---------|-------------|----------|-----------------|------|-----------|---------|
|  01.    |Testprintlist|push,abc,1|Name: push, Description: abc, Time Spent: 1 minute | edge |           |By:Steven|
|  02.    |Test reading a empty file|"","",""|"time: , description: "|edge||Tested by Leon
|  03.    |test add_activity|[jogging,running slowly for exercise,30]||normal case||Tested by Yiming|
|  04.    |test update_activity|[jogging, , ]||edge case|Pass||
|  05.    |test delete_activity|run|can not found activity run|error case|Fail||
|  06.    |test create_activity|push, 12 reps, 10|"name": "push", "description":"12 reps", "time":10|normal case|Pass|Tested by Danny|
|  07.    |test change_time|100|Invalid number, please try again!|error case|Fail|Tested by Danny|

## Code Used for Testing

```python
# Paste your Python test script here
