privacy_agreement = 'My name is {}. I agree to follow the {} and {}.'
print(privacy_agreement.format('Esmaeil MIRZAEE', 'privacy', 'license'))

privacy_agreement = 'My name is {name}. I agree to follow the {first_section} and {second_section}.'
print(privacy_agreement.format(name = 'Esmaeil', first_section = 'privacy', second_section = 'license'))

privacy_agreement = 'My name is {0}. I agree to follow the {1} and {2}.'
print(privacy_agreement.format('Esmaeil', 'privacy', 'license'))
