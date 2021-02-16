
from wtforms import SelectField

def select_field(*args, **kwargs):
    '''
    Create a select field to display enum value
    @choices: [(val1, label1), (val2, label2), ...] or [label1, label2, ...]
    '''
    if kwargs.contains('choices'):
        choices = kwargs['choices']
        if len(choices) > 0 and isinstance(choices[0], str):
            choices = [(i, choices[i]) for i in range(len(choices))]
            kwargs['choices'] = choices
            kwargs['coerce'] = int
    return SelectField(*args, **kwargs)
