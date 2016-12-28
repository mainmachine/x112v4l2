"""
	Gtk doesn't give us all the tools we need, so here's some more
"""

def find_child_by_id(root, name):
	"""
		Searches through a hierarchy of Gtk widgets for the `name`d
		
		Returns None if no such child was found.
	"""
	# We do a breadth-first search
	next_level = [root]
	while next_level:
		children = next_level
		next_level = []
		for child in children:
			if child.get_name() == name:
				# Bingo
				return child
			if hasattr(child, 'get_children'):
				next_level.extend(child.get_children())
	# Hierarchy exhausted. Ho hum.
	
