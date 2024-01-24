# Item Generator

This project is a Python application that generates random items, parts, and attributes.

## Features

- Generate random attributes for a given part type.
- Generate random parts with random attributes for a given part type.
- Generate random items with random parts for a given item type.

## How to Use

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Update `constants.py` to include your desired item configuration.
4. Update `main.py` to import and use your custom item(s).
5. Run the `main.py` script to start the application.

```sh
python main.py
```

Please note that this application requires Python 3.6 or later.

## Files

- `attribute.py`: Defines the `Attribute` class.
- `item.py`: Defines the `Item` and `ItemType` classes.
- `part.py`: Defines the `Part` and `PartType` classes.
- `generator.py`: Contains functions to generate random attributes, parts, and items.
- `main.py`: The entry point of the application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## TODO:
- write a better readme
- add configurable randomness weights
- add more complex attributes to parts
- add additional meta to items
- add tests
- add docs
- add item templates
- organize repo structure
