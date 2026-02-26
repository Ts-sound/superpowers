# Timeline Detailed Syntax

## Basic Syntax

```mermaid
timeline
    title Timeline Title
    Time Period : Event Description
```

## Basic Structure

### Single Time Period

```mermaid
timeline
    2024 : Company Founded
```

### Multiple Time Periods

```mermaid
timeline
    2020 : Project Started
    2021 : Product Development
    2022 : Market Expansion
    2023 : Overseas Expansion
```

### With Subtitles

```mermaid
timeline
    2024 Q1 : Requirements Analysis : Complete market research
    2024 Q2 : System Design : Complete technology selection
    2024 Q3 : Development : Complete core features
    2024 Q4 : Testing & Launch : Official release
```

## Time Period Formats

| Format | Example |
|--------|---------|
| Year | `2024` |
| Quarter | `2024 Q1` |
| Month | `2024-01` |
| Date | `2024-01-15` |
| Range | `Jan-Mar` |

## Event Description

Separate main event and subtitle with `:`:
```
Time Period : Main Event : Subtitle : More Details
```

## Complete Examples

### Project Milestones

```mermaid
timeline
    title Project Development Milestones
    2024 Q1 : Requirements Analysis
    2024 Q2 : System Design
    2024 Q3 : Development
    2024 Q4 : Testing & Launch
    2025 Q1 : Optimization & Iteration
```

### Product History

```mermaid
timeline
    title Product Development History
    2020-01 : Product Initiation : Define product direction
    2020-06 : Version 1.0 : Basic features launch
    2021-03 : Version 2.0 : Add AI features
    2022-01 : Version 3.0 : Open platform
    2023-06 : 1M Users : Received funding
```

### Personal Growth Timeline

```mermaid
timeline
    title My Learning Journey
    2019 : Started Programming : Learn Python
    2020 : Frontend Development : React projects
    2021 : Backend Development : Spring Boot
    2022 : Full-Stack Engineer : Independent projects
    2023 : Tech Lead : Architecture design
```

## Common Use Cases

1. **Project history** - Record project development
2. **Product roadmap** - Show product planning
3. **Personal resume** - Career development timeline
4. **Company history** - Corporate milestones
5. **Version history** - Software release records
