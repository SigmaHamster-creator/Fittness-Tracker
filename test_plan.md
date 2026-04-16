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
|  03.    |test create_activity|[jogging, 30, running slowly for exercise]|normal case||Tested by Yiming|
|  04.    |test update_activity|[jogging, , ]|edge case|Pass||
|  05.    |test delete_activity|run|error case|Fail||

## Code Used for Testing

```python
# Paste your Python test script here
