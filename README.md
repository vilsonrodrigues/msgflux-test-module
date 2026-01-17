# msgflux-test-module

A simple test module for [msgflux](https://github.com/msgflux/msgflux) AutoModule.

## Usage

```python
import msgflux as mf

# Load the class from GitHub
GreetingModule = mf.AutoModule("vilsonrodrigues/msgflux-test-module")

# Instantiate
greeter = GreetingModule(language="pt")

# Use (calls forward method)
print(greeter("msgflux"))  # Olá, msgflux!
print(greeter("World"))    # Olá, World!
```

## Module Structure

- `config.json` - Module configuration
- `modeling.py` - Module implementation (inherits from `msgflux.nn.Module`)

## License

MIT
