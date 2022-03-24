from ..extractors.personal_extractor import PersonalDataExtractor

PERSONAL_INFO_SEC = 'Personal Info.'
MILITARY_INFO_SEC = 'Military Data'

class PersonalData(PersonalDataExtractor):
    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        return {
            'name': self.name,
            'code': self.code,
            'relegion': self.religion,
            'gender': self.gender,
            'nationality': self.nationality,
            'birth': {
                'date':self.birth_date,
                'place':self.birth_place,
            },
            'id': {
                'number': self.id_number,
                'type': self.id_type,
                'date': self.id_date,
                'place': self.id_place,
            },
            'military': None if self.gender == 'female' \
            else {
                'state': self.military_state,
                'code': self.military_code,
                'date': self.military_date,
                'number': self.military_number,
                'notes': self.military_notes,
            },
        }

    '''
    Personal Information Section
    '''
    @property
    def name(self):
        return self.get_value(PERSONAL_INFO_SEC, 'Name')
    
    @property
    def code(self):
        return self.get_value(PERSONAL_INFO_SEC, 'Code')
    
    @property
    def religion(self):
        return self.get_value(PERSONAL_INFO_SEC, 'Religion')
    
    @property
    def gender(self):
        return self.get_value(PERSONAL_INFO_SEC, 'Gender')
    
    @property
    def nationality(self):
        return self.get_value(PERSONAL_INFO_SEC, 'Nationality')
    
    @property
    def birth_date(self):
        return self.get_value(PERSONAL_INFO_SEC, 'Birth Date')
    
    @property
    def birth_place(self):
        return self.get_value(PERSONAL_INFO_SEC, 'Birth Place')
    
    @property
    def id_number(self):
        return self.get_value(PERSONAL_INFO_SEC, 'ID Number')
    
    @property
    def id_type(self):
        return self.get_value(PERSONAL_INFO_SEC, 'ID Type')
    
    @property
    def id_date(self):
        return self.get_value(PERSONAL_INFO_SEC, 'ID Date')

    @property
    def id_place(self):
        return self.get_value(PERSONAL_INFO_SEC, 'ID Place')

    '''
    Military Information Section (Males Only)
    '''
    @property
    def military_state(self):
        return self.get_value(MILITARY_INFO_SEC, 'Military State')
    
    @property
    def military_code(self):
        return self.get_value(MILITARY_INFO_SEC, 'Military Code')
    
    @property
    def military_date(self):
        return self.get_value(MILITARY_INFO_SEC, 'Military Date')
    
    @property
    def military_number(self):
        return self.get_value(MILITARY_INFO_SEC, 'Military No.')
    
    @property
    def military_notes(self):
        return self.get_value(MILITARY_INFO_SEC, 'Notes')
