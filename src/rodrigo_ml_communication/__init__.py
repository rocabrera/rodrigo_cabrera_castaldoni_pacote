from importlib.metadata import version, PackageNotFoundError

try:
	__version__ = version('rodrigo-ml-communication')
except PackageNotFoundError:
	# package is not installed
	pass
