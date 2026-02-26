# User Journey Detailed Syntax

## Basic Syntax

```mermaid
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 5: Me

```

## Structure

### Basic Elements

1. **title** - Journey title
2. **section** - Phase/group name
3. **Task items** - Specific tasks with score and participants

### Task Format

```
Task Description: Score (1-5): Participant 1, Participant 2
```

## Score Guide

| Score | Meaning |
|-------|---------|
| 5 | Very satisfied/Smooth |
| 4 | Satisfied |
| 3 | Neutral |
| 2 | Dissatisfied |
| 1 | Very dissatisfied |

## Participants

Can be any role:
- User
- System
- Support
- Merchant
- etc.

Separate multiple participants with commas.

## Complete Examples

### E-commerce Shopping Flow

```mermaid
journey
    title User Shopping Journey
    section Browse Products
      View product list: 5: User
      Search products: 4: User
      Filter products: 3: User
    section Place Order
      Add to cart: 4: User
      Fill address: 3: User, System
      Checkout payment: 5: User, System
    section Receive & Review
      Confirm receipt: 5: User
      Review product: 2: User
```

### User Registration Flow

```mermaid
journey
    title New User Registration Experience
    section Discover Product
      See advertisement: 3: User
      Visit website: 4: User
    section Register Account
      Enter email: 4: User
      Verify email: 3: User, System
      Set password: 4: User
    section Start Using
      Onboarding guide: 5: User, System
      Complete first action: 5: User
```

### Customer Support Flow

```mermaid
journey
    title Online Customer Support Journey
    section Start Inquiry
      Enter support page: 4: User
      Select issue type: 3: User
      Describe problem: 3: User
    section Problem Resolution
      AI support response: 2: User, System
      Transfer to human: 4: User, Support
      Wait for reply: 2: User
      Problem resolved: 5: User, Support
    section Service End
      Service rating: 4: User
```

## Design Guidelines

1. **Clear phase divisions** - Group by natural user experience stages
2. **Scores reflect real experience** - Low scores are optimization priorities
3. **Mark participants** - Clarify who participates in each task
4. **Cover complete flow** - Full journey from start to end

## Common Use Cases

1. **UX optimization** - Identify experience pain points
2. **Service design** - Design service flows
3. **Product improvement** - Discover product issues
4. **Customer journey** - Analyze customer experience
