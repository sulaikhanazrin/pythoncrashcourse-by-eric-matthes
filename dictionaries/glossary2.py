glossary = {
    'linux' : 'software',
    'variable' : 'value that may vary',
    'zen python' : 'rules of a good python programmer',
    'function range()' : 'generating numbers',
    'lists' : 'a collection of different values',
    }

gloss = glossary['linux'].title()
print(f"the linux is a {gloss}")

for name,values in glossary.items():
    print(f"{name.title()}: {values.title()}")
    
for name in glossary.keys():
    print(f"{name.title()}")    


learned = ['zen python','lists']
for name in glossary.keys():
    print(f"I learned {name.title()}")    
    if name in learned:
        sentence = glossary[name].title()
        print(f"\t{name.title()} : {sentence.title()}")    
        
if 'java' not in glossary.keys():
    print(f"you should study java")   
    
for name in sorted(glossary.keys()):
    print(f"{name.title()}, you should learn this")
    
print("the following are what i learned today")    
for gloss in glossary.values():
    print(f"{gloss.title()}")