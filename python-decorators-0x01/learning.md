## generators
Generators are functions that yield values one at a time, instead of returning all values at once (like a list). This makes them memory-efficient, especially for large datasets.

- Use *yield* instead of *return*.
- Generator expressions are like list comprehensions, but use *()* instead of *[].*

*Like a water dispenser: you press the tap, and it gives you water on demand, instead of handing you the whole tank.*

### When to Use:
- Reading huge files line-by-line.
- Streaming data from APIs.
- Paginated DB results.

## decorator
A decorator is a function that wraps another function to modify or extend its behavior—without changing its source code.

- Use @decorator_name before a function.
- Use *args, **kwargs to make the decorator work for any function signature.

*Putting a phone case around your phone. The core (function) remains the same, but the case (decorator) adds new features (like grip, protection, or style).*

### When to Use:
- Logging
- Authentication
- Timing functions
- Input validation

## Context Managers: Clean Resource Management
Context managers are used to manage resources (like files or database connections) that need to be opened and closed properly.

- Use with statement.
- Create with __enter__ and __exit__ or with @contextmanager.

*Think of *with* like borrowing a book from the library—you open it (__enter__) and once done, you return it (__exit__).*
