# Testing Plan

## Overview
**Functions tested:**  
**Testing types:** Unit / Integration / Regression  
**Date:**  

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail |  Notes  |
|---------|-------------|----------|-----------------|------|-----------|---------|
|  01.    |Testprintlist|push,abc,1|Name: push, Description: abc, Time Spent: 1 minute | edge ||Steven|
|  02.    |Test reading a empty file|"","",""|"time: , description: "|edge||Tested by Leon
|  03.    |test create_activity|[],{"name": "jogging", "description":"running slowly for exercise", "time":30}|[{'name': 'jogging', 'description': 'running slowly for exercise', 'time': 30}]|normal case||Tested by Yiming|
|  04.    |test update_activity|["jogging", "0", ""]|[{'name': 'jogging', 'description': '', 'time': 0}]|edge case|Pass||
|  05.    |test delete_activity|{'name': 'jogging', 'description': 'running slowly for exercise', 'time': 30},"run"|"Can not found activity run"|error case|Pass||

## Code Used for Testing

```python
# Paste your Python test script here