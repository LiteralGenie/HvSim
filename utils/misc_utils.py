from ruamel.yaml import YAML

def load_yaml(file_path):
	txt= open(file_path).read()
	return YAML().load(txt)

def dump_yaml(data, file_path):
	with open(file_path, "w+") as f:
		YAML().dump(data)
	