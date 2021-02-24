"""Normal functions to test with separate file."""

def salutation(name):
	"""Say hello to someone."""
	return f"Hello, {name}!"


def repeatName(name, times):
	"""Repeat a name a number of times."""
	name_repeated = name * times
	return name_repeated


if __name__ == "__main__":
	print(salutation("Captain Luke"))