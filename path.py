from pathlib import Path

# check if folder exist
path = Path("first_pkg")
print(path.exists())

for file in path.glob('*.*'):
    print(file)

path2 = Path("emails")
#print(path2.mkdir())
#print(path2.rmdir())

for file in path.glob('*'):
    print(file)