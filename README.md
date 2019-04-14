## Persistent Numbers

Inspired by Numberphile: https://www.youtube.com/watch?v=Wim9WJeDTHQ

## Dependencies
* numpy

## Usage
This repo contains two different programs, `solve.py` which tells you how many steps a number has, and `gen.py`, which helps determine what steps might exist from a number.

### Solver
```bash
py solve.py <number> [<base>]
```

`number` is the number you want to see how many steps exist for (this is in the base you want to test).

`base` is the base you want to test it in (defaults to 10)

### Generator
```bash
py gen.py <start> <steps> [<base> <extraDigits>]
```

`start` is the number you want to start the test from (always in base 10)

`steps` are the number of steps you want to try to reach (the program will stop however if it can't find any more numbers to test)

`base` is the base you want to test in (defaults to 10)

`extraDigits` the number of digits you want to append to each test (e.g. extraDigits=3, 54 -> 99999)

## Testing
There is pretty exhaustive unit testing, the files are adjacent to their source and cover a good chunk of the possible interfaces.

## License
This code is protected by the MIT license. Feel free to reach out if there's any part of this project you would like to use or better understand!
