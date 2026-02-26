# Class Diagram Detailed Syntax

## Basic Syntax

```mermaid
classDiagram
    class ClassName {
        Attributes
        Methods
    }
```

## Member Visibility

| Prefix | Visibility |
|--------|------------|
| `+` | Public |
| `-` | Private |
| `#` | Protected |
| `~` | Package |

## Member Types

| Symbol | Type |
|--------|------|
| (none) | Normal member |
| `*` | Static |
| `$` | Abstract |
| `()` | Method |

## Defining Classes

### Full Definition

```mermaid
classDiagram
    class User {
        -String username
        -String email
        +login()
        +logout()
    }
```

### Shorthand Definition

```mermaid
classDiagram
    class User
    User : -String username
    User : +login()
```

## Class Relationships

| Relationship | Syntax | Description |
|--------------|--------|-------------|
| Inheritance/Generalization | `<|--` | Subclass extends parent |
| Implementation | `<|..` | Class implements interface |
| Composition | `*--` | Strong ownership |
| Aggregation | `o--` | Weak ownership |
| Association | `-->` | Usage relationship |
| Dependency | `..>` | Temporary dependency |

### Labeled Relationships

```mermaid
classDiagram
    class A
    class B
    A --> B : uses
```

### Multiplicity Relationships

```mermaid
classDiagram
    User "1" *-- "0..*" Post
    Order "1" --> "1..*" Item
```

## Abstract Classes

```mermaid
classDiagram
    class Animal {
        #String name
        *void breathe()
        $void makeSound()
    }
```

## Interfaces

```mermaid
classDiagram
    class Animal {
        <<interface>>
        void makeSound()
    }
    
    class Dog {
        void bark()
    }
    
    Animal <|.. Dog
```

## Notes

```mermaid
classDiagram
    note "This is a general note"
    note for MyClass "This is a note for a class"
    class MyClass{
    }
```

## Complete Examples

### E-commerce System

```mermaid
classDiagram
    class User {
        -String username
        -String email
        +login()
        +logout()
        +placeOrder()
    }
    
    class Order {
        -String orderId
        -Date createTime
        +calculateTotal()
        +pay()
    }
    
    class Product {
        -String name
        -Double price
        -Integer stock
        +updateStock()
    }
    
    class Payment {
        <<interface>>
        +processPayment()
    }
    
    class Alipay {
        +processPayment()
    }
    
    class WechatPay {
        +processPayment()
    }
    
    User "1" --> "0..*" Order : places
    Order "1" --> "1..*" Product : contains
    Payment <|-- Alipay
    Payment <|-- WechatPay
    Order ..> Payment : uses
```

### MVC Architecture

```mermaid
classDiagram
    class Model {
        <<abstract>>
        #Map data
        #save()*
        #delete()*
    }
    
    class View {
        -String template
        +render()
        +update()
    }
    
    class Controller {
        -Model model
        -View view
        +handleRequest()
        +processInput()
    }
    
    class User
    class Product
    class Order
    
    Model <|-- User
    Model <|-- Product
    Model <|-- Order
    Controller o-- Model
    Controller o-- View
    View --> Model : reads data
```

## Common Use Cases

1. **Code structure** - Show classes, interfaces, relationships
2. **Design patterns** - Describe roles in patterns
3. **Database design** - Entity relationship diagrams
4. **System architecture** - Module dependencies
