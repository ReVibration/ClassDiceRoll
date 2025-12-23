# Random Number Name Generator

A Python script that reads names from a text file and appends a random number (0–6) to the end of each name, then saves the result to a new file.

## What this script does
- Reads a list of names from `names.txt`
- Adds a random number between 0 and 6 to each name
- Writes the updated names to `random.txt`

## Files used
- `names.txt`  
  Contains one name per line

- `random.txt`  
  Output file containing names with a random number appended

- `script.py`  
  Main Python script

## How to run
1. Ensure Python 3 is installed.
2. Make sure `names.txt` exists in the same folder as the script.
3. Run the script:

python script.py

4. Check `random.txt` for the output.

## Example

names.txt
Alice  
Bob  
Charlie  

random.txt
Alice3  
Bob0  
Charlie6  

## Notes
- Random numbers are generated using Python’s `random` module
- Numbers range from 0 to 6
- Each name must be on a new line in `names.txt`

## License
Educational use only.
