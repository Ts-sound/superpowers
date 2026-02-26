# Flowchart Detailed Syntax

## Basic Syntax

```mermaid
graph TD
    A --> B
```

## Direction

Place after `graph`:

| Code | Direction |
|------|-----------|
| `graph TD` | Top to Down |
| `graph LR` | Left to Right |
| `graph RL` | Right to Left |
| `graph BT` | Bottom to Top |

## Node Shapes

| Syntax | Shape | Example |
|--------|-------|---------|
| `A` | Plain node | `A` |
| `A[]` | Rectangle | `A[Rectangle]` |
| `A()` | Rounded rectangle | `A(Rounded)` |
| `A((()))` | Circle | `A((Circle))` |
| `A>` | Half-circle | `A>Half]` |
| `A{}` | Diamond (decision) | `A{Decision}` |
| `A[/]` | Parallelogram | `A[/Parallelogram/]` |
| `A[\]` | Inverse parallelogram | `A[\Inverse/]` |
| `A[(())]` | Cylinder | `A[(Cylinder)]` |
| `A[[ ]]` | Double rectangle | `A[[Double]]` |

## Connection Types

| Syntax | Type | Example |
|--------|------|---------|
| `-->` | Solid arrow | `A --> B` |
| `---` | Solid line | `A --- B` |
| `-.->` | Dashed arrow | `A -.-> B` |
| `-. -` | Dashed line | `A -. - B` |
| `==>` | Thick solid arrow | `A ==> B` |
| `===` | Thick solid line | `A === B` |
| `\|label\|` | With label | `A -->\|Yes\| B` |

## Labels on Connections

```mermaid
graph TD
    A -->|Yes| B
    A -->|No| C
    A -.- |Maybe| D
```

## Subgraphs

```mermaid
graph TD
    subgraph Department A
        A1 --> A2
    end
    subgraph Department B
        B1 --> B2
    end
    A2 --> B1
```

Syntax:
```
subgraph Title
    Node1 --> Node2
end
```

## Styling with classDef

Define custom styles for nodes and apply them using the `class` keyword.

```mermaid
graph TD
    A["Explore project context"] --> B["Ask clarifying questions"];
    B --> C["Propose 2-3 approaches"];
    C --> D["Present design sections"];
    D --> E{"User approves design?"};
    E -->|no, revise| D;
    E -->|yes| F["Write design doc"];
    F --> G["Invoke writing-plans skill"];

    classDef endnode fill:#f9f;
    classDef decision fill:#ddf;
    classDef process fill:#e6f2ff;

    class G endnode;
    class E decision;
    class A,B,C,D,F process;
```

**Syntax:**
```
classDef styleName property:value,property2:value2
class NodeName1,NodeName2 styleName
```

## Complete Examples

### Simple Flow

```mermaid
graph TD
    A[Start] --> B[Process Data]
    B --> C{Success?}
    C -->|Yes| D[Save Result]
    C -->|No| E[Log Error]
    D --> F[End]
    E --> F
```

### System Architecture

```mermaid
graph LR
    subgraph Frontend
        A[User Interface]
        B[API Client]
    end
    subgraph Backend
        C[API Gateway]
        D[Business Logic]
        E[(Database)]
    end
    A --> B
    B --> C
    C --> D
    D --> E
```

## Common Use Cases

1. **Business process flows** - Use TD direction, diamond for decisions
2. **System architecture** - Use subgraph grouping, LR direction
3. **Decision trees** - Multiple levels of diamond decisions
4. **Organization charts** - Use TD for clear hierarchy
