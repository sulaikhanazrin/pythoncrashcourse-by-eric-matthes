favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()},thankyou for taking the poll!")

print("the following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())
for language in set(favorite_languages.values()):
    print(language)
    
    
    
    