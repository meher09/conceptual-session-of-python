my_data = [
 {
  "name": "Ashraful Alam",
  "age": 45
 },
 {
  "name": "Taposh",
  "age": 48
 },
 {
  "name": "Aouwal",
  "age": 32
 },
 {
  "name": "Emran ",
  "age": 25
 },
 {
  "name": "Shorif ",
  "age": 28
 },
 {
  "name": "Taleb",
  "age": 56
 }
]


for person in my_data:
    print(f"{person.get('name')} is {person.get('age')} years old")
