# Gantt Chart Detailed Syntax

## Basic Syntax

```mermaid
gantt
    title A Gantt Diagram
    dateFormat YYYY-MM-DD
    section Section
        A task          :a1, 2014-01-01, 30d
        Another task    :after a1, 20d
    section Another
        Task in Another :2014-01-12, 12d
        another task    :24d
```

## Configuration

### Date Formats

| Format | Example |
|--------|---------|
| `YYYY-MM-DD` | 2024-01-15 |
| `YYYY-MM` | 2024-01 |
| `MM-DD` | 01-15 |
| `YYYY-MM-DD HH:mm` | 2024-01-15 10:00 |

### Axis Configuration

```
axisFormat %Y-%m-%d
todayMarker off
```

## Task States

| State | Description | Display |
|-------|-------------|---------|
| `done` | Completed | Gray |
| `active` | In progress | Blue highlight |
| `crit` | Critical task | Red |
| `milestone` | Milestone | Diamond marker |

## Time Definitions

### Absolute Time
```
Task1 : 2024-01-01, 2024-01-10
Task2 : 2024-01-05, 7d
```

### Relative Time
```
Task1 : 2024-01-01, 7d
Task2 : after Task1, 5d
Task3 : after Task2, 3d
```

### Duration Units
- `d` - Days
- `w` - Weeks
- `h` - Hours
- `m` - Minutes

## Section Grouping

```mermaid
gantt
    title Project Development Plan
    dateFormat YYYY-MM-DD
    axisFormat %m-%d
    section Design Phase
    Requirements Analysis :done, des1, 2024-01-01, 7d
    Technical Design :active, des2, after des1, 5d
    section Development Phase
    Frontend Development :dev1, after des2, 10d
    Backend Development :dev2, after des2, 12d
    section Testing Phase
    Unit Testing :test1, after dev1, 5d
    Integration Testing :test2, after dev2, 7d
```

## Milestones

```
Project Kickoff :milestone, m1, 2024-01-01, 0d
Project Launch :milestone, m2, 2024-03-31, 0d
```

## Complete Example

### Project Development Plan

```mermaid
gantt
    title Project Development Plan
    dateFormat YYYY-MM-DD
    axisFormat %m-%d
    
    section Requirements
    Requirements Research :done, req1, 2024-01-01, 5d
    Requirements Analysis :done, req2, after req1, 5d
    Requirements Review :milestone, m1, 2024-01-10, 0d
    
    section Design
    High-Level Design :active, des1, 2024-01-11, 5d
    Detailed Design :des2, after des1, 5d
    
    section Development
    Environment Setup :crit, dev1, 2024-01-16, 3d
    Core Features :crit, dev2, after dev1, 10d
    Supporting Features :dev3, after dev1, 8d
    
    section Testing
    Unit Testing :test1, after dev2, 5d
    Integration Testing :test2, after dev3, 7d
    Production Release :milestone, m2, 2024-02-28, 0d
```

## Advanced Configuration

### Exclude Weekends
```
includes
    excludes weekends
```

### Time Range
```
title Project Plan
dateFormat YYYY-MM-DD
axisFormat %m-%d
```

## Common Use Cases

1. **Project planning** - Multi-phase, multi-task project scheduling
2. **Progress tracking** - Mark progress with done/active states
3. **Critical path** - Mark critical tasks with crit
4. **Milestone management** - Mark important checkpoints
