# State Diagram Detailed Syntax

## Basic Syntax

```mermaid
stateDiagram-v2
    [*] --> StateName
    StateName --> OtherState: Transition condition
    OtherState --> [*]
```

**Note:** Use `stateDiagram-v2` version, not the old `stateDiagram`

## States

### Simple State with ID Only

```mermaid
stateDiagram-v2
    State1
    State2
```

### State with Description (using state keyword)

```mermaid
stateDiagram-v2
    state "This is a state description" as State1
```

### State with Description (using colon)

```mermaid
stateDiagram-v2
    State1 : This is a state description
```

## Transitions

Transitions are represented using `-->` arrow syntax.

### Basic Transition

```mermaid
stateDiagram-v2
    State1 --> State2
```

### Transition with Label

```mermaid
stateDiagram-v2
    State1 --> State2: Transition label
```

### Self Transition

```mermaid
stateDiagram-v2
    State1 --> State1: Reprocess
```

## Start and End States

Use `[*]` syntax for start and end states. The direction determines if it's a start or end state.

```mermaid
stateDiagram-v2
    [*] --> StartState
    StartState --> EndState
    EndState --> [*]
```

## Composite States

Composite states contain internal states. Use `state` keyword with `{}` body.

### Basic Composite State

```mermaid
stateDiagram-v2
    state ParentState {
        ChildState1 --> ChildState2
    }
```

### Nested Composite States

```mermaid
stateDiagram-v2
    state Level1 {
        state Level2 {
            DeepState1 --> DeepState2
        }
    }
```

### Transitions Between Composite States

```mermaid
stateDiagram-v2
    state FirstComposite {
        StateA --> StateB
    }
    state SecondComposite {
        StateC --> StateD
    }
    StateB --> StateC
```

**Note:** You cannot define transitions between internal states belonging to different composite states.

## Choice

Model choices between paths using `<<choice>>`.

```mermaid
stateDiagram-v2
    state if_state <<choice>>
    [*] --> IsPositive
    IsPositive --> if_state
    if_state --> False: if n < 0
    if_state --> True : if n >= 0

```

## Forks and Joins

Specify forks and joins using `<<fork>>` and `<<join>>`.

```mermaid
   stateDiagram-v2
    state fork_state <<fork>>
      [*] --> fork_state
      fork_state --> State2
      fork_state --> State3

      state join_state <<join>>
      State2 --> join_state
      State3 --> join_state
      join_state --> State4
      State4 --> [*]

```

## Notes

Add notes to the left or right of a state.

```mermaid
stateDiagram-v2
    State1
    note right of State1: Note on the right
    State2
    note left of State2: Note on the left
```

## Concurrency

Specify concurrent states using `--` separator.

```mermaid
stateDiagram-v2
    [*] --> Active

    state Active {
        [*] --> NumLockOff
        NumLockOff --> NumLockOn : EvNumLockPressed
        NumLockOn --> NumLockOff : EvNumLockPressed
        --
        [*] --> CapsLockOff
        CapsLockOff --> CapsLockOn : EvCapsLockPressed
        CapsLockOn --> CapsLockOff : EvCapsLockPressed
    }

```

## Setting Diagram Direction

Control the rendering direction of the diagram.

```mermaid
stateDiagram-v2
    direction LR
    [*] --> State1
    State1 --> State2
    State2 --> [*]
```

**Direction options:**
- `TD` - Top to Down (default)
- `LR` - Left to Right
- `RL` - Right to Left
- `BT` - Bottom to Top

## Comments

Add comments using `%%` prefix. Comments are ignored by the parser.

```mermaid
stateDiagram-v2
    [*] --> State1
    %% This is a comment
    State1 --> State2 : Transition
```

## Styling with classDefs

Define and apply custom styles using `classDef`.

### Define a Style

```
classDef styleName property:value,property2:value2
```

**Example:**
```
classDef movement font-style:italic
classDef badEvent fill:#f00,color:white,stroke:yellow
```

### Apply Styles with `class` Statement

```mermaid
stateDiagram-v2
    classDef movement font-style:italic
    classDef badEvent fill:#f00,color:white
    
    [*] --> Moving
    Moving --> Crash
    class Moving movement
    class Crash movement, badEvent
    Crash --> [*]
```

### Apply Styles with `:::` Operator

```mermaid
stateDiagram-v2
    classDef danger fill:#f00,color:white
    
    [*] --> Safe:::danger
    Safe --> Danger
    Danger --> [*]
```

**Limitations:**
- Cannot be applied to start (`[*]`) or end states directly
- Cannot be applied to or within composite states

## Spaces in State Names

Use an ID with description for state names containing spaces.

```mermaid
stateDiagram-v2
    state "State with spaces" as sws
    [*] --> sws
    sws --> AnotherState
    class sws customStyle
```

## Complete Examples

### Order State Machine

```mermaid
stateDiagram-v2
    [*] --> PendingPayment
    PendingPayment --> Paid: Payment successful
    PendingPayment --> Cancelled: Timeout
    Paid --> Shipping: Merchant ships
    Shipping --> Completed: Confirm receipt
    Shipping --> Refunding: Request refund
    Refunding --> Completed: Refund successful
    Completed --> [*]
```

### User Authentication with Notes

```mermaid
stateDiagram-v2
    [*] --> LoggedOut
    LoggedOut --> LoggedIn: Login
    LoggedIn --> LoggedOut: Logout
    
    note right of LoggedOut: User is not authenticated
    note left of LoggedIn: User has valid session
```

## Common Use Cases

1. **Business processes** - Order, approval workflow states
2. **UI states** - Page and component state transitions
3. **Game states** - Game flow control (menu, playing, paused)
4. **Device control** - Machine and device state management
5. **User sessions** - Authentication and authorization states
6. **Protocol states** - Network protocol state machines
