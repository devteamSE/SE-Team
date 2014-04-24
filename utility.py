import re


def email_is_valid(email):
	if not re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+").match(email):
		return False
	if not len(re.findall('[a-zA-Z]',email[-1]))>0:
		return False
	if '@.' in email:
		return False
	return True


def dictfetchall(cursor, num_rows_to_fetch=1000000000):
	"""Returns all rows from a cursor as a dict"""
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchmany(size=num_rows_to_fetch)
	]
