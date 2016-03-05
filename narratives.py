# A class for storing narrative texts
# Michelle Kim
# Winter 2016
from textblob import TextBlob


class NarrativeSet:
    '''
    '''
    def __init__(self, narrative_type):
        self.type = narrative_type
        self.narratives = []
        self._sort_by_gender = None
        self._sort_by_age = None
        self._sort_by_education_level = None


    @property
    def narratives(self):
        return narratives

    def add_narrative(self, narrative):
        self.narratives.append(narrative)


    def sort_by_gender(self):
        accepted_genders = ['m', 'f', 'other']
        if self._sort_by_gender is None:
            d = {}
            for gender in accepted_genders:
                d[gender] = []
            for narrative in self.narratives:
                d[narrative.gender] = narrative
            self._sort_by_gender = d
        return self._sort_by_gender


    def sort_by_age(self):
        age_groups = {'child': (0, 13), 'teen': (13, 18), 
                      'young adult': (18, 26), 'adult': (26, 125}
        if self._sort_by_age is None:
            d = {}
            for group in age_groups:
                d[group] = []
            for narrative in self.narratives:
                for group, bounds in age_groups.items():
                    (lb, ub) = bounds
                    if narrative.age >= lb and narrative.age < ub:
                        d[group].append(narrative)
                        break
            self._sort_by_age = d
        return self._sort_by_age


    def sort_by_education_level(self):
        accepted_levels = ['high school', 'college', 'phd', 'N/A']
        if self._sort_by_education_level is None:
            d = {}
            for level in accepted_levels:
                d[level] = []
            for narrative in narratives:
                level = narrative.education_level
                d[level].append(narrative)
            self._sort_by_education_level = d
        return self._sort_by_education_level



class Narrative:
    '''
    Attributes:
        text:
        transcriber:
        gender:
        age:
        education_level:
        previous_residences:
        current_school:
        notes:
    '''
    def __init__(self, text):
        assert isinstance(text, str)
        self.text = text
        self.blob = TextBlob(text)
        self.transcriber = None
        self.gender = None
        self.age = None
        self.education_level = None
        self.previous_residences = []
        self.current_school = None
        self.notes = None


    @property
    def text(self):
        return self.text


    @property
    def transcriber(self):
        return self.transcriber

    @transcriber.setter
    def transcriber(self, transcriber):
        assert isinstance(transcriber, str)
        self.transcriber = transcriber


    @property
    def gender(self):
        return self.gender

    @gender.setter
    def gender(self, gender):
        assert isinstance(gender, str)
        accepted_genders = ['m', 'f', 'other']
        error ="Needs to be one of the following: {}".format(accepted_genders)
        if gender not in accepted_genders:
            print(error)
        self.gender = gender


    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        assert isinstance(age, (float, int, complex))
        self.age = age


    @property
    def education_level(self):
        return self.education_level

    @education_level.setter
    def education_level(self, education_level):
        assert isinstance(education_level, str)
        accepted_levels = ['high school', 'college', 'phd', 'N/A']
        error = "Needs to be one of the following: {}".format(accepted_levels)
        if education_level not in accepted_levels:
            print(error)
        self.education_level = education_level


    @property
    def previous_residences(self):
        return self.previous_residences

    def add_previous_residence(self, previous_residence):
        assert isinstance(previous_residence, str)
        self.previous_residences.append(previous_residence)


    @property
    def current_school(self):
        return self.current_school

    @current_school.setter
    def current_school(self, current_school):
        assert isinstance(current_school, str)
        self.current_school = current_school


    @property
    def notes(self):
        return self.notes

    @notes.setter
    def notes(self, notes):
        assert isinstance(notes, str)
        self.notes = notes
