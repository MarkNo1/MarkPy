class Atom(object):
    '''
        Version v0.0.1                                           (TM)
        ______________


        Fan Fuct:
        __________

            An atom is the smallest constituent unit of ordinary matter that has
            the properties of a chemical element. Every solid, liquid, gas, and
            plasma is composed of neutral or ionized atoms. Atoms are extremely
            small;

                        typical sizes are around 100 picometers


            The picometre (international spelling as used by the International
            Bureau of Weights and Measures; SI symbol: pm) or picometer
            (American spelling) is a unit of length in the metric system;


                        equal to 1e12 meters.



             L'ångström (Å), o angstrom (pronuncia: /'ɔŋstrœm/), è un'unità di
             lunghezza non appartenente al Sistema internazionale (SI) corrispondente
             a 0,1 nm o 1×10−10 m[1].
             L'ångström prende nome dal fisico svedese Anders Jonas Ångström,
             uno dei padri della spettroscopia. Viene spesso impiegata per
             indicare le dimensioni delle molecole e degli atomi,
             il cui raggio varia tra 0,25 e 3 Å e per indicare la lunghezza dei
             legami chimici, compresi, di solito, tra 0,75 (molecola di H2) e 2 Å.


             1 Å = 100 pm = 0,1 nm = 1e-4 μm = 1e-7 mm = 13e-8 cm = 1e-10 m


        Arguments:
        __________

            Proton:     atom's protons
            Neutron:    atom's neutrons
            Electron:   atom's electrons


            Energy: atom's approximated Energy


            Dimension:  atom's dimension
            VDmension:  atom's virtual dimension in byte



                                                                 Treglia M.

    '''

    NameSpace = []

    def __init__(self, Name = 'Atom'):
        '''
            Init:
            _____

            Name: atom's name.


        '''
        self.Name = Name
        self.NameSpace + [ Name ]

        self.Dimension = 1e-12
        self.VDimension = 56

    @property
    def Name(self):
        return Name
    @Name.setter
    def Name(self, Name):
        self.Name = Name
    @Name.deleter
    def Name(self, Name):
        self.Name = Name
        
    def has_attribute(self, attribute):
        return hasattr(self, attribute)
