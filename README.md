# Fitness-Tracker

## Description

This program allows user to record their fitness activity including name, a description and time spent. The user can choose whether to create, display, delete, update activity, or change time spent of their activity. The activity created is automatically saved and can be read and used at any time.

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone the repository from GitHub.
3. Open the folder in VS Code.
4. Make sure Data.txt and Fitness-Tracker.py is included in the same folder.
5. Open the terminal.
6. Run the program using:

```python
python Fitness-Tracker.py
```

## Example input/output 1:(Add and view)

- Input: 

```python
1#Add Activity (With time)
run
slow pace
60

2#View List
```

- Output:

```python
Activity added!

1. Name: run | Description: slow pace | Time: 60 Minutes
Total time spent: 60 Minutes
```

## Example input/output 2:(Add,Remove and view)

- Input: 

```python
1#Add Activity (With time)
run
slow pace
60

3#Remove Activity
run

2#View List
```

- Output:

```python
Activity added!

Activity removed!

No activities yet
Total time spent: 0 Minutes
```

## Example input/output 3:(Add,update and view)

- Input: 

```python
1#Add Activity (With time)
run
slow pace
60

4#Update Activity
run
120
marathon

2#View List
```

- Output:

```python
Activity added!

Activity updated!

1. Name: run | Description: marathon | Time: 120 Minutes
Total time spent: 120 Minutes
```
