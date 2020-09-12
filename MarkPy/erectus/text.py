import re



def replace(text, target, changer, count=None):
    return text.replace(target, changer, count)


def between(text, start, end):
    match = re.match(r'{}'.format(f"^.*{start}(.*){end}.*$"), text)
    return match.group(1) if match else None
