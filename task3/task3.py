import json

tests = []
print("Введите путь до файла тестов")
with open(input()) as f:
    tests = json.load(f)

values = []
print("Введите путь до файла значений")
with open(input()) as f:
    values = json.load(f)

values = values['values']
def fill_values(test_data):
    if isinstance(test_data, dict):
      for key, value in test_data.items():
        if isinstance(value, dict):
          fill_values(value)
        elif isinstance(value, list):
          for i in range(len(value)):
            fill_values(value[i])
        elif isinstance(value, str) and key == 'value':
          for i in range(len(values)):
            if values[i]['id'] == test_data['id']:
              test_data[key] = values[i]['value']

fill_values(tests)

with open("report.json", 'w') as f:
    json.dump(tests, f, indent=4)