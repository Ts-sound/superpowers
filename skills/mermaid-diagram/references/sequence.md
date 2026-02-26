# Sequence Diagram Detailed Syntax

## Basic Syntax

```mermaid
sequenceDiagram
    participant A as Participant A
    participant B as Participant B
    A->>B: Message content
```

## Participants

### Define Participants

```
participant Name
participant Alias as Display Name
```

### Participant Types

| Syntax | Shape |
|--------|-------|
| `participant A` | Rectangle |
| `actor A` | Actor icon |
| `boundary A` | Boundary box |
| `control A` | Control circle |
| `entity A` | Entity box |
| `database A` | Cylinder |

## Message Types

| Syntax | Type | Description |
|--------|------|-------------|
| `A->>B` | Solid arrow | Synchronous message |
| `A-->>B` | Dashed arrow | Return message |
| `A->B` | Solid line | Synchronous (no arrow) |
| `A--B` | Dashed line | Dashed message |
| `A-xB` | Solid cross | Destroy/terminate |
| `A--xB` | Dashed cross | Dashed terminate |
| `A-)B` | Open arrow | Asynchronous message |
| `A--)B` | Dashed open | Dashed asynchronous |

## Activation Bars

```mermaid
sequenceDiagram
    A->>B: Request
    activate B
    B-->>A: Response
    deactivate B
```

Or shorthand:
```
A->>+B: Request (auto-activate)
B-->>-A: Response (auto-deactivate)
```

## Notes

```mermaid
sequenceDiagram
    Note over A,B: Note over A and B
    Note right of A: Note on right of A
    Note left of B: Note on left of B
```

## Conditional Branches

### Alt (if-else)

```mermaid
sequenceDiagram
    alt Condition met
        A->>B: Execute action
    else Condition not met
        A->>B: Execute alternative
    end
```

### Opt (Optional)

```mermaid
sequenceDiagram
    opt Optional action
        A->>B: Execute
    end
```

### Loop

```mermaid
sequenceDiagram
    loop Loop description
        A->>B: Repeat execution
    end
```

### Par (Parallel)

```mermaid
sequenceDiagram
    par Parallel execution
        A->>B: Action 1
    and
        A->>C: Action 2
    end
```

## Create Participants Dynamically

```mermaid
sequenceDiagram
    A->>B: Create
    create participant C
    B->>C: Use new object
```

## Auto Numbering

```
sequenceDiagram
    autonumber
    participant A
    participant B
```

## Complete Examples

### User Login Flow

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant S as System
    participant D as Database
    
    U->>S: Login request
    activate S
    S->>D: Verify user info
    activate D
    D-->>S: Return verification
    deactivate D
    alt Verification success
        S-->>U: Login successful
    else Verification failed
        S-->>U: Login failed
    end
    deactivate S
```

### API Call

```mermaid
sequenceDiagram
    participant C as Client
    participant G as Gateway
    participant S as Service
    
    C->>+G: HTTP Request
    G->>+S: Forward Request
    S-->>-G: Response
    G-->>-C: HTTP Response
    
    opt Error handling
        C->>G: Retry
    end
```

## Common Use Cases

1. **API interactions** - Calls between client, gateway, service
2. **User flows** - User interactions with system
3. **Protocol specifications** - Message exchange in network protocols
4. **Async processing** - Using async messages and parallel execution
