
T = '''
name: to-init
val_1: 1
val_2: 2.0
val_3: 1e1
val_4: 1e1 * 4
val_5: [5]
val_6: "@do hash('a6')"
val_7: "@do dict(b7=hash('b7'))"

'''

class Matrix:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.creation_date = datetime()
        self.creation_time = clock()
        self.destruction_date: datetime = None
        self.was_init = False
        self.rand_id = random()

    def __eq__(self, other):
        return self.version == other.version and self.creation_date == other.creation_date and self.creation_time == other.creation_time

    def __hash__(self):
        return hash((self.name, self.version, self.creation_time, self.rand_id))

    def init(self):
        self.was_init = True


class AtomHistory:

    def __init__(self, name, version):
        class_details = ClassDetails(name=name, version=version)
        self.classes = {name: class_details}
        self.classes_history_hash = [self.__hash__()]

    def __eq__(self, other):
        return self.classes == other.classes

    def __hash__(self):
        _hashes = []
        for atom in self.classes:
            _hashes += [hash(self.classes[atom])]
        return hash(tuple(_hashes))

    def add(self, name, version):
        self.classes[name] = ClassDetails(name=name, version=version)
        self.classes_history_hash.append(self.__hash__())

    def show(self):
        return str(self.classes), str(self.classes_history_hash)

    def get_names(self):
        return list(self.classes.keys())

    def get_versions(self):
        return [v.version for k, v in self.classes.items()]

    def set_class_init(self, name):
        self.classes[name].init()

    def __call__(self, name):
        return self.classes[name]
