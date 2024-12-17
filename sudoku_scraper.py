from bs4 import BeautifulSoup
from flask import Flask, render_template
import requests, json


def convertList(puzzle_data: list[int]) -> str:
    convertedList = '' 
    for val in puzzle_data:
        if val != 0:
            convertedList += str(val)
        else:
            convertedList += '-'
    return convertedList

url = "https://www.nytimes.com/puzzles/sudoku/easy"


# Scrape the NY times website for puzzles
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
div_tag = doc.find(class_="pz-content pz-hide-loading")
script_tag = div_tag.find("script")

# Extract the JavaScript code
script_content = script_tag.text

# Locate the start and end of the JSON data
start_index = script_content.find('{')
end_index = script_content.rfind('}') + 1

# Extract the JSON data
json_data = script_content[start_index:end_index]

# Parse the JSON data
game_data = json.loads(json_data)

# Access the puzzle data
easy_puzzle_data: list[int] = game_data['easy']['puzzle_data']['puzzle']
medium_puzzle_data: list[int] = game_data['medium']['puzzle_data']['puzzle']
hard_puzzle_data: list[int] = game_data['hard']['puzzle_data']['puzzle']

easy_puzzle_data_solution: list[str] = game_data['easy']['puzzle_data']['solution']
medium_puzzle_data_solution: list[str] = game_data['medium']['puzzle_data']['solution']
hard_puzzle_data_solution: list[str] = game_data['hard']['puzzle_data']['solution']

app = Flask(__name__)

@app.route('/')
def index():
    easy_py = [convertList(easy_puzzle_data), convertList(easy_puzzle_data_solution)]
    medium_py = [convertList(medium_puzzle_data), convertList(medium_puzzle_data_solution)]
    hard_py = [convertList(hard_puzzle_data), convertList(hard_puzzle_data_solution)]

    easy_json = json.dumps(easy_py)
    medium_json = json.dumps(medium_py)
    hard_json = json.dumps(hard_py)

    return render_template('sudoku.html', easy_py=easy_json, medium_py=medium_json, hard_py=hard_json)

if __name__ == '__main__':
    app.run(debug=True)